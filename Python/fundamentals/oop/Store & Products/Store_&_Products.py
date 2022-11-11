class Store:
    def __init__(self, name=[],price=[]):
        self.name = name
        self.price = price
        
    def add_product(self):#takes a product and adds it to the store
        add_another = "Y"
        while add_another.upper() == "Y":
            new_product = input("Add Product: ")
            self.name.append(new_product)
            add_another = input("more products to add? (y/n) ")
        return self.name
    def sell_product(self,id): #remove the product from the store's list of products given the id
        buy_product = "Y"
        while buy_product.upper() == "Y":
            new_product = input("Buy Product: ")
            self.name.pop(new_product)
            buy_product = input("Buy more products? (y/n) ")                      #(assume id is the index of the product in the list) and print its info.
        return self.name
    def inflation(self, percent_increase):
        
        pass
    def set_clearance(self, category, percent_discount):
        
        pass
class Product(Store):
    def __init__(self,name,price,category):
        super().__init__(name,price)
        self.category = category
        
    def update_price(self, percent_change, is_increased):
        if is_increased is True:
            Store.inflation = percent_change
            
        else:
            Store.set_clearance = percent_change
            
        pass
    def print_info(self): # print the name of the product, its category, and its price.
        
        pass
    
shopper = Store()
shopper.add_product()
kevin = shopper.name

print(kevin)




