import os
from datetime import datetime, timezone

from gspread import Spreadsheet as Document, Worksheet
from dotenv import load_dotenv
import pytest

#from app.spreadsheet_service import SpreadsheetService

load_dotenv()

CI_ENV = (os.getenv("CI", default="false") == "true")
CI_SKIP_MESSAGE = "taking a lighter touch to testing on the CI server, to reduce API usage and prevent rate limits"


# READING DATA
#

@pytest.mark.skipif(CI_ENV, reason=CI_SKIP_MESSAGE)
def test_document(ss):
    assert isinstance(ss.doc, Document)

@pytest.mark.skipif(CI_ENV, reason=CI_SKIP_MESSAGE)
def test_sheets(ss):
    sheets = ss.sheets
    assert isinstance(sheets, list)

    for sheet in sheets:
        assert isinstance(sheet, Worksheet)


# TODO: setup test sheet

#@pytest.mark.skipif(CI_ENV, reason=CI_SKIP_MESSAGE)
#def test_get_sheet(ss):
#    sheet = ss.get_sheet("products")
#    assert isinstance(sheet, Worksheet)
#
#@pytest.mark.skipif(CI_ENV, reason=CI_SKIP_MESSAGE)
#def test_get_records(ss):
#    sheet, products = ss.get_records("products")
#    assert isinstance(sheet, Worksheet)
#    assert isinstance(products, list)
#
#@pytest.mark.skipif(CI_ENV, reason=CI_SKIP_MESSAGE)
#def test_get_products(ss):
#    products = ss.get_products()
#    assert len(products) == 3
#    assert [p["name"] for p in products] == ["Strawberries", "Cup of Tea", "Textbook"]
#    assert [p["id"] for p in products] == [1,2,3]
#
#@pytest.mark.skipif(CI_ENV, reason=CI_SKIP_MESSAGE)
#def test_get_orders(ss):
#    orders = ss.get_orders()
#    assert not any(orders)
#
#
#@pytest.mark.skipif(CI_ENV, reason=CI_SKIP_MESSAGE)
#def test_destroy_all(ss):
#    sheet, records = ss.get_records("products")
#    assert len(records) == 3
#
#    ss.destroy_all("products")
#
#    sheet, records = ss.get_records("products")
#    assert not any(records)


#
# WRITING DATA
#

#@pytest.mark.skipif(CI_ENV, reason=CI_SKIP_MESSAGE)
#def test_create_product(ss):
#
#    sheet, products = ss.get_records("products")
#    assert len(products) == 3
#
#    new_product = {"name": "Mock Product", "price": 999.99, "description": "Testing 123...", "url": "https://picsum.photos/360/200"}
#    ss.create_product(new_product)
#
#    sheet, products = ss.get_records("products")
#    assert len(products) == 4
#
#    product = products[-1]
#    assert product["id"] == 4
#    assert product["name"] == "Mock Product"
#    assert product["price"] == 999.99
#    assert product["description"] == "Testing 123..."
#    assert product["url"] == "https://picsum.photos/360/200"
#    assert isinstance(product["created_at"], datetime)
#
#
#
#@pytest.mark.skipif(CI_ENV, reason=CI_SKIP_MESSAGE)
#def test_create_order(ss):
#    sheet, orders = ss.get_records("orders")
#    assert not any(orders)
#
#    ss.create_order({
#        "user_email": "example@test.com",
#        "product_id": 3,
#        "product_name": "Test Product",
#        "product_price": 4.99
#    })
#
#    sheet, orders = ss.get_records("orders")
#    assert len(orders) == 1
#
#    order = orders[0]
#    assert order["id"] == 1
#    assert order["user_email"] == "example@test.com"
#    assert order["product_id"] == 3
#    assert order["product_name"] == "Test Product"
#    assert order["product_price"] == 4.99
#    assert isinstance(order["created_at"], datetime)
#
#
#
#
#@pytest.mark.skipif(CI_ENV, reason=CI_SKIP_MESSAGE)
#def test_get_user_orders(ss):
#    user_email = "example@test.com"
#
#    user_orders = ss.get_user_orders(user_email)
#    assert not any(user_orders)
#
#    ss.create_orders([
#        {"user_email": user_email,      "product_id": 2, "product_name": "Product 2", "product_price": 4.99},
#        {"user_email": user_email,      "product_id": 2, "product_name": "Product 2", "product_price": 4.99},
#        {"user_email": user_email,      "product_id": 2, "product_name": "Product 2", "product_price": 4.99},
#        {"user_email": "other@yep.com", "product_id": 2, "product_name": "Product 2", "product_price": 4.99},
#        {"user_email": "other@yep.com", "product_id": 1, "product_name": "Product 1", "product_price": 5.99},
#        {"user_email": "other@yep.com", "product_id": 3, "product_name": "Product 3", "product_price": 6.99},
#    ])
#
#    user_orders = ss.get_user_orders(user_email)
#    assert len(user_orders) == 3
#    assert [o["id"] for o in user_orders] == [1,2,3]
#    assert [o["user_email"] for o in user_orders] == [user_email, user_email, user_email]
#    assert [o["product_id"] for o in user_orders] == [2,2,2]
#    assert [o["product_name"] for o in user_orders] == ["Product 2", "Product 2", "Product 2"]
#    assert [o["product_price"] for o in user_orders] == [4.99,4.99,4.99]
#    assert [isinstance(o["created_at"], datetime) for o in user_orders] == [True, True, True]
#
