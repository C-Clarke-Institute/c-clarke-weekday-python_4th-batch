from day_13.bus_reservation.reservation.bookings import title, get_bookings, seat_numbers
from day_13.bus_reservation.reservation.routes import display_route


def display_seats():
    """Show all the seats and their availability"""

    title("SEAT_AVAILABILITY")

    current_bookings = get_bookings()

    #Collect the booked seat numbers
    booked_seats = []

    for booking in current_bookings:
        booked_seats.append(booking['seat_number'])

    #Display seats

    for seat_number in seat_numbers:

        if seat_number in booked_seats:
            seat_status = "[X]"

        else:
            seat_status = "[ ]"

        print(f"{seat_number:02} {seat_status}", end=" ")

        if seat_number % 4 == 0:
            print()

    print("\n[X] - Booked     [ ] - Available")

def show_routes_and_seats():
    """Display route information and the seat map"""

    display_route()
    display_seats()




