class Score:

    def __init__(self):
        self.score = 0

    # 단어의 길이가 길수록 더해지는 점수가 커짐
    def increaseScore(self, answer):
        if len(answer) <= 6:
            self.score += 1

        elif len(answer) <= 11:
            self.score += 2

        elif len(answer) <= 15:
            self.score += 3

        elif len(answer) <= 20:
            self.score += 5
