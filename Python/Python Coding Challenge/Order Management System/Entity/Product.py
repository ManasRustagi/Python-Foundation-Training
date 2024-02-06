class product:
    def __init__(self,productId,productname,description,price,quantityinstock,type):
        self.productid=productId
        self.productname=productname
        self.description=description
        self.price=price
        self.quantityinstock=quantityinstock
        self.type=type



    @property
    def productID(self):
        return self.productid
    @productID.setter
    def productID(self,new_productid):
        self.productid=new_productid

    @property
    def productname(self):
        return self.productname
    @productname.setter
    def productname(self,new_productname):
        self.productname=new_productname

    @property
    def description(self):
        return self.description
    @description.setter
    def description(self,new_description):
        self.description=new_description

    @property
    def price(self):
        return self.price
    @price.setter
    def price(self,new_price):
        self.price=new_price



    @property
    def quantityinstock(self):
        return self.quantityinstock
    @quantityinstock.setter
    def quantityinstock(self,new_quantityinstock):
        self.quantityinstock=new_quantityinstock

    @property
    def type(self):
        return self.type
    @type.setter
    def type(self,new_type):
        self.type=new_type

