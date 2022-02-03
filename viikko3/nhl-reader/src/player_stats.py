from player_reader import PlayerReader

class PlayerStats():

    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players_by_nationality = []

        for player in self.players:
            if player.nationality == nationality:
                players_by_nationality.append(player)
        players_by_nationality.sort(key=lambda player: player.scores)
        players_by_nationality.reverse()
        return players_by_nationality