
import pytest
import os
from time import sleep

from dotenv import load_dotenv

from app.spreadsheet_service import SpreadsheetService
from app.models.base import BaseModel
from app.models.book import Book
from app.models.product import Product

from web_app import create_app

load_dotenv()

# an example sheet that is being used for testing purposes:
GOOGLE_SHEETS_TEST_DOCUMENT_ID= os.getenv("GOOGLE_SHEETS_TEST_DOCUMENT_ID")
TEST_SLEEP = int(os.getenv("TEST_SLEEP", default="10"))


@pytest.fixture()
def ss():
    """Spreadsheet service connected to the test document. Sleeps to avoid rate limits."""
    ss = SpreadsheetService(document_id=GOOGLE_SHEETS_TEST_DOCUMENT_ID)

    yield ss

    print("SLEEPING...")
    sleep(TEST_SLEEP)


@pytest.fixture()
def model_context():
    """Use this fixture and subsequent model calls will be made against the test database."""
    BaseModel.set_document_id(GOOGLE_SHEETS_TEST_DOCUMENT_ID)
    assert BaseModel.ss.document_id == GOOGLE_SHEETS_TEST_DOCUMENT_ID
    assert Book.ss.document_id == GOOGLE_SHEETS_TEST_DOCUMENT_ID

    yield "Using test document!"


#@pytest.fixture()
#def books_context(model_context):
#
#    #BaseModel.set_document_id(GOOGLE_SHEETS_TEST_DOCUMENT_ID)
#    #assert BaseModel.ss.document_id == GOOGLE_SHEETS_TEST_DOCUMENT_ID
#    #assert Book.ss.document_id == GOOGLE_SHEETS_TEST_DOCUMENT_ID
#
#    # setup / remove any records that may exist:
#    Book.destroy_all()
#
#    # seed default records:
#    Book.seed()
#
#    yield "Using test document!"
#
#    # clean up:
#    Book.destroy_all()



#@pytest.fixture()
#def products_context(model_context):
#
#    # setup / remove any records that may exist:
#    Product.destroy_all()
#
#    # seed default records:
#    Product.seed()
#
#    yield "Using test document!"
#
#    # clean up:
#    Product.destroy_all()



#@pytest.fixture()
#def test_client(ss):
#    app = create_app(spreadsheet_service=ss)
#    app.config.update({"TESTING": True})
#    return app.test_client()

@pytest.fixture()
def test_client(model_context):
    app = create_app()
    app.config.update({"TESTING": True})
    return app.test_client()
