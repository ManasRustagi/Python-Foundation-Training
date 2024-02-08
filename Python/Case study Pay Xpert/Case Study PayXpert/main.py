from Entity.Employee import Employee
from util.DB_connection import DBConnector
from Entity.EmployeeService import employeeservice
from Entity.PayrollService import payrollservice
from Entity.TaxService import taxservice
from Entity.FinancialRecordService import FinancialRecordService

class Payxpert:
    def main(self):
        db_connector = DBConnector("localhost", "root", "root", 3306, "payxpert")
        Emp = Employee(db_connector=db_connector)
        ES = employeeservice(db_connector)
        PS = payrollservice(db_connector)
        TS = taxservice(db_connector)
        FS = FinancialRecordService(db_connector)

        while True:
            print("Hi folks !! This is Pay Xpert")
            print("Choose from the following Options : ")
            print("1. If you need help with the employee database ")
            print("2. If you need help with the Payroll database ")
            print("3. If you need help with the Tax database ")
            print("4. If you need help with the Financial Record database ")
            print("5. Exit")
            choice = input("Now Enter Your Choice : ")
            if choice == '1':
                print("Employee Database Loading...")
                print("Now, Choose from the following options ")
                print("1. If you want to know the age of employee")
                print("2. If you want employee Details")
                print("3. All the Employees working here")
                print("4. If you want to Add a new Employee")
                print("5. If you want to update database")
                print("6. If you want to delete the employee details from the database")
                print("7. Exit")
                emp = input("Enter the choice : ")
                if emp == '1':
                    Emp.CalculateAge()
                elif emp == '2':
                    ES.GetEmployeeById()
                elif emp == '3':
                    ES.GetAllEmployees()
                elif emp == '4':
                    ES.AddEmployee()
                elif emp == '5':
                    ES.UpdateEmployee()
                elif emp == '6':
                    ES.RemoveEmployee()
                elif emp == '7':
                    self.main()
                else:
                    print("Invalid Choice")
            elif choice == '2':
                print("Payroll Databasse Loading ...")
                print("Now, Choose from the following options : ")
                print("1. If you want to generate payroll")
                print("2. IF you want to Payroll Details")
                print("3. If you want to know all Payrolls for an employee")
                print("4. If you want all payrolls for a specific period")
                print("5. Exit")
                pay = input("Enter your choice : ")
                if pay == '1':
                    PS.GeneratePayroll()
                elif pay == '2':
                    PS.GetPayrollById()
                elif pay == '3':
                    PS.GetPayrollsForEmployee()
                elif pay == '4':
                    PS.GetPayrollsForPeriod()
                elif pay == '5':
                    self.main()
                else:
                    print("Invalid Choice")
            elif choice == '3':
                print("Tax Database Loading...")
                print("Now, Choose from the following options ")
                print("1. If you want to Calculate Tax")
                print("2. If you want to Know tax details")
                print("3. If you want to know all Taxes for an employee")
                print("4. If you want to know all taxes in a year ")
                print("5. Exit")
                tax = input("Enter your Choice : ")
                if tax == '1':
                    TS.CalculateTax()
                elif tax == '2':
                    TS.GettaxbyID()
                elif tax == '3':
                    TS.GetTaxesForEmployee()
                elif tax == '4':
                    TS.GetTaxesForYear()
                elif tax == '5':
                    self.main()
                else:
                    print("Invalid Choice")
            elif choice == '4':
                print("Financial Record Loading...")
                print("Now, Choose from the following options ")
                print("1. IF you want to add a financial record")
                print("2. If you want to Financial Record details")
                print("3. If you want to know all finacial records for an employee")
                print("4. If you want to know all Financial Records for a specific date")
                print("5. Exit")
                fin = input("Enter Your Choice : ")
                if fin == '1':
                    FS.AddFinancialRecord()
                elif fin == '2':
                    FS.GetFinancialRecordById()
                elif fin == '3':
                    FS.GetFinancialRecordsForEmployee()
                elif fin == '4':
                    FS.GetFinancialRecordsForDate()
                elif fin == '5':
                    self.main()
                else:
                    print("Invalid Choice")
            elif choice=='5':
                exit()
            else:
                print("Invalid Choice")



if __name__=='__main__':
    obj=Payxpert()
    obj.main()