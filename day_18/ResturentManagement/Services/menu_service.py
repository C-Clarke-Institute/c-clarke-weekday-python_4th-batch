from day_18.ResturentManagement.Repositories.MenuRepository import MenuRepository
from day_18.ResturentManagement.models.menu_item import MenuItem


class MenuService:

    def __init__(self, repository : MenuRepository):
        self.repository = repository

    def add_menu_item(self, item : MenuItem) -> None:

        # Validate item name
        if not item.name.strip():
            raise ValueError("Item Name cannot be empty")

        # validate item price
        if item.price < 0 :
            raise ValueError("Price Must be greater than Zero")

        # add item to repository
        self.repository.add(item)
