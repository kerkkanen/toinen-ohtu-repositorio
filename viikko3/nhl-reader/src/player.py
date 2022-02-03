class Player:
    def __init__(self, name, nationality, team, goals, assists):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.goals = goals
        self.assists = assists
        self.scores = self.goals + self.assists

    def nationality(self):
        return self.nationality

    def team(self):
        return self.team

    def goals(self):
        return self.goals

    def assists(self):
        return self.assists
    
    def scores(self):
        return self.scores

    def __str__(self):
        return f"{self.name:20} {self.team} {self.goals} + {self.assists} = {self.scores}"
