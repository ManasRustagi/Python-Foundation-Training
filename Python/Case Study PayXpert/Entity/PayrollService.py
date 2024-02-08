from Dao.IPayrollService import IPayrollService
from Exception.Exceptions import PayrollGenerationException
class payrollservice(IPayrollService):
    def __init__(self,db_connector):
        self.db_connector= db_connector


    def GeneratePayroll(self):
        self.db_connector.open_connection()
        cur=self.db_connector.connection.cursor()
        employeeId=input("Enter the employeeID for which you want to generate payroll : ")
        payrollid=self.getuniquepayrollid()
        basesalary=int(input("Enter the base salary of the employee : "))
        Payperiodstartingdate=input("Enter the pay period starting date in the format 'YYYY-MM-DD' : ")
        Payperiodendingdate = input("Enter the pay period ending date in the format 'YYYY-MM-DD' : ")
        OvertimePay=int(input("Enter the overtime pay of the employee : "))
        Deductions=int(input("Enter the deduction for the employee : "))
        NetSalary=self.CalculateSalary(basesalary,OvertimePay,Deductions)
        query="Insert into payroll values(%s,%s,%s,%s,%s,%s,%s,%s)"
        values=(payrollid,employeeId,Payperiodstartingdate,Payperiodendingdate,basesalary,OvertimePay,Deductions,NetSalary,)
        cur.execute(query,values)
        self.db_connector.connection.commit()
        print("Payroll Generated !!!  ")
        self.db_connector.close_connection()


    def GetPayrollById(self):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        payrollID=input("Enter the payrollId for details : ")
        cur.execute("Select * from payroll where PayrollId=%s",(payrollID,))
        record=cur.fetchone()
        if record:
            print("Here are the details : ")
            print(f"Payroll If : {record[0]}")
            print(f"Employee Id : {record[1]}")
            print(f"Pay period starting date : {record[2]}")
            print(f"Pay period ending date : {record[3]}")
            print(f"Base Salary : {record[4]}")
            print(f"Overt time pay : {record[5]}")
            print(f"deductions : {record[6]}")
            print(f"Net salary : {record[7]}")
        else:
            raise PayrollGenerationException()
        self.db_connector.close_connection()


    def GetPayrollsForEmployee(self):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        employeeID=input("Enter the employee Id for which you want Payrolls : ")
        cur.execute("Select * from payroll where EmployeeId=%s", (employeeID,))
        record = cur.fetchall()
        if record:
            print("Here are the details : ")
            for i in record:
                print(f"Payroll Id : {i[0]}")
                print(f"Employee Id : {i[1]}")
                print(f"Pay period starting date : {i[2]}")
                print(f"Pay period ending date : {i[3]}")
                print(f"Base Salary : {i[4]}")
                print(f"Overt time pay : {i[5]}")
                print(f"deductions : {i[6]}")
                print(f"Net salary : {i[7]}")
                print(" ")
        else:
            raise PayrollGenerationException()
        self.db_connector.close_connection()

    def GetPayrollsForPeriod(self):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        startingdate=input("Enter the Starting date in the format 'YYYY-MM-DD' : ")
        endingdate=input("Enter the ending date in the format 'YYYY-MM-DD' : ")
        query="select * from payroll where Payperiodstartingdate >= %s and Payperiodendingdate <= %s"
        values=(startingdate,endingdate,)
        cur.execute(query,values)
        record=cur.fetchall()
        if record:
            print("Here are the payroll for the given period : ")
            for i in record:
                print(f"Payroll Id : {i[0]}")
                print(f"Employee Id : {i[1]}")
                print(f"Pay period starting date : {i[2]}")
                print(f"Pay period ending date : {i[3]}")
                print(f"Base Salary : {i[4]}")
                print(f"Overt time pay : {i[5]}")
                print(f"deductions : {i[6]}")
                print(f"Net salary : {i[7]}")
                print(" ")
        else:
            raise PayrollGenerationException()
        self.db_connector.close_connection()


    def getuniquepayrollid(self):
        return len(self.geallpayroll())+1

    def geallpayroll(self):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        cur.execute("select * from payroll")
        record=cur.fetchall()
        return record

    def CalculateSalary(self,basepay,Overtimepay,deductions):
        NetSalary=basepay+Overtimepay-deductions
        return NetSalary

