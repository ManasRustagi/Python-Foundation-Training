from abc import ABC, abstractmethod

class IPayrollService(ABC):
    @abstractmethod
    def GeneratePayroll(self):
        pass

    @abstractmethod
    def GetPayrollById(self):
        pass

    @abstractmethod
    def GetPayrollsForEmployee(self):
        pass

    @abstractmethod
    def GetPayrollsForPeriod(self):
        pass

    @abstractmethod
    def getuniquepayrollid(self):
        pass