from main import Char 

class Archer(Char):
    def __init__(self, name,char_class,defense,attack,health=100,stamina=100):
        super().__init__(name,char_class,defense,attack,health,stamina)
        
        
        

        
        
class Warrior(Char):
    def __init__(self, name,char_class,defense,attack,health=200,stamina=100):
        super().__init__(name,char_class,defense,attack,health,stamina)
        
        
        

        
        
class Mage(Char):
    def __init__(self, name,char_class,defense,attack,health=100,stamina=50,manna=100):
        super().__init__(name,char_class,defense,attack,health,stamina)
        self.manna = manna
        
        

        
        
class Thief(Char):
    def __init__(self, name,char_class,defense,attack,health=100,stamina=100,):
        super().__init__(name,char_class,defense,attack,health,stamina)
        self.steal = steal
        self.stelth = stelth
        
        

        

class Thief(Char):
    def __init__(self, name,char_class,defense,attack,health,stamina=100,):
        super().__init__(name,char_class,defense,attack,health,stamina)