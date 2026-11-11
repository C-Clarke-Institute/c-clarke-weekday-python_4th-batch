from day_18.ResturentManagement.Repositories.MenuRepository import InMemoryMenuRepository
from day_18.ResturentManagement.Services.menu_service import MenuService
from day_18.ResturentManagement.input_handler import get_integer, get_string, get_float, get_positive_numbers
from day_18.ResturentManagement.models.menu_item import MenuItem

menu_services = MenuService(repository=InMemoryMenuRepository())


def add_menu_item():

    print("\n============= ADD MENU ITEM =============")

    #get user inputs
    item_id = get_integer("Enter Item ID : ")
    name = get_string("Enter Item Name : ")
    description = get_string('Enter Description : ')
    price = get_positive_numbers("Enter Price : ")

    #create MenuItem Object

    item = MenuItem(item_id=item_id,name=name,description=description, price=price)

    #send item to service
    try:

        menu_services.add_menu_item(item)
        print("\nMenu Item added Successfully.")

    except ValueError as error :
        print(error)



while True:

    print("\n ====== Main Menu ====== ")
    print("\n1. Add Menu Item"
          ". Exit  "
          "")
    user_input = get_integer("Select Option Number : ")

    if user_input == 1:

        add_menu_item()

    else :
        exit()




