class financialrecord:
    def __init__(self, RecordID=None, EmployeeID=None, RecordDate=None, Description=None, Amount=None, RecordType=None):
        self.recordID=RecordID
        self.employeeID=EmployeeID
        self.RecordDate=RecordDate
        self.description=Description
        self.Amount=Amount
        self.RecordType=RecordType

    @property
    def recordID(self):
        return self.recordID

    @recordID.setter
    def recordID(self, new_recordID):
        self.recordID = new_recordID

    @property
    def employeeID(self):
        return self.employeeID

    @employeeID.setter
    def employeeID(self, new_employeeID):
        self.employeeID = new_employeeID

    @property
    def RecordDate(self):
        return self.RecordDate

    @RecordDate.setter
    def RecordDate(self, new_RecordDate):
        self.RecordDate = new_RecordDate

    @property
    def description(self):
        return self.description

    @description.setter
    def description(self, new_description):
        self.description = new_description

    @property
    def Amount(self):
        return self.Amount

    @Amount.setter
    def Amount(self, new_Amount):
        self.Amount = new_Amount

    @property
    def RecordType(self):
        return self.RecordType

    @RecordType.setter
    def RecordType(self, new_RecordType):
        self.RecordType = new_RecordType