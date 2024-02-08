from abc import ABC, abstractmethod

class IEmployeeService(ABC):
    @abstractmethod
    def GetEmployeeById(self):
        pass

    @abstractmethod
    def GetAllEmployees(self):
        pass

    @abstractmethod
    def AddEmployee(self):
        pass

    @abstractmethod
    def UpdateEmployee(self):
        pass

    @abstractmethod
    def RemoveEmployee(self):
        pass