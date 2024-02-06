from DB_Util import DBConnector
from dao.IOrderManagementRepository import IOrderManagementRepository
class OrderManagement:

    def main():
        db_connector = DBConnector(host="localhost", user="root", password="root", port="3306",database="OrderManagementSystem")
        order_respositoy = IOrderManagementRepository(db_connector)
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

if __name__=='__main__':
    obj=OrderManagement
    obj.main()




