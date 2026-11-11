from abc import ABC, abstractmethod

from day_18.ResturentManagement.models.menu_item import MenuItem


class MenuRepository(ABC):

    @abstractmethod
    def add(self, item : MenuItem):
        pass




class InMemoryMenuRepository(MenuRepository):


    def __init__(self):
        self.items = {}

    def add(self, item: MenuItem) -> None :

        if item.item_id in self.items:
            raise ValueError("Menu Item ID already exists.")

        self.items[item.item_id] = item



