from Dao.IEmployeeService import IEmployeeService
from Exception.Exceptions import EmployeeNotFoundException
class employeeservice(IEmployeeService):
    def __init__(self,db_connector):
        self.db_connector=db_connector

    def GetEmployeeById(self):
        self.db_connector.open_connection()
        cur=self.db_connector.connection.cursor()
        employeeId=input("Please enter your employeeID : ")
        cur.execute("Select * from Employee Where employeeID =%s",(employeeId,))
        record=cur.fetchone()
        if record:
            print("Here are the details of th employee : ")
            print(f"Employee ID = {record[0]}")
            print(f"First name = {record[1]}")
            print(f"Last Name = {record[2]}")
            print(f"Date Of Birth = {record[3]}")
            print(f"Gender = {record[4]}")
            print(f"Email = {record[5]}")
            print(f"Phone Number = {record[6]}")
            print(f"Address = {record[7]}")
            print(f"Position = {record[8]}")
            print(f"Joining Date = {record[9]}")
            print(f"Termination Date = {record[10]}")

        else:
            raise EmployeeNotFoundException(employeeId)
        self.db_connector.close_connection()


    def GetAllEmployees(self):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        cur.execute("Select FirstName from Employee")
        record=cur.fetchall()
        if record:
            for i in record:
                print(i[0])
        else:
            print("No employee work here")
        self.db_connector.close_connection()


    def AddEmployee(self):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        print("Enter the details of employee you want to add")
        employeeID=self.GetuniqueEmployeeID()
        FirstName=input("Enter Frist Name : ")
        LastName=input("Enter Last Name : ")
        DateofBirth=input("Enter Date of birth in the format 'YYYY-MM-DD' : ")
        Gender=input("Enter Gender (Male,Female) : ")
        Email=input("Enter the email address : ")
        PhoneNumber=input("Enter Phone Number : ")
        Address=input("Enter Address : ")
        Positon=input("Enter Position : ")
        Joiningdate=input("Enter Joining Date in the format 'YYYY-MM-DD' :")
        query = "Insert into Employee (EmployeeId, Firstname, Lastname, Dateofbirth, Gender, Email, Phonenumber, Address, Position, Joiningdate) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values=(employeeID,FirstName,LastName,DateofBirth,Gender,Email,PhoneNumber,Address,Positon,Joiningdate,)
        cur.execute(query,values)
        print("Employee Added Successfully")
        self.db_connector.connection.commit()
        self.db_connector.close_connection()

    def UpdateEmployee(self):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        employeeId = input("Enter the employeeID you want to update : ")
        print("Choose what you want to update : ")
        print("1.First name ")
        print("2.Last Name ")
        print("3.Date Of Birth ")
        print("4.Gender ")
        print("5.Email ")
        print("6.Phone Number ")
        print("7.Address ")
        print("8.Position ")
        print("9.Joining Date ")
        print("10.Termination Date ")
        choice = int(input("Enter your choice : "))
        cur.execute("Select * from Employee Where employeeID =%s", (employeeId,))
        record = cur.fetchone()
        if record:
            FirstName = record[1]
            LastName = record[2]
            DateOfBirth = record[3]
            Gender = record[4]
            Email = record[5]
            PhoneNumber = record[6]
            Address = record[7]
            Position = record[8]
            JoiningDate = record[9]
            TerminationDate = record[10]

            if choice == 1:
                FirstName = input("Enter Frist Name : ")
            elif choice == 2:
                LastName = input("Enter Last Name : ")
            elif choice == 3:
                DateOfBirth = input("Enter Date of birth in the format 'YYYY-MM-DD' : ")
            elif choice == 4:
                Gender = input("Enter Gender (Male,Female) : ")
            elif choice == 5:
                Email = input("Enter the email address : ")
            elif choice == 6:
                PhoneNumber = input("Enter Phone Number : ")
            elif choice == 7:
                Address = input("Enter Address : ")
            elif choice == 8:
                Position = input("Enter Position : ")
            elif choice == 9:
                JoiningDate = input("Enter Joining Date in the format 'YYYY-MM-DD' :")
            elif choice == 10:
                TerminationDate = input("Enter Termination Date in the format 'YYYY-MM-DD' : ")
            else:
                print("Enter correct choice !!! ")
            query = "Update employee set Firstname=%s,Lastname=%s,Dateofbirth=%s, Gender=%s, Email=%s, Phonenumber=%s, Address=%s, position=%s, joiningdate=%s, TerminationDate=%s Where EmployeeId=%s"
            values = (FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate,
                      TerminationDate, employeeId,)
            cur.execute(query, values)
            print("Updated Successfully")
            self.db_connector.connection.commit()
        else:
            raise EmployeeNotFoundException(employeeId)
        self.db_connector.close_connection()

    def RemoveEmployee(self):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        emploeeID=input("Enter the employee id of the employee you want to remove : ")
        cur.execute("Delete from employee Where employeeId=%s",(emploeeID,))
        print("Employee successfully removed")
        self.db_connector.connection.commit()
        self.db_connector.close_connection()



    def GetuniqueEmployeeID(self):
        return len(self.get_allemployee())+1

    def get_allemployee(self):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        cur.execute("select FirstName from employee")
        record=cur.fetchall()
        return record
