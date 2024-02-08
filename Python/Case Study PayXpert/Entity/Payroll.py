class payroll:
    def __init__(self,PayrollID=None,EmployeeID=None,PayPeriodEndDate=None,BasicSalary=None,OvertimePay=None,deductions=None,Netsalary=None):
        self.PayrollID=PayrollID
        self.EmployeeID=EmployeeID
        self.PayPeriodEndDate=PayPeriodEndDate
        self.BasicSalary=BasicSalary
        self.Overtimepay=OvertimePay
        self.deductions=deductions
        self.Netsalary=Netsalary

    @property
    def PayrollID(self):
        return self.PayrollID

    @PayrollID.setter
    def PayrollID(self, new_PayrollID):
        self.PayrollID = new_PayrollID

    @property
    def EmployeeID(self):
        return self.EmployeeID

    @EmployeeID.setter
    def EmployeeID(self, new_EmployeeID):
        self.EmployeeID = new_EmployeeID

    @property
    def PayPeriodEndDate(self):
        return self.PayPeriodEndDate

    @PayPeriodEndDate.setter
    def PayPeriodEndDate(self, new_PayPeriodEndDate):
        self.PayPeriodEndDate = new_PayPeriodEndDate

    @property
    def BasicSalary(self):
        return self.BasicSalary

    @BasicSalary.setter
    def BasicSalary(self, new_BasicSalary):
        self.BasicSalary = new_BasicSalary

    @property
    def Overtimepay(self):
        return self.Overtimepay

    @Overtimepay.setter
    def Overtimepay(self, new_Overtimepay):
        self.Overtimepay = new_Overtimepay

    @property
    def deductions(self):
        return self.deductions

    @deductions.setter
    def deductions(self, new_deductions):
        self.deductions = new_deductions

    @property
    def Netsalary(self):
        return self.Netsalary

    @Netsalary.setter
    def Netsalary(self, new_Netsalary):
        self.Netsalary = new_Netsalary




