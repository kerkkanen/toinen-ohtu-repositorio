class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = player1_name
        self.player2 = player2_name
        self.score1 = 0
        self.score2 = 0
        self.tielist = ["Love-All", "Fifteen-All",
                        "Thirty-All", "Forty-All", "Deuce"]
        self.scorelist = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player_name):
        if player_name == self.player1:
            self.score1 = self.score1 + 1
        else:
            self.score2 = self.score2 + 1

    def get_score(self):

        if self.tie():
            return self.tielist[self.score1]

        true, player = self.points_over_four()
        if true:
            return self.win_or_advantage(player)

        return f"{self.scorelist[self.score1]}-{self.scorelist[self.score2]}"

    def tie(self):
        if self.score1 == self.score2:
            return True
        return False

    def points_over_four(self):
        if max(self.score1, self.score2) >= 4:
            if self.score1 > self.score2:
                return True, self.player1
            else:
                return True, self.player2
        return False, ""

    def win_or_advantage(self, player):
        if abs(self.score1 - self.score2) >= 2:
            return f"Win for {player}"
        return f"Advantage {player}"

