from day_15.transport.passenger import Passenger


class Ticket:

    def __init__(self, ticket_no: str, price: float,route: str, passenger: Passenger):
        self.__ticket_no = ticket_no
        self.__price = price
        self.__passenger = passenger
        self.__route = route