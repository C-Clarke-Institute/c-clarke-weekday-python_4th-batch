from abc import ABC, abstractmethod
from typing import List, Optional, Dict

from day_18.supermarket.models import Product, Customer, Order, SuperMarketError


class ProductRepository(ABC) :

    @abstractmethod
    def add_product(self, product : Product) -> None:
        pass

    @abstractmethod
    def get_by_id(self, product_id : str) -> Optional[Product]:
        pass

    @abstractmethod
    def update_product(self, product: Product) -> None:
        pass

    @abstractmethod
    def list_all_products(self) -> List[Product]:
        pass

class CustomerRepository(ABC):
    @abstractmethod
    def add_customer(self, customer : Customer) -> None:
        pass

    @abstractmethod
    def get_by_id(self, customer_id : str) -> Optional[Customer]:
        pass

    @abstractmethod
    def update_customer(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def list_all_customers(self) -> List[Customer]:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[Customer]:
        pass

class OrderRepository(ABC):
    @abstractmethod
    def add_order(self, order : Order) -> None:
        pass

    @abstractmethod
    def get_by_id(self, order_id : str) -> Optional[Order]:
        pass

    @abstractmethod
    def update_order(self, order: Order) -> None:
        pass

    @abstractmethod
    def list_all_orders(self) -> List[Order]:
        pass

class InMemoryProductRepository(ProductRepository):

    def __init__(self):
        self.__products : Dict[str, Product] = {} # {"001" : product_object}

    def add_product(self, product: Product) -> None:
        self.__products[product.product_id] = product

    def get_by_id(self, product_id: str) -> Optional[Product]:
        return self.__products.get(product_id)

    def update_product(self, product: Product) -> None:
        if self.__products.get(product.product_id) is None:
            raise SuperMarketError("Product does not exists")
        self.__products[product.product_id] = product

    def list_all_products(self) -> List[Product]:
        return list(self.__products.values())


class InMemoryCustomerRepository(CustomerRepository):

    def find_by_email(self, email: str) -> Optional[Customer]:
        for customer in self.__customers.values():
            if customer.email == email:
                return customer
        return None

    def __init__(self):
        self.__customers: Dict[str, Customer] = {}
    def add_customer(self, customer: Customer) -> None:
        self.__customers[customer.customer_id] = customer

    def update_customer(self, customer: Customer) -> None:
        if self.__customers.get(customer.customer_id) is None:
            raise SuperMarketError("Customer Not found")
        self.__customers[customer.customer_id] = customer

    def get_by_id(self, customer_id: str) -> Optional[Customer]:
        return self.__customers.get(customer_id)

    def list_all_customers(self) -> List[Customer]:
        return list(self.__customers.values())

class InMemoryOrderRepository(OrderRepository):

    def __init__(self):
        self.__orders: Dict[str,Order] = {}

    def add_order(self, order: Order) -> None:
        self.__orders[order.order_id] = order

    def get_by_id(self, order_id: str) -> Optional[Order]:
        return self.__orders.get(order_id)

    def list_all_orders(self) -> List[Order]:
        return list(self.__orders.values())

    def update_order(self, order: Order) -> None:
        self.__orders[order.order_id] = order

class FileBasedProductRepository(ProductRepository):

    def __init__(self, filename: str = "product.txt"):
        self.filename = filename
        self.products: Dict[str, Product] = {}
        self.load()

    def load(self):
        try:
            with open("product.txt", "r") as file:
                for line in file:
                    line_splitted = line.strip().split(",")
                    product = Product(line_splitted[0]
                                      ,line_splitted[1],
                                      float(line_splitted[2]),
                                      int(line_splitted[3]))
                    self.products[product.product_id] = product
        except FileNotFoundError as e:
            print(e)

    def save(self):
        with open("product.txt", "w") as f:
            for product in self.products.values():
                f.write(f"{product.product_id},{product.name},{product.price},{product.quantity}\n")


    def add_product(self, product: Product) -> None:
        self.__products[product.product_id] = product
        self.save()

    def get_by_id(self, product_id: str) -> Optional[Product]:
        return self.__products.get(product_id)

    def update_product(self, product: Product) -> None:
        if self.__products.get(product.product_id) is None:
            raise SuperMarketError("Product does not exists")
        self.__products[product.product_id] = product
        self.save()

    def list_all_products(self) -> List[Product]:
        return list(self.__products.values())


# if __name__ == '__main__':
#     in_memory_prod_repo = InMemoryProductRepository()
#     prod1 = Product(product_id="001"
#                     , name="Anchor"
#                     , price=1000.00
#                     ,quantity=10)
#     in_memory_prod_repo.add_product(prod1)
#
#     print(in_memory_prod_repo.list_all_products())
