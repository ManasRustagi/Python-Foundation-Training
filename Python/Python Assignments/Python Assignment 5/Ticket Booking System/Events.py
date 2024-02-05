from datetime import datetime
from Venue import Venue


class Event(Venue):
    def __init__(self, EventName, EventDate, EventTime, Venue, TotalSeats, AvailableSeats, TicketPrice, EventType):
        self.event_name = EventName
        self.event_date = datetime.strptime(EventDate, "%Y-%m-%d").date()
        self.event_time = datetime.strptime(EventTime, "%H:%M").time()
        self.venue_name = Venue.venue_name
        self.total_seats = TotalSeats
        self.available_seats = AvailableSeats
        self.ticket_price = TicketPrice
        self.event_type = EventType

    def calculate_total_revenue(self):
        return self.ticket_price * (self.total_seats - self.available_seats)

    def getBookedNoOfTickets(self):
        return self.total_seats-self.available_seats

    def book_tickets(self, num_tickets):
        self.available_seats = self.available_seats - num_tickets

    def cancel_booking(self, num_tickets):
        self.available_seats = self.available_seats + num_tickets

    def display_event_details(self):
        print(f"Event name = {self.event_name}")
        print(f"Date of event = {self.event_date}")
        print(f"Time of event = {self.event_time}")
        print(f"Venue name = {self.venue_name}")
        print(f"Available Seats = {self.available_seats}")