import time

from day_13.bus_reservation.reservation.bookings import title, reserve_seat, cancel_booking, search_booking
from day_13.bus_reservation.reservation.reports import display_passengers
from day_13.bus_reservation.reservation.seats import show_routes_and_seats


def display_menu():
    '''Display the main menu'''

    title("BUS RESERVATION SYSTEM")

    print("\n1. View Routes & Seats"
          "\n2. Reserve a seat"
          "\n3. Cancel a reservation"
          "\n4. Search booking"
          "\n5. View passenger list"
          "\n6. Exit")
    print("=" * 40)

def main():
    """Run the applicattion until Exit is selected"""

    while True:
        display_menu()

        choice = int(input("Choose an option : ").strip())

        if choice  == 1:
            show_routes_and_seats()
            time.sleep(3)
        elif choice== 2:
            reserve_seat()
            time.sleep(3)
        elif choice == 3:
            cancel_booking()
            time.sleep(3)

        elif choice == 4:
            search_booking()

        elif choice == 5:
            display_passengers()
            time.sleep(3)


        elif choice == 6:
            print("Thank you for using the BUS SEAT RESERVATION SYSTEM...")
            time.sleep(3)
            print('Application Closed.')
            break

        else:
            print("Invalid choise.Please select an option from 1 - 6")

main()