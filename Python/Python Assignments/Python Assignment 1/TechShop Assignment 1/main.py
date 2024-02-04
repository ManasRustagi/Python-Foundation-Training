from db_connection import DBConnector
from Customer import Customer
from Orders import orders
from Product import product
from OrderDetails import orderdetails
from Inventory import inventory
db_connector = DBConnector(host="localhost", user="root", password="root", port="3306", database="TechShop")
customer=Customer(1,"John","Doe","John.doe@example.com","1234567890","123 main st", db_connector)
products=product(1,"Laptop","PC","1320",db_connector)
orders=orders(1,1,'2024-01-15',3080,db_connector)
orderdetails=orderdetails(1,1,2,3,db_connector)
inventory=inventory( 1 ,1,50,'2024-01-15',db_connector)
'''customer.UpdateCustomerInfo(Phone='45454545', Email='email@gmail.com',Address='New Delhi',CustomerID='1')
customer.GetCustomerDetails(2)
customer.create(12,"Manas","Rustagi","manasrustagi16@gmail.com","7982681438","Karol bagh")
customer.CalcualteTotalOrders(1)
customer.UpdateCustomerInfo("1234567890","abcd@outloo.com","New York",1)
products.GetProductDetails(5)
products.UpdateProductInfo(980,"Phone",2)
products.Is_product_Instock(5)
orders.CalculateTotalAmount(8)

orders.CancelOrder(15)
orderdetails.Calculate_subtotal(2)
orderdetails.GetOrderdetailInfo(5)
orderdetails.Update_Quantity(3,5)
orderdetails.AddDiscount(15,4)
inventory.GetProduct(2)
inventory.QuantityInStock(5)
inventory.AddtoQuantity(5,6)
inventory.RemoveFromInventory(2,3)
inventory.UpdateStockQuantity(55,7)
inventory.IsProductAvailable(12)
inventory.IsProductAvailable(10)
inventory.GetInventoryValue()
inventory.ListLowStockProducts(25)
inventory.ListOutOfStockProducts()
inventory.ListAllProducts()
'''
orders.GetOrderDetails(9)
