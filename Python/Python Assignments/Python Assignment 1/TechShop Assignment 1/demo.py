import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="root",port="3306",database="TechShop")
print(conn)
cur=conn.cursor()
query="Select * From Customers Where CustomerId=%s"
values=('1',)
cur.execute(query,values)
customer_detail=cur.fetchone()
if customer_detail:
    print(f"CustomerID : {customer_detail[0]}")
    print(f"First Name : {customer_detail[1]}")
    print(f"Last Name : {customer_detail[2]}")
    print(f"Email : {customer_detail[3]}")
    print(f"Phone Number : {customer_detail[4]}")
    print(f"Address : {customer_detail[5]}")
else:
    print("No")