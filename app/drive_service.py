from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

from app.google_apis import GOOGLE_CREDENTIALS_FILEPATH



def upload_file_to_drive(file_path, folder_id, credentials_json=GOOGLE_CREDENTIALS_FILEPATH):
    """
    Upload a file to Google Drive.

    :param credentials_json: Path to the credentials JSON file.
    :param file_path: Path to the local file to be uploaded.
    :param folder_id: (Optional) Google Drive folder ID where the file will be uploaded.
                      If not provided, the file will be uploaded to the root directory.
    :return: The file ID of the uploaded file.
    """

    # need to enable the google drive api from the google cloud console first
    credentials = service_account.Credentials.from_service_account_file(
        credentials_json, scopes=['https://www.googleapis.com/auth/drive.file']
    )
    # Build the Drive API service
    drive_service = build('drive', 'v3', credentials=credentials)

    # Define the file metadata
    file_metadata = {'name': file_path.split('/')[-1]} # # Extracts the file name from the path

    if folder_id:
        file_metadata['parents'] = [folder_id]

    breakpoint()

    media = MediaFileUpload(file_path, resumable=True)

    #uploaded_file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    # get all fields:
    #uploaded_file = drive_service.files().create(body=file_metadata, media_body=media, fields='*').execute()
    fields = ", ".join(["id", "name", "originalFilename", "parents", "quotaBytesUsed", "size", "webContentLink", "webViewLink"])
    uploaded_file = drive_service.files().create(body=file_metadata, media_body=media, fields=fields).execute()

    # Return the file ID
    return uploaded_file.get('id')

# Example usage
if __name__ == '__main__':


    import os

    filepath = os.path.join(os.path.dirname(__file__), "..", "test", "notebooks", "Spotify_API_Demo_(Summer_2024).ipynb")
    assert os.path.isfile(filepath)

    # need to share folder > editor access with service account email address
    folder_id = '1OIPp3BkjUwMZSpKMn_PW9RozdpmRqBno'

    file_id = upload_file_to_drive(filepath=filepath, folder_id=folder_id)
    print(f"File uploaded successfully with ID: {file_id}")
