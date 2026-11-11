from dataclasses import dataclass, field
from typing import List

from day_18.ResturentManagement.models.order_status import OrderStatus


@dataclass
class OrderLine :

    menu_item_id : int
    item_name : str
    unit_price : float
    quantity : int

    @property
    def subtotal(self) -> float:
        return self.unit_price * self.quantity

@dataclass
class Order :

    order_id : int
    status: OrderStatus = OrderStatus.PENDING
    items: List[OrderLine] = field(default_factory=list)

    @property
    def total(self) -> float:
        return sum(line.subtotal for line in self.items)