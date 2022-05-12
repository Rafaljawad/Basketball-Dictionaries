class Player:
    new_team_list=[]
#Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.
    def __init__(self,player_data):
        self.name=player_data['name']
        self.age=player_data['age']
        self.position=player_data['position']
        self.team=player_data['team']
        # Player.new_team_list.append(self)
    @classmethod
    def get_team(cls, team_list):
        for team_object in team_list:
            player=Player(team_object)
            cls.new_team_list.append(player)
        return Player.new_team_list

    def print_players_info(self):
        return f"name:{self.name}, age: {self.age}, position: {self.position}, team: {self.team}"

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
#Challenge 2: Create instances using individual player dictionaries.
# Given these variables, create Player instances for each of the following dictionaries. Be sure to instantiate these outside the class definition, in the outer scope.

kevin=Player(kevin)
print(kevin.print_players_info())
jason=Player(jason)
print(jason.print_players_info())
kyrie=Player(kyrie)
print(kyrie.print_players_info())

print("********************finishing challeng2**********************************************")

#Challenge 3: Make a list of Player instances from a list of dictionaries
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


new_team=[]
for player in range(len(players)):
    player_data=Player(players[player]).print_players_info()
    new_team.append(player_data)
print(new_team[:])

print("****************finishing challenge 3**************************************************")

# NINJA BONUS: Add a get_team(cls, team_list) @class method
# Add an @class method called get_team(cls, team_list) that, given a list of dictionaries populates and returns a new list of Player objects. Be sure to test your method!
print(Player.get_team(players))
print(Player.new_team_list)



