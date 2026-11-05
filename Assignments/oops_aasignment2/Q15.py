class Cricket:
    players=[]
    def __init__(self,name,role,run):
        self.name=name
        self.role=role
        self.run=run
        
    def add_player_details(self):
        Cricket.players.append(self)

    def display_stastics(self):
        for player in Cricket.players:
            print(f"\nname : {player.name}")
            print(f"role : {player.role}")
            print(f"run scored : {player.run}")

    def highest_score(self):
        highest=0
        player=""
        for player in Cricket.players:
            if player.run>highest:
                highest=player.run
                player=player.name

        print(f"{player} has highest run {highest}")
                

    

player1=Cricket("virat","batsman",56)
player2=Cricket("rohit","batsman",6)
player3=Cricket("rishab","batsman",86)

player1.add_player_details()
player2.add_player_details()
player3.add_player_details()

player1.display_stastics()
player1.highest_score()



    
      