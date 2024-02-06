from OrderProcessor import orderprocessor
from DB_Util import DBConnector
from Exception.exception import InvalidDataException
db_connector = DBConnector(host="localhost", user="root", password="root", port="3306", database="OrderManagementSystem")


class IOrderManagementRepository():
    def __init__(self,db_connector):
        self.db_connector=db_connector


    def create_order(self):
        userID=input("Enter the User ID : ")
        productID=input("Enter the Product Id of order you want to purchase : ")
        Quantity=input("Quantity you want to purchase : ")
        existing_record=self.get_user_id(userID)
        if existing_record is None:
            self.create_user()

        existing_product=self.get_productID(productID)
        if existing_product is None:
            self.create_product()
        orderprocess.create_order(userID,productID,Quantity)

    def cancel_order(self):
        userID=input("Please Enter the user ID : ")
        orderId=input("Enter the Order ID you want to delete")
        existing_order=self.get_order_id(userID,orderId)
        if existing_order:
            self.delete_order(orderId)
        else:
            raise InvalidDataException("This Order ID not associated with this user ID")

    def create_product(self):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        productId=self.get_unique_productId()
        productname=input("Enter the Product Name : ")
        description=input("Enter the discription of Product : ")
        price=input("Enter the price of Product : ")
        Quantity=int(input("Enter the Quantity in Stock : "))
        type=input("Enter the type of the Product 1. Electronics  2. Clothing : ")
        query="Insert into Product values(%s,%s,%s,%s,%s,%s)"
        values=(productId,productname,description,price,Quantity,type,)
        cur.execute(query,values)
        self.db_connector.connection.commit()

    def create_user(self):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        userID=self.get_unique_userId()
        username=input("Enter the username : ")
        password=input("Enter the password : ")
        role=input("Enter the Role 1.Admin 2.User : ")
        query="Insert into User values(%s,%s,%s,%s)"
        values=(userID,username,password,role,)
        cur.execute(query,values)
        self.db_connector.connection.commit()



    def get_all_Products(self):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        cur.execute("select Productname from Product")
        record = cur.fetchall()
        for i in record:
            print(i[0])

    def get_allProducts(self):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        cur.execute("select Productname from Product")
        record = cur.fetchall()
        return record

    def getOrderByUser(self):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        UserID=input("Enter the user Id For which you want to fetch orders: ")
        query="Select OrderId from Orders Where UserID=%s"
        values=(UserID)
        cur.execute(query,values)
        record=cur.fetchall()
        for i in record:
            print(i[0])


    def get_user_id(self,userID):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        cur.execute("Select UserID from user Where UserID=%s",(userID,))
        return cur.fetchone()


    def get_productID(self,productID):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        cur.execute("Select ProductID from Product Where ProductID=%s",(productID,))
        return cur.fetchone()

    def get_quantity(self,productId):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        cur.execute("Select QuantityInStock From Product Where ProductId =%s",(productId,))
        record=cur.fetchone()
        return record[0]

    def get_order_id(self,UserID,orderID):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        cur.execute("Select orderId from Orders Where userId=%s and orderID=%s",(UserID,orderID,))
        return cur.fetchone()

    def delete_order(self,orderID):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        cur.execute("Delete From Orders Where OrderId=%s",(orderID))
        self.db_connector.connection.commit()

    def get_unique_productId(self):
        return len(self.get_allProducts())+1



    def get_unique_userId(self):
        return len(self.get_alluser())+1

    def get_alluser(self):
        self.db_connector.open_connection()
        cur = self.db_connector.connection.cursor()
        cur.execute("select userName from User")
        record=cur.fetchall()
        return record
def main():
    print("Choose from The below options : ")
    print("1. If you want to create Order")
    print("2. If you want to cancel the order")
    print("3. If you want add a product in the inventory")
    print("4. If you want to Create user ID")
    print("5. If you want to see all the products in the inventory:")
    print("6. If you want to see Completed Orders")
    choice = input("Enter your choice : ")
    if choice == '1':
        order_respositoy.create_order()
    elif choice == '2':
        order_respositoy.cancel_order()
    elif choice == '3':
        order_respositoy.create_product()
    elif choice == '4':
        order_respositoy.create_user()
    elif choice == '5':
        order_respositoy.get_all_Products()
    elif choice == '6':
        order_respositoy.getOrderByUser()
    else:
        print("Enter correct choice")
order_respositoy=IOrderManagementRepository(db_connector)
orderprocess = orderprocessor(db_connector)

main()

