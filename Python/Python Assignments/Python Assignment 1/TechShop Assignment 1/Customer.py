from Exception_Handling import InvalidDataException
class Customer:
    def __init__(self, customer_id : int, firstname : str, lastname : str, email : str, phone : str, address :str, db_connector ):
       self._CustomerID = customer_id
       self._FirstName = firstname
       self._LastName = lastname
       self._Email = email
       self._Phone = phone
       self._Address = address
       self.db_connector=db_connector



    @property
    def CustomerID(self):
        return self._CustomerID
    @CustomerID.setter
    def CustomerID(self,new_customerID):
        self._CustomerID=new_customerID

    @property
    def FirstName(self):
        return self._FirstName
    @FirstName.setter
    def FirstName(self,new_firstname):
        self._FirstName=new_firstname


    @property
    def LastName(self):
        return self._LastName
    @LastName.setter
    def LastName(self,new_lastname):
        self._LastName=new_lastname


    @property
    def Email(self):
        return self._Email
    @Email.setter
    def Email(self,new_email):
        if '@' in new_email and '.com' in new_email:
            self._Email=new_email
        else:
            raise InvalidDataException("Invalid Email Format")

    @property
    def Phone(self):
        return self._Phone
    @Phone.setter
    def Phone(self,new_phone):
        if len(new_phone) == 10 and new_phone.isdigit():
            self._Phone=new_phone
        else:
            raise InvalidDataException("Invalid Phone Number Format")


    @property
    def Address(self):
        return self._Address
    @Address.setter
    def Address(self,new_address):
        self._Address=new_address


    def create(self,CustomerID,firstname,lastname,email,phone,address):
        try:
            self.db_connector.open_connection()
            cursor=self.db_connector.connection.cursor()

            cursor.execute("Select * from Customers Where email = %s",(email,))
            existing_customer = cursor.fetchone()

            if existing_customer:
                print("This is already in use")
            else:
                cursor.execute("Insert into Customers(CustomerID,firstname,lastname,email,phone,address) Values (%s,%s,%s,%s,%s,%s)",(CustomerID,firstname,lastname,email,phone,address))
                self.db_connector.connection.commit()
                print("Customer created Successfully")
        except Exception as e:
            print("Error",e)
        finally:
            self.db_connector.close_connection()

    def CalcualteTotalOrders(self,CustomerID):
        try:
            self.db_connector.open_connection()
            cur=self.db_connector.connection.cursor()
            query="Select Count(OrderID) From Orders Where CustomerID=%s Group by CustomerID"
            values=(CustomerID,)
            cur.execute(query,values)
            record=cur.fetchone()
            if record:
                print(f"Total Order Done by the customer = {record[0]}")
            else:
                print("This customer didn't place any order")
        except Exception as e:
            print("Customer Id not Found")
        finally:
            self.db_connector.close_connection()


    def GetCustomerDetails(self,CustomerID):
        try:
            self.db_connector.open_connection()
            cur=self.db_connector.connection.cursor()
            query="Select * from Customers Where CustomerID = %s"
            values=(CustomerID,)
            cur.execute(query,values)
            customer_detail=cur.fetchone()
            if customer_detail:
                print(f"CustomerID : {customer_detail[0]}")
                print(f"First Name : {customer_detail[1]}")
                print(f"Last Name : {customer_detail[2]}")
                print(f"Email : {customer_detail[3]}")
                print(f"Phone Number : {customer_detail[4]}")
                print(f"Address : {customer_detail[5]}")
            else:
                print("NO Customer Exists")

        except Exception as e:
            print("Please Enter Correct customer id")
        finally:
            self.db_connector.close_connection()

    #def GetCustomerDetails(self):



    def UpdateCustomerInfo(self,Phone,Email,Address,CustomerID):
        try:
            self.db_connector.open_connection()
            cur=self.db_connector.connection.cursor()
            query="Update Customers Set Phone = %s, Email= %s, Address= %s Where CustomerID= %s"
            values=(Phone, Email, Address, CustomerID)
            cur.execute(query,values)
            self.db_connector.connection.commit()
            print("Updation request Succesfully Submitted")
        except Exception as e:
            print("Error Updating Request")
        finally:
            self.db_connector.close_connection()
