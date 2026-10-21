route = ("Kurunegala", "Colombo", "08.00 AM")
ticket_price = 1500.0

def display_route(start,end,time, ticket_price):
    """display route, departure time, and ticket price"""

    print("\n" + "=" * 40)
    print('Bus Route Details'.center(40))
    print("\n" + "=" * 40)

    print(f"Starting Location :{start}")
    print(f"Destination : {end}")
    print(f"Depature Time : {time}")
    print(f"Ticket Prrice : Rs. {ticket_price}")
    print("\n" + "=" * 40)




