from datetime import datetime

class orders:
    def __init__(self,order_id : int,customerID : int, orderdate : datetime, totalAmount : float,db_connector):
        self._OrderID = order_id
        self._CustomerID = customerID
        self._OrderDate = orderdate
        self._TotalAmount = totalAmount
        self.db_connector = db_connector


    @property
    def OrderID(self):
        return self._OrderID
    @OrderID.setter
    def OrderID(self,new_orderID):
        self._OrderID=new_orderID

    @property
    def CustomerID(self):
        return self._CustomerID
    @CustomerID.setter
    def CustomerID(self,new_customerID):
        self._CustomerID=new_customerID

    @property
    def OrderDate(self):
        return self._OrderDate
    @OrderDate.setter
    def OrderDate(self,new_orderdate):
        self._OrderDate-new_orderdate

    @property
    def TotalAccount(self):
        return self._TotalAmount
    @TotalAccount.setter
    def TotalAccount(self,new_total):
        self._TotalAmount=new_total

    def CalculateTotalAmount(self,OrderID):
        try:
            self.db_connector.open_connection()
            cur=self.db_connector.connection.cursor()
            query="Select TotalAmount From Orders Where OrderId = %s"
            values=(OrderID,)
            cur.execute(query,values)
            record=cur.fetchone()
            if record:
                print(f"Total Amount of OrderID {OrderID} is : {record[0]}")
            else:
                print("NO Order Done")
        except Exception as e:
            print("NO ORDER ID FOUND")
        finally:
            self.db_connector.close_connection()

    def GetOrderDetails(self,OrderID):
        try:
            self.db_connector.open_connection()
            cur=self.db_connector.connection.cursor()
            query="Select * from Orders Where OrderID=%s"
            values=(OrderID,)
            print (f"Enter the Order Id : {OrderID}")
            print("Getting Details ........")
            cur.execute(query,values)
            record=cur.fetchone()
            if record:
                print(f"OrderID : {record[0]}")
                print(f"CustomerID : {record[1]}")
                print(f"Order Date : {record[2]}")
                print(f"Total Amount : {record[3]}")
            else:
                print("OrderID not Present")
        except Exception as e:
            print("Error")
        finally:
            self.db_connector.close_connection()

    def UpdateOrderStatus(self):
        # no Status column in database Schema
        pass

    def CancelOrder(self,OrderID):
        try:
            self.db_connector.open_connection()
            cur = self.db_connector.connection.cursor()
            query = "Select * from Orders Where OrderID=%s"
            values = (OrderID,)
            cur.execute(query, values)
            record = cur.fetchone()
            if record:
                print(f"Delting Order {OrderID}")
                print("Wait work in Progress.........")
                query1 = "Delete From Orders Where OrderID=%s"
                cur.execute(query1, values)
                query2 = (
                    "UPDATE Inventory SET QuantityInStock = QuantityInStock + (SELECT Quantity FROM OrderDetails WHERE OrderDetails.ProductID = Inventory.ProductID AND OrderDetails.OrderId = %s) WHERE EXISTS (SELECT 1 FROM OrderDetails WHERE OrderDetails.ProductID = Inventory.ProductID AND OrderDetails.OrderId = %s)")
                values1 = (OrderID, OrderID,)
                cur.execute(query2, values1)
                query3 = ("Delete From OrderDetails Where OrderID=%s")
                cur.execute(query3, values)
            else:
                print("No ORDERID Found")
        except Exception as e:
            print("Error in Deletion")
        finally:
            self.db_connector.close_connection()

















