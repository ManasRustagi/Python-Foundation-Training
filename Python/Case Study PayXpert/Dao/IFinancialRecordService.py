from abc import ABC, abstractmethod

class IFinancialRecordService(ABC):
    @abstractmethod
    def AddFinancialRecord(self):
        pass

    @abstractmethod
    def GetFinancialRecordById(self):
        pass

    @abstractmethod
    def GetFinancialRecordsForEmployee(self):
        pass

    @abstractmethod
    def GetFinancialRecordsForDate(self):
        pass
