from dataclasses import dataclass

from day_18.supermarket.models import Product, SuperMarketError, Customer, OrderItem, Order
from day_18.supermarket.repositories import InMemoryProductRepository, InMemoryOrderRepository, \
    InMemoryCustomerRepository, ProductRepository, OrderRepository, CustomerRepository

@dataclass
class SuperMarketService:

    # def __init__(self, product_repository: ProductRepository,
    #              order_repository: OrderRepository,
    #              customer_repository: CustomerRepository):
    #
    #     self.product_repository = product_repository
    #     self.customer_repository = customer_repository
    #     self.order_repository = order_repository

    product_repository: ProductRepository
    customer_repository: CustomerRepository
    order_repository: OrderRepository

    def add_product(self, prod_id: str, name: str, price: float, quantity: int) -> Product:

        if self.product_repository.get_by_id(product_id=prod_id) is not None:
            raise SuperMarketError("Product already exists")

        if quantity < 0:
            raise SuperMarketError("Quantity cannot be less than zero")

        if price < 0:
            raise SuperMarketError("Price cannot be less than zero")

        product = Product(product_id=prod_id, name=name, price=price, quantity=quantity)
        self.product_repository.add_product(product)

        return product

    def add_customer(self, customer_id: str, name: str, email: str, phone_no: str) -> Customer:
        if self.customer_repository.get_by_id(customer_id) is not None:
            raise SuperMarketError("Customer Already exists")
        if self.customer_repository.find_by_email(email) is not None:
            raise SuperMarketError("Customer already exists with this email")
        customer = Customer(customer_id=customer_id, name=name, email=email, contact_no=phone_no)
        self.customer_repository.add_customer(customer)
        return customer

    def add_item_to_order(self, order_id, product_id, quantity):

        order = self.order_repository.get_by_id(order_id)
        product = self.product_repository.get_by_id(product_id)

        if order is None:
            raise SuperMarketError ("Order doesn't exists. ")

        if product is None:
            raise SuperMarketError("Product doesn't exists. ")

        if product.quantity < quantity:
            raise SuperMarketError(f'Not enough {product.name} left')

        order_item = OrderItem(product_id,product.name,quantity,product.price)
        order.add_item(order_item)

        product.reduce_quantity(quantity)
        self.product_repository.update_product(product)
        self.order_repository.update_order(order)

        return order_item

    def add_order(self, order_id, cust_id):

        if self.order_repository.get_by_id(order_id) is not None:
            raise SuperMarketError("Order already Exists.")

        customer = self.customer_repository.get_by_id(cust_id)

        if customer is None:
            raise SuperMarketError("Customer Doesn't exists. ")

        order = Order(order_id,customer.customer_id,customer.name)

        self.order_repository.add_order(order)
        return order


