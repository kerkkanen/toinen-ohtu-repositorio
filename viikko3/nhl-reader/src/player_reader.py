import requests
from player import Player

class PlayerReader():

    def __init__(self, url):
        self.stats = requests.get(url).json()

    def get_players(self):
        players = []

        for player_dict in self.stats:
            name = player_dict['name']
            nationality = player_dict['nationality']
            team = player_dict['team']
            goals = player_dict['goals']
            assists = player_dict['assists']
            player = Player(name, nationality, team, goals, assists)
            players.append(player)
        return players