
class Venue:
    def __init__(self, VenueName, Address):
        self.Venue_name = VenueName
        self.Address = Address

    def display_venue_details(self):
        print(f"Venue Name = {self.Venue_name}")
        print(f"Address of venue = {self.Address}")
