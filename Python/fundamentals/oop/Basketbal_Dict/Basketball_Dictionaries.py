class Player:
    def __init__(self, the_players):
        self.name = the_players['name']
        self.age = the_players['age']
        self.position = the_players['position']
        self.team = the_players['team']
        
    def __repr__(self):
        display = f"\nPlayer: {self.name}\nAge: {self.age}\nPosition: {self.position}\nTeam: {self.team}"
        return display
    @classmethod
    def get_team(cls, team_list):
        New_team = []
        for ball_player in team_list:
            New_team.append(Player(ball_player))
        return New_team
    
kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}
jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}
kyrie = {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
}
players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "", 
        "age":16, 
        "position": "P", 
        "team": "en"
    }
]
    
new_team = []
obj_player = Player.get_team(players)
print(obj_player)
for each_player in players:
    new_player = Player(each_player)
    new_team.append(new_player)
print(new_team)


#Challenge 2: Create instances using individual player dictionaries.
# player_kevin = Player(kevin)
# print(player_kevin) 
# player_jason = Player(jason)
# player_kyrie = Player(kyrie)
# print(f"Player: {player_kevin.name}\nAge: {player_kevin.age}\nPosition: {player_kevin.position}\nTeam: {player_kevin.team}")
# print(f"Player: {player_jason.name}\nAge: {player_jason.age}\nPosition: {player_jason.position}\nTeam: {player_jason.team}")
# print(f"Player: {player_kyrie.name}\nAge: {player_kyrie.age}\nPosition: {player_kyrie.position}\nTeam: {player_kyrie.team}")

# Challenge 3: Make a list of Player instances from a list of dictionaries


