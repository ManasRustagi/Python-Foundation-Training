from abc import ABC, abstractmethod
from DB_Util import DBConnector
class IOrderManagemntRespository(ABC):
    @abstractmethod
    def create_order(self,user,products):
        pass

    @abstractmethod
    def cancel_order(self,userID,orderId):
        pass

    @abstractmethod
    def create_product(self,admin_user,products):
        pass

    @abstractmethod
    def create_user(self,user):
        pass

    @abstractmethod
    def get_all_products(self):
        pass

    @abstractmethod
    def getOrderByUser(self,user):
        pass

db_connector = DBConnector(host="localhost", user="root", password="root", port="3306",database="OrderManagementSystem")
class orderprocessor:
    def __init__(self,db_connector):
        self.db_connector=db_connector


    def create_order(self,userID,productID,Quantity):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        orderID=self.get_unique_orderId()
        userID=userID
        productID=productID
        Quantity=Quantity
        cur.execute("Select Price from Product Where ProductId=%s",(productID,))
        record=cur.fetchone()
        TotalAmount=Quantity*record[0]
        Query="INSERT INTO Orders (orderID, userID, ProductId, TotalAmount,Quantity,OrderDate) VALUES (%s, %s, %s, %s,%s,CURDATE())"
        values=(orderID,userID,productID,TotalAmount,Quantity,)
        cur.execute(Query,values)
        self.db_connector.connection.commit()
        self.db_connector.close_connection()

    def get_unique_orderId(self):
        return len(self.get_allorders()) + 1

    def get_allorders(self):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        cur.execute("Select orderID from Orders")
        record = cur.fetchall()
        return record
