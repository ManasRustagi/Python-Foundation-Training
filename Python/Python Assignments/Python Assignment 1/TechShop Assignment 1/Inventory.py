from datetime import datetime
class inventory:
    def __init__(self, inventoryID : int,productID, quantityinstock, LastStockUpdate : datetime,db_connector):
        self._InventoryID=inventoryID
        self._ProductID=productID
        self._QuantityInStock=quantityinstock
        self._LastStockupdate=LastStockUpdate
        self.db_connector=db_connector


    @property
    def InventoryId(self):
        return self._InventoryID
    @InventoryId.setter
    def InventoryID(self,new_inventoryID):
        self._InventoryId=new_inventoryID


    @property
    def ProductID(self):
        return self._ProductID
    @ProductID.setter
    def ProductId(self,new_productId):
        self._ProductID=new_productId


    @property
    def QuantityInStock(self):
        return self._QuantityInStock
    @QuantityInStock.setter
    def QuantityInStock(self,new_quantityinstock):
        self._QuantityInStock=new_quantityinstock


    @property
    def LastStockUpdate(self):
        return self._LastStockupdate
    @LastStockUpdate.setter
    def LastStockUpdate(self,new_laststockupdate):
        self._LastStockupdate=new_laststockupdate

    def GetProduct(self,InventoryId):
        try:
            self.db_connector.open_connection()
            cur=self.db_connector.connection.cursor()
            query="Select * from Products Where ProductID in (Select ProductId from Inventory where InventoryID = %s)"
            values=(InventoryId,)
            cur.execute(query,values)
            record=cur.fetchone()
            if record:
                print(f"Enter the Inventory ID for Which you want to know Product Details : {InventoryId}")
                print(f"ProductId : {record[0]}")
                print(f"Product Name : {record[1]}")
                print(f"Description : {record[2]}")
                print(f"Price : {record[3]}")
            else:
                print("Product ID not exixts")
        except Exception as e:
            print("Error In Finding Product")
        finally:
            self.db_connector.close_connection()

    def QuantityInStock(self,ProductId):
        try:
            self.db_connector.open_connection()
            cur=self.db_connector.connection.cursor()
            query="Select QuantityInStock From Inventory Where ProductId=%s"
            values=(ProductId,)
            cur.execute(query,values)
            record=cur.fetchone()
            if record:
                print(f"Enter the ProductID : {ProductId}")
                print(f"Quantity In Stock is  : {record[0]}")
            else:
                print("No Product Found in inventory")
        except Exception as e:
            print("Error infetching Stock")
        finally:
            self.db_connector.close_connection()

    def AddtoQuantity(self,Add_Quantity,ProductID):
        try:
            self.db_connector.open_connection()
            cur=self.db_connector.connection.cursor()
            query="Update Inventory Set QuantityInStock = QuantityInStock+%s Where ProductId=%s"
            values=(Add_Quantity,ProductID,)
            cur.execute(query,values)
            self.db_connector.connection.commit()
            print(f"For ProductId {ProductID} Quantity you want to add in stocks is : {Add_Quantity}")
            print("Quantity Added Successfully")
        except Exception as e:
            print("Error In updation")
        finally:
            self.db_connector.close_connection()

    def RemoveFromInventory(self,Quantity,ProductID):
        try:
            self.db_connector.open_connection()
            cur=self.db_connector.connection.cursor()
            query="Update Inventory set QuantityInStock=QuantityInStock-%s Where ProductID=%s"
            values=(Quantity,ProductID,)
            cur.execute(query,values)
            self.db_connector.connection.commit()
            print(f"For ProductId {ProductID} Quantity you want to remove in stocks is : {Quantity}")
            print("Quantity In Stock Updated Successfully")
        except:
            print("Error In Updation ")
        finally:
            self.db_connector.close_connection()

    def UpdateStockQuantity(self,new_quantity,ProductID):
        try:
            self.db_connector.open_connection()
            cur=self.db_connector.connection.cursor()
            query="Update Inventory set QuantityInStock=%s Where ProductID=%s"
            values=(new_quantity,ProductID,)
            cur.execute(query,values)
            self.db_connector.connection.commit()
            print(f"For ProductId {ProductID}  Updated Quantity will be {new_quantity}")
            print("Quantity updated Successfully")
        except Exception as e:(
            print("Error in updation"))
        finally:
            self.db_connector.close_connection()

    def IsProductAvailable(self,ProductId):
        try:
            self.db_connector.open_connection()
            cur=self.db_connector.connection.cursor()
            query="Select QuantityInStock From Inventory Where ProductID=%s"
            values=(ProductId,)
            cur.execute(query,values)
            record=cur.fetchone()
            print(f"Enter the ProductID for which you want to know stocks:{ProductId} ")
            if record:
                if record[0]>0:
                    print("Product Available")
                else:
                    print("Out Of Stock")
            else:
                print("Wrong Product ID")

        except Exception as e:
            print("Error in Fetching")
        finally:
            self.db_connector.close_connection()

    def GetInventoryValue(self):
        try:
            self.db_connector.open_connection()
            cur=self.db_connector.connection.cursor()
            query="Select Sum(Value) From (Select (I.QuantityInStock*P.Price) as Value From Inventory I Inner join Products P On I.ProductId=P.ProductID) a"
            cur.execute(query)
            record=cur.fetchone()
            if record:
                print(f"Total Inventory Value : {record[0]}")
            else:
                print("Something went wrong")
        except Exception as e:
            print("Error in Calculating")
        finally:
            self.db_connector.close_connection()

    def ListLowStockProducts(self,Threshold):
        try:
            self.db_connector.open_connection()
            cur = self.db_connector.connection.cursor()
            query="Select ProductId From Inventory Where QuantityInStock<%s"
            values=(Threshold,)
            cur.execute(query,values)
            record=cur.fetchall()
            print(f"Enter Threshold : {Threshold}")
            if record:
                print("Product ID for Products which have low Stocks in Inventory Are :")
                for i in record:
                    print(i[0])
            else:
                print("No Product Quantity is below threshold")
        except Exception as e:
            print("Error in Fetching")
        finally:
            self.db_connector.close_connection()

    def ListOutOfStockProducts(self):
        try:
            self.db_connector.open_connection()
            cur = self.db_connector.connection.cursor()
            query="Select ProductID From Inventory Where QuantityInStock <= 0"
            cur.execute(query)
            record=cur.fetchall()
            if record:
                for i in record:
                    print(i)
            else:
                print("No out of Stock Products")
        except Exception as e:
            print("Error in fetching")
        finally:
            self.db_connector.close_connection()

    def ListAllProducts(self):
        try:
            self.db_connector.open_connection()
            cur = self.db_connector.connection.cursor()
            query="Select ProductID,QuantityInStock From Inventory"
            cur.execute(query)
            record = cur.fetchall()
            if record:
                for i in record:
                    print(f"Product ID : {i[0]}, Quantity In Stock : {i[1]}")
            else:
                print("No Product in the inventory")
        except Exception as e:
            print("Error in fetching")
        finally:
            self.db_connector.close_connection()



