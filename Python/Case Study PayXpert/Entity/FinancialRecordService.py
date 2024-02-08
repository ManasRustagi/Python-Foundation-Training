from Dao.IFinancialRecordService import IFinancialRecordService
from Exception.Exceptions import FinancialRecordException
class FinancialRecordService(IFinancialRecordService):
    def __init__(self,db_connector):
        self.db_connector=db_connector


    def AddFinancialRecord(self):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        recordID=self.GetuniquerecordID()
        employeeId=input("Enter the Employee Id : ")
        RecordDate=input("Enter the record date in the format 'YYYY-MM-DD' : ")
        description=input("Enter the description : ")
        amount=input("Enter the amount : ")
        recordType=input("Enter the Record type from three options ('Income','Expense','Tax Payment') : ")
        query="Insert into financialrecord values(%s,%s,%s,%s,%s,%s)"
        values=(recordID,employeeId,RecordDate,description,amount,recordType,)
        cur.execute(query,values)
        print("Successfully Added")
        self.db_connector.connection.commit()
        self.db_connector.close_connection()

    def GetFinancialRecordById(self):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        recordId=input("Enter the record Id : ")
        cur.execute("Select * from financialrecord where recordid=%s",(recordId,))
        record=cur.fetchone()
        if record:
            print("Here are the details : ")
            print(f"Record ID : {record[0]}")
            print(f"employee ID : {record[1]}")
            print(f"Record Date : {record[2]}")
            print(f"description : {record[3]}")
            print(f"Amount : {record[4]}")
            print(f"Record Type : {record[5]}")
        else:
            raise FinancialRecordException
        self.db_connector.close_connection()

    def GetFinancialRecordsForEmployee(self):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        employeeID = input("Enter the employee Id for which you want record : ")
        cur.execute("Select * from financialrecord where EmployeeId=%s", (employeeID,))
        record = cur.fetchall()
        if record:
            print("Here are the details : ")
            for i in record:
                print(f"Record ID : {i[0]}")
                print(f"Employee Id : {i[1]}")
                print(f"Record Date : {i[2]}")
                print(f"Description : {i[3]}")
                print(f"Amount : {i[4]}")
                print(f"Record Type : {i[5]}")
                print(" ")
        else:
            raise FinancialRecordException
        self.db_connector.close_connection()

    def GetFinancialRecordsForDate(self):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        recorddate = input("Enter the record date in the format 'YYYY-MM-DD' : ")
        cur.execute("Select * from financialrecord where recorddate=%s", (recorddate,))
        record = cur.fetchall()
        if record:
            print("Here are the details : ")
            for i in record:
                print(f"Record ID : {i[0]}")
                print(f"Employee Id : {i[1]}")
                print(f"Record Date : {i[2]}")
                print(f"Description : {i[3]}")
                print(f"Amount : {i[4]}")
                print(f"Record Type : {i[5]}")
                print(" ")
        else:
            raise FinancialRecordException
        self.db_connector.close_connection()

    def GetuniquerecordID(self):
        return len(self.get_allrecord())+1

    def get_allrecord(self):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        cur.execute("select recordId from financialrecord")
        record=cur.fetchall()
        return record
