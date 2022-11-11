
class Items:
    def __init__(self):
        self.items = []
    
    
    
        pass

    
class Potions(Items):
    def __init__(self, name):
        super().__init__()
        self.name = name
        
        
health_Pot = Potions("red vial")
print(health_Pot)
health_Pot.items.append(health_Pot.name)
print(health_Pot.items)