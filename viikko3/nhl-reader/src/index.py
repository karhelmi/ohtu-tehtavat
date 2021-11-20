from playerreader import PlayerReader
from playerstats import PlayerStats

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url) #lisätty t.3
    stats = PlayerStats(reader) #lisätty t.3
    players = stats.top_scorers_by_nationality("FIN") #lisätty t.3
    print(players)

    for player in players: #lisätty t.3
        print(player) #lisätty t.3    
    
    #print("JSON-muotoinen vastaus:")
    #print(response)

    #players = []

    #for player_dict in response:
     #   if player_dict['nationality'] == "FIN":
      #      player = Player(
       #         player_dict['name'],player_dict['team'],
        #        player_dict['goals'],player_dict['assists']
         #   )

          #  players.append(player)

    #print("Oliot:")

    #players.sort(key = lambda players: players.goals + players.assists, reverse=True)

    #for player in players:
     #   print(player)

if __name__ == "__main__":
    main()
