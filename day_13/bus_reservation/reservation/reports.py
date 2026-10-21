from day_13.bus_reservation.reservation.bookings import title, get_bookings


def display_passengers():
    """Display the current Passenger List"""

    title("PASSENGER LIST")

    current_bookings = get_bookings()

    if not  current_bookings:
        print("No Passengers have booked seats yet.")
        return

    #tablelu
    #display the table
    print(
          f"{'Reference':<15}"
    f"{'Passenger':<20}"
    f"{'Seat':<10}"
    f"{'Price':<15}")

    print("-" * 65)

    #Display each passenger
    for booking in current_bookings:

        print(
            f"{booking['reference']:<15}"
            f"{booking['passenger_name']:<20}"
            f"{booking['seat_number']:<15}"
            f"Rs. {booking['ticket_price']:<15}"
        )
    print("=" * 65)

