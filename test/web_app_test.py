
from app.models.product import Product

# tests for each page
# ... update the tests if you change the page contents:


def test_home_page(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"<h1>Home</h1>" in response.data


def test_about_page(test_client):
    response = test_client.get("/about")
    assert response.status_code == 200
    assert b"<h1>About</h1>" in response.data


def test_products_page(test_client):
    # setup (seed database with some products):
    Product.destroy_all()
    Product.seed_records()
    products = Product.find_all()
    assert len(products) == 3

    assert len(Product.find_all())
    response = test_client.get("/products")
    assert response.status_code == 200
    assert b"<h1>Products</h1>" in response.data

    assert b"Textbook" in response.data
    assert b"Cup of Tea" in response.data
    assert b"Strawberries" in response.data

    Product.destroy_all()
