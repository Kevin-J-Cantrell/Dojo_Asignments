class Pet:
    def __init__(self, name,animal,tricks, health=10,energy=10):

        self.name = name
        self.animal = animal
        self.tricks = tricks
        self.health = health
        self.energy = energy
        
    def sleep(self):# sleep() - increases the pets energy by 25
        self.energy += 25
        print(f'{self.name} is Sleeping....')
        return self
    def eat(self):# eat() - increases the pet's energy by 5 & health by 10
        self.energy += 5
        self.health += 10
        print(f'{self.name} is Eating .')
        return self
    def play(self):# play() - increases the pet's health by 5
        self.health += 5
        print(f'{self.name} is playing.')
        return self
    def noise(self):# noise() - prints out the pet's sound
        if self.animal == "dog" or self.animal == "Dog":
            return print('Woof Woof...')
        elif self.animal == "cat" or self.animal == "Cat":
            return print('Meow...')
        elif self.animal == "snake" or self.animal == "Snake":
            return print('Hiss...')
        elif self.animal == "horse" or self.animal == "Horse":
            return print('neigh...')
        elif self.animal == "hamster" or self.animal == "Hamster":
            return print('Squeak...')
        else: 
            print('Unknown Sound...')
        return self
    
