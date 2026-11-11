from dataclasses import dataclass, field
from datetime import datetime
from typing import List


class SuperMarketError(Exception):
    pass

@dataclass
class Product:

    product_id: str
    name: str
    price: float
    quantity: int

    def is_available(self) -> bool:
        return self.quantity > 0
    def reduce_quantity(self, amount) -> None:
        if amount > self.quantity:
            raise SuperMarketError(f"amount is greater than available qty - {self.quantity}")
        self.quantity -= amount
    def add_quantity(self, amount):
        if amount < 0 :
            raise SuperMarketError("Value cannot be less than zero")
        self.quantity += amount

@dataclass
class Customer:
    customer_id: str
    name: str
    email: str
    contact_no: str

@dataclass
class OrderItem:
    product_id: str
    product_name: str
    quantity: int
    unit_price: float

    def total_price(self) -> float:
        return self.quantity * self.unit_price

@dataclass
class Order:
    order_id: str
    customer_id: str
    customer_name: str
    created_at: datetime = field(default=datetime.now)
    items: List[OrderItem] = field(default_factory=list)

    def add_item(self, item: OrderItem) -> None:
        self.items.append(item)

    def cal_total(self):
        total = 0

        for item in self.items:
            total += item.total_price()

        return total

    def item_count(self):
        return len(self.items)
