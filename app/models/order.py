

from app.models.base import BaseModel
from pprint import pprint


class Order(BaseModel):

    SHEET_NAME = "orders"

    COLUMNS = ["user_email", "product_id", "product_name", "product_price"]

    SEEDS = []


if __name__ == "__main__":

    orders = Order.find_all()

    if any(orders):
        for order in orders:
            pprint(dict(order))
