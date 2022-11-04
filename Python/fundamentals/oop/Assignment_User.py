class User:
    def __init__(self, first_name,last_name,email,age,):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.gold_card_points = 0
        self.is_rewards_member = False    
    def display_info (self):
        print (f'{self.first_name}')
        print (f'{self.last_name}')
        print (f'{self.email}')
        print (f'{self.age}')
        print (f'{self.gold_card_points}')
        print (f'{self.is_rewards_member}')
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        
    def spend_points(self, amount):
        self.gold_card_points -= amount
        
            
kevin = User("Kevin","Cantrell","blah@gmail.com",35)
jen = User("jenny","kearns","blah@gmail.com",37)
john = User("john","jake","blah@gmail.com",20,)

kevin.enroll()
kevin.spend_points(80)# <---use any number to spend points
kevin.display_info()
# ------------------------------------------------------------------------------------------------
jen.enroll()
jen.spend_points(50)# <---use any number to spend points
jen.display_info()

john.enroll()
john.spend_points(130)# <---use any number to spend points
john.display_info()
