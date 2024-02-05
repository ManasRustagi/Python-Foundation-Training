

class Customer:
    def __init__(self, CustomerName, Email, Phone):
        self.CustomerName = CustomerName
        self.Email = Email
        self.Phone = Phone

    def display_customer_details(self):
        print(f"Customer Name : {self.CustomerName}")
        print(f"Email : {self.Email}")
        print(f"Phone Number : {self.Phone}")