
class EmployeeNotFoundException(Exception):

    def __init__(self, employee_id):
        self.employee_id = employee_id
        self.message = f"Employee with ID {employee_id} not found"
        super().__init__(self.message)

class PayrollGenerationException(Exception):

    def __init__(self, message="Error in payroll generation"):
        self.message = message
        super().__init__(self.message)

class TaxCalculationException(Exception):

    def __init__(self, message="Error in tax calculation"):
        self.message = message
        super().__init__(self.message)

class FinancialRecordException(Exception):

    def __init__(self, message="Financial record management error"):
        self.message = message
        super().__init__(self.message)

class InvalidInputException(Exception):

    def __init__(self, message="Invalid input data"):
        self.message = message
        super().__init__(self.message)

class DatabaseConnectionException(Exception):

    def __init__(self, message="Database connection error"):
        self.message = message
        super().__init__(self.message)