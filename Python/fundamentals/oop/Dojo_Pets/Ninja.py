from pets import Pet
class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
        
    def walk(self):# walk() - walks the ninja's pet invoking the pet play() method
        self.pet.play()
        return self
    def feed(self):# feed() - feeds the ninja's pet invoking the pet eat() method
        self.pet.eat()
        return self
    def bathe(self):# bathe() - cleans the ninja's pet invoking the pet noise() method
        self.pet.noise()
        return self

Winter = Pet("Winter","Dog","sit")
# first_name, last_name, pet, treats, pet_food
Shinzo = Ninja("Kuro","Shinigami",Winter,"jerky","Chow")
Shinzo.feed().bathe().walk()
