

class product:
    def __init__(self,productid : int, productname : str, description : str, price : float,db_connector):
        self._ProductID = productid
        self._ProductName = productname
        self._Description = description
        self._Price = price
        self.db_connector = db_connector

    @property
    def ProductID(self):
        return self._ProductID
    @ProductID.setter
    def ProductID(self,new_productID):
        self._ProductID=new_productID

    @property
    def ProductName(self):
        return self._ProductName
    @ProductName.setter
    def ProductName(self,new_productname):
        self._ProductName=new_productname

    @property
    def Description(self):
        return self._Description
    @Description.setter
    def Description(self,new_description):
        self._Description=new_description

    @property
    def Price(self):
        return self._Price
    @Price.setter
    def Price(self,new_price):
        if new_price >= 0:
            self._Price=new_price
        else:
            pass


    def GetProductDetails(self,ProductID):
        try:
            self.db_connector.open_connection()
            cur=self.db_connector.connection.cursor()
            query="Select * from Products Where ProductID=%s"
            values=(ProductID,)
            cur.execute(query,values)
            record=cur.fetchone()
            if record:

                print(f"Product ID =: {record[0]}")
                print(f"Product Name : {record[1]}")
                print(f"Description : {record[2]}")
                print(f"Price : {record[3]}")
            else:
                print("Prdoduct not found")
        except Exception as e:
            print("Incorrect Id")
        finally:
            self.db_connector.close_connection()



    def UpdateProductInfo(self,Price,Description,ProductID):
        try:
            self.db_connector.open_connection()
            cur=self.db_connector.connection.cursor()
            query="Update Products Set Description=%s,Price=%s Where ProductID=%s"
            values=(Description,Price,ProductID)
            cur.execute(query,values)
            self.db_connector.connection.commit()
            print("Updated Successfully")
        except Exception as e:
            print("Error")
        finally:
            self.db_connector.close_connection()

    def Is_product_Instock(self,ProductId):
        try:
            self.db_connector.open_connection()
            query = "Select QuantityInStock From Inventory Where ProductId=%s"
            values = (ProductId,)
            cur = self.db_connector.connection.cursor()
            cur.execute(query, values)
            record = cur.fetchone()
            if record:
                print(f"Qunatity in Stock = {record[0]}")
            else:
                print("Not Quantity Availabe")
        except Exception as e:
            print(f"Error Occured : {e}")
        finally:
            self.db_connector.close_connection()





