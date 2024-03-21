### Google Cloud Setup

1. Visit the [Google Cloud Console](https://console.cloud.google.com). Create a new project, and name it. After it is created, select it from the project selection dropdown menu.

![alt text](/.github/markdown-images/image-3.png)
![alt text](/.github/markdown-images/image-4.png)

### Google OAuth Client

Visit the [API Credentials](https://console.cloud.google.com/apis/credentials) page for your Google Cloud project. Click the button with the plus icon to "Create Credentials", and choose "Create OAuth Client Id".

Click to "Configure Consent Screen". Leave the domain info blank, and leave the defaults / skip lots of the setup for now. If/when you deploy your app to a production server, you can return to populating this info (or you will be using a different project).

You should see a screen like this after clicking through the Consent Screen settings.

![alt text](/.github/markdown-images/image-6.png)

Return to actually creating the "OAuth Client Id". Choose a "Web application" type, give it a name, and set the following "Authorized Redirect URIs" (for now, while the project is still in development):

#### http://localhost:5000/auth/google/callback

![alt text](/.github/markdown-images/image-7.png)

After the client is created, note the `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET` (right side of the screen below). You'll need these to set up your env file below.

![alt text](/.github/markdown-images/image-8.png)

### Google Cloud Service Account Credentials

To fetch data from the Google Sheets database (and use other Google APIs), the app will need access to a local "service account" credentials file.

From the [Google API Credentials](https://console.cloud.google.com/apis/credentials) page, create a new service account as necessary.

For the chosen service account, create new JSON credentials file as necessary from the "Keys" menu, then download the resulting JSON file into the root directory of this repo, specifically named "google-credentials.json".

![alt text](/.github/markdown-images/image-9.png)

### Enabling APIs

In the Google APIs project console, from the "Enabled APIs and Services" page, search for and enable the "Google Sheets API".

If you would like to use additional APIs in the future (for example Google Calendar API for a calendar integration), you will need to come back and enable them sepearately in the future.
