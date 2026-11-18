'''
15. Sports Management
Player
CricketPlayer
Captain(CricketPlayer)

Add captain-specific functionality.
'''
class Player:
    def players(self):
        print(" player class method")

class CricketPlayer:
    def CricketPlayers(self):
        print("CricketPlayer class method")

class Captain(Player,CricketPlayer):
    def captain(self):
        print("captain class method")

obj=Captain()
obj.players()
obj.CricketPlayers()
obj.captain()
