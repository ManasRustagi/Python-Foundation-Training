from abc import ABC, abstractmethod

class ITaxService(ABC):
    @abstractmethod
    def CalculateTax(self):
        pass

    @abstractmethod
    def GettaxbyID(self):
        pass

    @abstractmethod
    def GetTaxesForEmployee(self):
        pass

    @abstractmethod
    def GetTaxesForYear(self):
        pass


