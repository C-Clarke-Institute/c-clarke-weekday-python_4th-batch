from routes import route, ticket_price

def title(title):
    print("\n" + "=" * 40)
    print(title.center(40))
    print("\n" + "=" * 40)

MAX_SEAT = 20


#avaialble  seat numbers
seat_numbers = list(range(1,MAX_SEAT+1))

#store all active bookings
booking_records = []

next_reference_number = 1001

def get_bookings():
    """Return all the active bookings"""
    return booking_records

def reserve_seat():
    """Reserve an available seat for  a passenger"""

    global next_reference_number

    print("\n" + "=" * 40)
    print("RESERVE A SEAT".center(40))
    print("\n" + "=" * 40)

    passenger_name = input("Passenger Name : ".strip())

    #validate passeneger name
    if not passenger_name:
        raise ValueError("Passenger Name cannot be empty.")

    try:
        selected_seat = int(input(f"Choose seat number (1 - {MAX_SEAT}) : "))

    except ValueError:
        print("Error : Please enter a valid numeric seat number :  ")
        return

    if selected_seat not in seat_numbers:
         for booking in booking_records:

             if booking["seat_number"] == seat_numbers:
                 print("Error:this seat is a already booked")
                 return

    booking_referance = f"BUS-{next_reference_number}"

    new_booking = {
        "reference" : booking_referance,
        "passenger_name" :passenger_name,
        "seat_number" : selected_seat,
        "route" : route[:2],
        "ticket_price" : ticket_price
    }


    booking_records.append(new_booking)

    next_reference_number += 1

    print("\nReservation Success !")
    print(f"Passenger Name :  : {passenger_name}")
    print(f"Seat Number : {selected_seat:2}")

    print(f"route : {route[0]}  -> {route[1]}")
    print(f"Ticket price : LKR  ")


def search_booking():
    """Find a booking using its referance number"""

    title("SEARCH BOOKING")

    reference = input("Enter the booking reference : ").strip().upper()

    for booking in booking_records:

        if booking['reference'] == reference:

            print("\nBooking Found!...")
            print(f"Booking Reference : ".ljust(25) + booking['reference'])
            print(f"Passenger Name : ".ljust(25) + booking['passenger_name'])
            print(f"Seat Number : ".ljust(25) + booking['seat_number'])
            print(f"Route : ".ljust(25) + f"{booking['route'[0]]} -> {booking['route'[1]]}")
            print(f"Ticket Price : Rs. ".ljust(25) + booking['ticket_price'])
            return
        print("Error : No Booking found with that reference")












