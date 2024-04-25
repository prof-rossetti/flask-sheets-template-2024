
from flask import session, flash, redirect, current_app
from flask import Blueprint, session, redirect, url_for, render_template #request, , , jsonify

from app.models.login import Login

auth_routes = Blueprint("auth_routes", __name__)

@auth_routes.route("/login")
def login():
    print("LOGIN...")
    return render_template("login.html")

@auth_routes.route("/auth/google/login")
def google_login():
    print("GOOGLE OAUTH LOGIN...")
    oauth = current_app.config["OAUTH"]
    redirect_uri = url_for("auth_routes.google_oauth_callback", _external=True) # see corresponding route below
    return oauth.google.authorize_redirect(redirect_uri) # send the user to login with google, then hit the callback route

@auth_routes.route("/auth/google/callback")
def google_oauth_callback():
    print("GOOGLE OAUTH CALLBACK...")
    oauth = current_app.config["OAUTH"]
    token = oauth.google.authorize_access_token()
    user_info = token.get("userinfo")
    if user_info:
        print("STORING USER INFO IN THE SESSION...")
        #print(user_info)
        #> {
        #>     'at_hash': '______',
        #>     'aud': '______.apps.googleusercontent.com',
        #>     'azp': '______.apps.googleusercontent.com',
        #>     'email': '______@gmail.com',
        #>     'email_verified': True,
        #>     'exp': 1712683963,
        #>     'family_name': 'Student',
        #>     'given_name': 'Sally',
        #>     'iat': 1712680363,
        #>     'iss': 'https://accounts.google.com',
        #>     'name': 'Sally Student',
        #>     'nonce': '______',
        #>     'picture': 'https://lh3.googleusercontent.com/a/______',
        #>     'sub': '______'
        #> }
        print("USER INFO:", user_info["email"], user_info["name"])

        # add user info to the session:
        session["current_user"] = user_info

        # consider storing the user login info in the database:
        Login.create({
            "email": user_info["email"],
            "verified": user_info["email_verified"],
            "first_name": user_info["given_name"],
            "last_name": user_info["family_name"],
            "profile_photo_url": user_info["picture"],
        })

    else:
        print("NO USER INFO")
    return redirect("/")

@auth_routes.route("/logout")
def logout():
    print("LOGGING OUT...")
    session.pop("current_user", None) # remove user info from the session
    return redirect("/")
