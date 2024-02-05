
class orderdetails:
    def __init__(self,orderdetailid : int, OrderID, ProductID, quantity : int,db_connector):
        self._OrderDetailID =orderdetailid
        self._OrderID=OrderID
        self._ProductID=ProductID
        self._Quantity = quantity
        self.db_connector=db_connector


    @property
    def OrderDetailID(self):
        return self._OrderDetailID
    @OrderDetailID.setter
    def OrderDetailID(self,new_orderdetailID):
        self._OrderDetailID=new_orderdetailID

    @property
    def OrderID(self):
        return self._OrderID
    @OrderID.setter
    def OrderID(self,new_orderID):
        self._OrderID=new_orderID

    @property
    def ProductID(self):
        return self._ProductID
    @ProductID.setter
    def ProductID(self,new_productID):
        self._ProductID=new_productID

    @property
    def Quantity(self):
        return self._Quantity
    @Quantity.setter
    def Quantity(self,new_quantity):
        if new_quantity >= 0:
            self._Quantity=new_quantity
        else:
            pass

    def Calculate_subtotal(self,OrderDetailsID):
        try:
            self.db_connector.open_connection()
            cur=self.db_connector.connection.cursor()
            query="Select OD.Quantity,P.Price From OrderDetails OD Inner Join Products P ON Od.ProductId=P.ProductID Where OrderDetailID=%s"
            values=(OrderDetailsID,)
            cur.execute(query,values)
            record=cur.fetchone()
            if record:
                quantity=record[0]
                price=record[1]
                Subtotal=quantity*price
                print(f"Subtotal for this Order Detail Id {OrderDetailsID} is : {Subtotal}")
            else:
                print("OrderDetailID not Found")

        except:
            print("Error in fetching OrderDetailId")
        finally:
            self.db_connector.close_connection()

    def GetOrderdetailInfo(self,OrderDetailID):
        try:
            self.db_connector.open_connection()
            cur=self.db_connector.connection.cursor()
            query="Select * From OrderDetails Where OrderID=%s"
            values=(OrderDetailID,)
            cur.execute(query,values)
            record=cur.fetchone()
            if record:
                print(f"Getting info for Order Detail ID : {OrderDetailID}")
                print(f"OrderDetailID : {record[0]}")
                print(f"OrderID : {record[1]}")
                print(f"ProductID : {record[2]}")
                print(f"Quantity : {record[3]}")
            else:
                print("No Order Found")
        except Exception as e:
            print("Error Please Enter the OrderDeatailId only")
        finally:
            self.db_connector.close_connection()

    def Update_Quantity(self,new_quantity,OrderDetailID):
        try:
            self.db_connector.open_connection()
            cur=self.db_connector.connection.cursor()
            print(f"Updating Quantity to {new_quantity} of Order Detail ID {OrderDetailID} ")
            query="Update OrderDetails Set Quantity=%s Where OrderDetailID =%s"
            values=(new_quantity,OrderDetailID,)
            cur.execute(query,values)
            self.db_connector.connection.commit()
            print("Quantity Updated Successfully")
        except:
            print("Error In Updation")
        finally:
            self.db_connector.close_connection()

    def AddDiscount(self,Discount_percentage,OrderID):
        try:
            if Discount_percentage>0:
                self.db_connector.open_connection()
                cur = self.db_connector.connection.cursor()
                query = "Select TotalAmount From Orders Where OrderID=%s"
                values = (OrderID,)
                cur.execute(query, values)
                record = cur.fetchone()
                if record:
                    print(f"Getting Discount on Order ID : {OrderID}")
                    Amount = record[0]
                    Payment = Amount - (Amount * Discount_percentage / 100)
                    print(f"Total Amount after Discount = {Payment}")
                else:
                    print("Wrong OrderID Entered")
            else:
                print("Discount Percentage Cannot be in Negative")
        except:
            print("Error in Payment")
        finally:
            self.db_connector.close_connection()


