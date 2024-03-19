
from flask import Blueprint, render_template, flash, redirect, current_app, url_for, session, request #, jsonify

from app.models.order import Order
from web_app.routes.wrappers import authenticated_route

order_routes = Blueprint("order_routes", __name__)

#
# USER ORDERS
#

@order_routes.route("/user/orders")
@authenticated_route
def orders():
    print("USER ORDERS...")
    current_user = session.get("current_user")
    #service = current_app.config["SPREADSHEET_SERVICE"]
    #orders = service.get_user_orders(current_user["email"])
    orders = Order.filter_by(user_email=current_user["email"])
    return render_template("user_orders.html", orders=orders)


@order_routes.route("/user/orders/create", methods=["POST"])
@authenticated_route
def create_order():
    print("CREATE USER ORDER...")

    form_data = dict(request.form)
    print("FORM DATA:", form_data)
    product_id = form_data["product_id"]
    product_name = form_data["product_name"]
    product_price = form_data["product_price"]

    current_user = session.get("current_user")
    user_email = current_user["email"]

    #service = current_app.config["SPREADSHEET_SERVICE"]
    try:
        order = Order({
            "user_email": user_email,
            "product_id": int(product_id),
            "product_name": product_name,
            "product_price": float(product_price)
        })
        order.save()
        flash(f"Order received!", "success")
        return redirect("/user/orders")
    except Exception as err:
        print(err)
        flash(f"Oops, something went wrong: {err}", "warning")
        return redirect("/products")
