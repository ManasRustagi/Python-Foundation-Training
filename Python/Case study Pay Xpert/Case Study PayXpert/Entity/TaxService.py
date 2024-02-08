from Dao.ITaxService import ITaxService
from Exception.Exceptions import TaxCalculationException
from Exception.Exceptions import InvalidInputException
class taxservice(ITaxService):
    def __init__(self,db_connector):
        self.db_connector=db_connector

    def CalculateTax(self):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        cur.execute("Select TaxableIncome from tax")
        record=cur.fetchall()
        if record:
            for i in record:
                if i[0] <= 50000:
                    tax=i[0]*0.05
                    cur.execute("Update tax set TaxAmount=%s Where TaxableIncome=%s",(tax,i[0]))

                elif i[0]>50000:
                    tax = i[0] * 0.1
                    cur.execute("Update tax set TaxAmount=%s Where TaxableIncome=%s", (tax, i[0]))
        else:
            raise TaxCalculationException()

        self.db_connector.connection.commit()
        self.db_connector.close_connection()
        self.GetTaxesForEmployee()


    def GettaxbyID(self):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        taxID = input("Enter the tax ID for details : ")
        cur.execute("Select * from tax where taxid=%s", (taxID,))
        record = cur.fetchone()
        if record:
            print("Here are the details : ")
            print(f"Tax ID : {record[0]}")
            print(f"Employee Id : {record[1]}")
            print(f"Tax Year : {record[2]}")
            print(f"Taxable Income : {record[3]}")
            print(f"Tax Amount : {record[4]}")
        else:
            raise InvalidInputException
        self.db_connector.close_connection()


    def GetTaxesForEmployee(self):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        employeeID = input("Enter the employee Id for which you want tax : ")
        cur.execute("Select * from tax where EmployeeId=%s", (employeeID,))
        record = cur.fetchall()
        if record:
            print("Here are the details : ")
            for i in record:
                print(f"Tax ID : {i[0]}")
                print(f"Employee Id : {i[1]}")
                print(f"Tax Year : {i[2]}")
                print(f"Taxable Income : {i[3]}")
                print(f"Tax Amount : {i[4]}")
                print(" ")
        else:
            raise InvalidInputException
        self.db_connector.close_connection()

    def GetTaxesForYear(self):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        Year = input("Enter the Year for which you want taxes : ")
        cur.execute("Select * from tax where TaxYear =%s", (Year,))
        record = cur.fetchall()
        if record:
            print("Here are the details : ")
            for i in record:
                print("Here are the details : ")
                print(f"Tax ID : {i[0]}")
                print(f"Employee Id : {i[1]}")
                print(f"Tax Year : {i[2]}")
                print(f"Taxable Income : {i[3]}")
                print(f"Tax Amount : {i[4]}")
                print(" ")
        else:
            print("No taxes Found")
        self.db_connector.close_connection()