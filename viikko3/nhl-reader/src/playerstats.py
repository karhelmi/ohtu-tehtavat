class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
    
    def top_scorers_by_nationality(self, nationality):
        selected_players = self.reader.get_players(nationality)
        
        selected_players.sort(key = lambda selected_players: selected_players.goals + selected_players.assists, reverse=True)
        return selected_players