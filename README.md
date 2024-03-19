# flask-sheets-template-2024

A web application starter template, created in Python with the Flask framework. Allows users to login with their Google accounts (via OAuth). Interfaces with a Google Sheets database.

![](https://user-images.githubusercontent.com/1328807/160312385-7ffbbada-4363-4b48-873d-9eca868afef0.png)

## Prerequisites

This application requires a Python development environment:

  + Git
  + Anaconda, Python, Pip

For beginners, here are some instructions for how to install Anaconda, and [set up your local Python development environment](https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/local-dev-setup/README.md#option-b-full-setup).

## Repo Setup

Make a copy of this template repo (as necessary). Clone your copy of the repo onto your local machine. Navigate there from the command-line.

Setup and activate a new Anaconda virtual environment:

```sh
conda create -n flask-sheets-2024 python=3.10
conda activate flask-sheets-2024
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Services Setup

This app requires a few services, for user authentication and data storage. Follow the instructions below to setup these services.

1. Follow the [Google Cloud Setup](/admin/GOOGLE_CLOUD.md) guide to configure a Google Cloud project to facilitate user logins and programmatic access to Google APIs. Obtain and configure client credentials (via environment variables) and service account credentials (via JSON file).

2. Follow the [Google Sheets Database Setup](/admin/GOOGLE_SHEETS.md) guide to setup the google sheets database.

3. If you would like to configure Google Analytics, optionally consult the [Google Analytics Setup](/admin/GOOGLE_ANALYTICS.md) guide.


## Configuration

### Environment Variables

Create a file called ".env" in the root directory of this repository, and populate it with environment variables to specify your own credentials, as obtained in the "Setup" section above:

```sh
FLASK_APP="web_app"

#
# GOOGLE OAUTH
#
GOOGLE_CLIENT_ID="____________"
GOOGLE_CLIENT_SECRET="____________"

#
# GOOGLE SHEETS DATABASE
#
GOOGLE_SHEETS_DOCUMENT_ID="____________"

#
# GOOGLE ANALYTICS
#
GA_TRACKER_ID="UA-XXXXXXX-1"

#
# FRONT END CUSTOMIZATIONS
#

```




## Usage

### Sheets Service

Interfacing with the Google Sheets database:

```sh
python -m app.spreadsheet_service
```

### Sheets Database

Fetch records from Google Sheets database, and populate with example records (i.e. "seeds"):

```sh
python -m app.models.product

python -m app.models.order
```



### Web Application

Run the local web server (then visit localhost:5000 in a browser):

```sh
FLASK_APP=web_app flask run
```




## Testing

Setup a separate Google Sheet to use as the test document. Note its identifier and set environment variable `GOOGLE_SHEETS_TEST_DOCUMENT_ID` accordingly, via the ".env" file. Setup the sheets in the same way you would set up the normal google sheet database. Also setup a "books" sheet with columns "id", "title", "author", "year", "created_at", and "updated_at".

Run tests:

```sh
pytest
```

> NOTE: we are using a live sheet for testing, so to avoid API rate limits, we are waiting / sleeping between each test, which makes the tests a bit slow for now


## CI

See more information about the [CI](/admin/GITHUB_ACTIONS.md) build process.

Running tests in CI mode:

```sh
CI=true pytest
```

## Deploying

See the [Deployer's Guide](/admin/RENDER.md) for instructions on deploying to a production server hosted by Render.



## [License](/LICENSE.md)
