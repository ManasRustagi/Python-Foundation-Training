from Events import Event
import random
from datetime import date


class Booking(Event):

    def __init__(self, Event, Customer):
        self.BookingID = random.randint(10000, 99999)
        self.Customer = Event
        self.Event = Customer
        self.NumTickets = len(Customer)
        self.Total_cost = 0
        self.Booking_date = date.today()


    def calculate_booking_cost(self, num_tickets):
        pass

    def book_tickets(self, num_tickets):
        super().book_tickets(num_tickets)

    def cancel_booking(self, num_tickets):
        super().cancel_booking(num_tickets)

    def getAvailableNoOfTickets(self):
        return self.Event.available_seats

    def getEventDetails(self):
        pass
