from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

from app.google_apis import GOOGLE_CREDENTIALS_FILEPATH


def get_folder_id(course_id, assignment_id):
    # todo: lookup folder id given it's course id and assignment id
    return '1OIPp3BkjUwMZSpKMn_PW9RozdpmRqBno'


def get_drive_service(credentials_json=GOOGLE_CREDENTIALS_FILEPATH):
    # need to enable the google drive api from the google cloud console first
    credentials = service_account.Credentials.from_service_account_file(
        credentials_json,
        scopes=['https://www.googleapis.com/auth/drive.file']
    )
    drive_service = build('drive', 'v3', credentials=credentials)
    return drive_service



def upload_file_to_drive(file_path, folder_id=None):
    """
    Upload a file to Google Drive.

    Params:
        file_path (str): Path to the local file to be uploaded.

        folder_id (str, optional): Google Drive folder ID where the file will be uploaded.
            If not provided, the file will be uploaded to the root directory.

    Returns:
        str: The file ID of the uploaded file.
    """

    drive_service = get_drive_service()

    file_metadata = {'name': file_path.split('/')[-1]}
    if folder_id:
        file_metadata['parents'] = [folder_id]

    media = MediaFileUpload(file_path, resumable=True)

    #uploaded_file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    # get all fields:
    #uploaded_file = drive_service.files().create(body=file_metadata, media_body=media, fields='*').execute()
    fields = ", ".join(["id", "name", "originalFilename", "parents", "quotaBytesUsed", "size", "webContentLink", "webViewLink"])
    uploaded_file = drive_service.files().create(body=file_metadata, media_body=media, fields=fields).execute()

    return uploaded_file #> {}


if __name__ == '__main__':


    import os
    from pprint import pprint

    filepath = os.path.join(os.path.dirname(__file__), "..", "test", "notebooks", "Spotify_API_Demo_(Summer_2024).ipynb")
    assert os.path.isfile(filepath)

    # need to share folder > editor access with service account email address
    folder_id = '1OIPp3BkjUwMZSpKMn_PW9RozdpmRqBno'

    uploaded_file = upload_file_to_drive(filepath=filepath, folder_id=folder_id)
    pprint(uploaded_file)
