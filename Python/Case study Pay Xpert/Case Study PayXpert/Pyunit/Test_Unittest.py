import unittest

from util.DB_connection import DBConnector
from Entity.EmployeeService import employeeservice
from Entity.PayrollService import payrollservice
db_connector = DBConnector("localhost", "root", "root", 3306, "payxpert")

esl = employeeservice(db_connector)
psl = payrollservice(db_connector)



class PayrollSystemTestCase(unittest.TestCase):
    db_connector = DBConnector("localhost", "root", "root", 3306, "payxpert")
    def test_calculate_net_salary_after_deductions(self):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        query = "SELECT NetSalary, Overtime, Deductions FROM payroll"
        netCheck = []
        cur.execute(query)
        record=cur.fetchall()
        for NetSalary, Overtime, ded in record:
            netCheck.append(int(NetSalary + Overtime - ded))
        expected_net_salary = netCheck
        actual_net_salary = psl.CalculateSalary(record[0],record[1],record[2])
        self.assertEqual(actual_net_salary, expected_net_salary)