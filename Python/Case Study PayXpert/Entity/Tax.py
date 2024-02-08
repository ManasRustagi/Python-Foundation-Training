class tax:
    def __init__(self,TaxID=None, EmployeeID=None, TaxYear=None, TaxableIncome=None, TaxAmount=None):
        self.TaxID=TaxID
        self.employeeId=EmployeeID
        self.taxYear=TaxYear
        self.TaxableIncome=TaxableIncome
        self.TaxAmount=TaxAmount

    @property
    def TaxID(self):
        return self.TaxID

    @TaxID.setter
    def TaxID(self, new_TaxID):
        self.TaxID = new_TaxID

    @property
    def EmployeeID(self):
        return self.EmployeeID

    @EmployeeID.setter
    def EmployeeID(self, new_EmployeeID):
        self.EmployeeID = new_EmployeeID

    @property
    def TaxYear(self):
        return self.TaxYear

    @TaxYear.setter
    def TaxYear(self, new_TaxYear):
        self.TaxYear = new_TaxYear

    @property
    def TaxableIncome(self):
        return self.TaxableIncome

    @TaxableIncome.setter
    def TaxableIncome(self, new_TaxableIncome):
        self.TaxableIncome = new_TaxableIncome

    @property
    def TaxAmount(self):
        return self.TaxAmount

    @TaxAmount.setter
    def TaxAmount(self, new_TaxAmount):
        self.TaxAmount = new_TaxAmount

