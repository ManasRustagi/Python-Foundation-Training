import unittest
from unittest.mock import MagicMock
from Entity.PayrollService import payrollservice
from Entity.TaxService import taxservice
from util.DB_connection import DBConnector

class PayrollServiceTestCase(unittest.TestCase):

    def setUp(self):
        # Create a mock for the database connector
        self.db_connector = DBConnector("localhost", "root", "root", 3306, "payxpert")

        # Create an instance of the PayrollService with the mock database connector
        self.payroll_service = payrollservice(self.db_connector)
        self.tax_service = taxservice(self.db_connector)

    def test_CalculateNetSalaryAfterDeductions(self):
        base_salary = 50000
        overtime_pay = 2000
        deductions = 5000

        net_salary = self.payroll_service.CalculateSalary(base_salary, overtime_pay, deductions)

        # Assert that the net salary is calculated correctly
        expected_net_salary = base_salary + overtime_pay - deductions
        self.assertEqual(net_salary, expected_net_salary)

    def test_CalculateGrossSalaryForEmployee(self):
        base_salary = 60000
        overtime_pay = 2500

        gross_salary = self.payroll_service.CalculateGrossSalaryForEmployee(base_salary, overtime_pay)

        # Assert that the gross salary is calculated correctly
        expected_gross_salary = base_salary + overtime_pay
        self.assertEqual(gross_salary, expected_gross_salary)

    def test_VerifyTaxCalculationForHighIncomeEmployee(self):
        taxableIncome = 100000

        tax_amount = self.tax_service.Calculate(taxableIncome)

        # Assert that the tax amount is calculated correctly
        expected_tax_amount = 0.1 * (taxableIncome)
        self.assertEqual(tax_amount, expected_tax_amount)

    def test_end_to_end_payroll_processing(self):
        payroll_data = [
            {"EmployeeID": 5, "PayPeriodStartingdate": "2024-01-01", "PayPeriodEndingdate": "2024-01-15",
             "BasicSalary": 5000, "OvertimePay": 200, "Deductions": 300},
            {"EmployeeID": 6, "PayPeriodStartingdate": "2024-01-01", "PayPeriodEndingdate": "2024-01-15",
             "BasicSalary": 6000, "OvertimePay": 250, "Deductions": 400},
        ]

        for payrolldata in payroll_data:
            processed_payroll = self.payroll_service.Generate(payrolldata)

        self.assertTrue(processed_payroll, "Not all payrolls were generated successfully")

if __name__ == '__main__':
    unittest.main()


