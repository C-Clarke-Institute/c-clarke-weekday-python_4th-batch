route = ("Kurunegala", "Colombo", "08.00 AM")
ticket_price = 1500.0


def display_route():
    """display route, departure time, and ticket price"""

    print("\n" + "=" * 40)
    print('Bus Route Details'.center(40))
    print("\n" + "=" * 40)

    print(f"Starting Location :{route[0]}")
    print(f"Destination : {route[1]}")
    print(f"Depature Time : {route[2]}")
    print(f"Ticket Price : Rs. {ticket_price}")
    print("\n" + "=" * 40)

# def display_route(start,end,time, ticket_price):
#     """display route, departure time, and ticket price"""
#
#     print("\n" + "=" * 40)
#     print('Bus Route Details'.center(40))
#     print("\n" + "=" * 40)
#
#     print(f"Starting Location :{start}")
#     print(f"Destination : {end}")
#     print(f"Depature Time : {time}")
#     print(f"Ticket Prrice : Rs. {ticket_price}")
#     print("\n" + "=" * 40)




