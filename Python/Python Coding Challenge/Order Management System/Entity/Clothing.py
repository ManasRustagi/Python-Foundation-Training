from Product import product


class clothing(product):
    def __init__(self, productId, size, color):
        super().__init__(productId)
        self.size = size
        self.color = color

    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, new_size):
        self.size = new_size

    @property
    def color(self):
        return self.color

    @color.setter
    def color(self, new_color):
        self.color = new_color
