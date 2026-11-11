from enum import Enum


class OrderStatus(Enum):

    PENDING = "Pending"
    PREPARING = "Preparing"
    READY = "Ready"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"



