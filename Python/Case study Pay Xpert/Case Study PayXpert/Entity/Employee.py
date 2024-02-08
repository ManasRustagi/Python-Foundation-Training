
class Employee:
    def __init__(self, employeeID=None, firstname=None, lastname=None, dateofbirth=None, gender=None, email=None,
                 phonenumber=None, address=None, position=None, joiningdate=None, terminationdate=None, db_connector=None):
        self._employeeID = employeeID
        self._Firstname = firstname
        self._Lastname = lastname
        self._DateofBirth = dateofbirth
        self._Gender = gender
        self._email = email
        self._Phonenumber = phonenumber
        self._Address = address
        self._Position = position
        self._joiningDate = joiningdate
        self._terminationDate = terminationdate
        self._db_connector = db_connector

    @property
    def employeeId(self):
        return self._employeeID

    @employeeId.setter
    def employeeId(self, new_employeeId):
        self._employeeID = new_employeeId

    @property
    def Firstname(self):
        return self._Firstname

    @Firstname.setter
    def Firstname(self, new_Firstname):
        self._Firstname = new_Firstname

    @property
    def Lastname(self):
        return self._Lastname

    @Lastname.setter
    def Lastname(self, new_Lastname):
        self._Lastname = new_Lastname

    @property
    def DateofBirth(self):
        return self._DateofBirth

    @DateofBirth.setter
    def DateofBirth(self, new_DateofBirth):
        self._DateofBirth = new_DateofBirth

    @property
    def Gender(self):
        return self._Gender

    @Gender.setter
    def Gender(self, new_Gender):
        self._Gender = new_Gender

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        self._email = new_email

    @property
    def Phonenumber(self):
        return self._Phonenumber

    @Phonenumber.setter
    def Phonenumber(self, new_Phonenumber):
        self._Phonenumber = new_Phonenumber

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, new_Address):
        self._Address = new_Address

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, new_Position):
        self._Position = new_Position

    @property
    def joiningDate(self):
        return self._joiningDate

    @joiningDate.setter
    def joiningDate(self, new_joiningDate):
        self._joiningDate = new_joiningDate

    @property
    def terminationDate(self):
        return self._terminationDate

    @terminationDate.setter
    def terminationDate(self, new_terminationDate):
        self._terminationDate = new_terminationDate




    def CalculateAge(self):
        try:
            employeeID=input("Enter your EmployeeID for which you want to know the age : ")
            self._db_connector.open_connection()
            cur = self._db_connector.connection.cursor()
            query = "Select timestampdiff(YEAR,DateOfBirth,CurDate()) from Employee where EmployeeID=%s"
            value = (employeeID,)
            cur.execute(query, value)
            record = cur.fetchone()
            if record:
                print(f"The age of Employee whose employee ID is {employeeID} = {record[0]}")
            else:
                print("NO Employee Found")
        except Exception as e:
            print("Error in Fetching age")
        finally:
            self._db_connector.connection.close()



