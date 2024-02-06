from Product import product

class electronics(product):
    def __init__(self,productId,brand,warrantyperiod):
        super().__init__(productId)
        self.brand=brand
        self.warrantyperiod=warrantyperiod


    @property
    def brand(self):
        return self.brand
    @brand.setter
    def brand(self,new_brand):
        self.brand=new_brand

    @property
    def warrantyperiod(self):
        return self.warrantyperiod
    @warrantyperiod.setter
    def warrantyperiod(self,new_warrantyperiod):
        self.warrantyperiod=new_warrantyperiod
        