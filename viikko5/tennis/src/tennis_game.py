class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.add_point_to_player1()
        else:
            self.add_point_to_player2()
            
    def add_point_to_player1(self):
        self.m_score1 = self.m_score1 + 1

    def add_point_to_player2(self):
        self.m_score2 = self.m_score2 + 1


    def get_score(self):
        score = ""
        if self.m_score1 == self.m_score2:
            score = self.get_even_score()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            score = self.get_position()            
        else:
            score = self.get_score_score(score)
        return score
    
    def get_even_score(self):
        if self.m_score1 == 0:
            even_score = "Love-All"
        elif self.m_score1 == 1:
            even_score = "Fifteen-All"
        elif self.m_score1 == 2:
            even_score = "Thirty-All"
        elif self.m_score1 == 3:
            even_score = "Forty-All"
        else:
            even_score = "Deuce"
        return even_score

    def get_position(self):
        minus_result = self.m_score1 - self. m_score2
        if minus_result == 1:
            position_score = "Advantage player1"
        elif minus_result == -1:
            position_score = "Advantage player2"
        elif minus_result >= 2:
            position_score = "Win for player1"
        else:
            position_score = "Win for player2"
        return position_score

    def get_score_score(self, score):
        temp_score = 0
        for i in range(1, 3):
            if i == 1:
                temp_score = self.m_score1
            else:
                score = score + "-"
                temp_score = self.m_score2
            if temp_score == 0:
                score = score + "Love"
            elif temp_score == 1:
                score = score + "Fifteen"
            elif temp_score == 2:
                score = score + "Thirty"
            elif temp_score == 3:
                score = score + "Forty"
        return score