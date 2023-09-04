class Fridge:
    contents = {}

    def add(self, product:str, quantity:float):
        if product in self.contents:
            self.contents[product] += quantity
        else:    
            self.contents[product] = quantity

    def remove(self, product:str, quantity:float):
        if self.check(product, quantity):
            self.contents[product] -= quantity
            if self.contents[product] == 0:
                del self.contents[product]
        else:
            print("No such product or quantity is not enough")

    def check(self, product:str, quantity:float):
        if product in self.contents:
            print(f"{product} found {self.contents[product]}")
            if quantity <= self.contents[product]:
                return True
        return False

    def list_products(self):
        for product, quantity in self.contents.items():
            print(f"{product:30s} {quantity:>5g}")
