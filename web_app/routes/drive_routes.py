
from flask import Blueprint, render_template, request, flash, redirect, session #, current_app

from io import BytesIO
from googleapiclient.http import MediaIoBaseUpload #MediaFileUpload

from app.drive_service import get_folder_id, get_drive_service


drive_routes = Blueprint("drive_routes", __name__)


@drive_routes.route("/submissions/form")
def submission_form():
    return render_template("deliverable_submission_form.html")


@drive_routes.route("/submissions/upload", methods=["POST"])
def submission_upload():
    form_data = dict(request.form)
    print("FORM DATA:", form_data)
    print("FILES:", request.files)

    try:
        course_name = form_data["course_name"]
        assignment_name = form_data["assignment_name"]

        selected_file = request.files["selected_file"]
        filename = selected_file.filename
        mimetype = selected_file.mimetype
        print(selected_file)
        print(selected_file.filename)
        print(selected_file.mimetype)
        print(selected_file.content_type)
        print(selected_file.content_length)
        #> <FileStorage: 'Rock_Paper_Scissors_(Spring_2024)_SOLUTIONS.ipynb' ('application/octet-stream')>

        file_content = BytesIO(selected_file.read())
        print(type(file_content))
        media = MediaIoBaseUpload(file_content, mimetype=mimetype, resumable=True)
        print("MEDIA:", media)

        # USER INFO
        current_user = session.get("current_user")
        email_address = current_user["email"]

        # UPLOAD TO DRIVE

        drive_service = get_drive_service()

        folder_id = get_folder_id(course_name, assignment_name)
        #net_id = email_address.split("@")[0]
        #filename = filename.lower().split(".ipynb")[0] + " - " + net_id + ".ipynb"
        #> 'rock_paper_scissors_(spring_2024)_solutions - first.last.ipynb'
        file_metadata = {
            'name': filename,
            'parents': [folder_id],
        }
        print("METADATA:", file_metadata)

        drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()

        flash("File Uploaded Successfully", "success")
        return redirect("/submissions/form")
    except Exception as err:
        print("OOPS", err)
        flash("OOPS, Something went wrong. Please try again.", "warning")
        return redirect("/submissions/form")
