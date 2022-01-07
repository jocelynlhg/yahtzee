from enum import Enum

class Scoreboard(Enum):
    chance = 0

    aces = 1
    twos = 2
    threes = 3
    fours = 4
    fives = 5
    sixes = 6

    threeOfAKind = 7
    fourOfAKind = 8
    fullHouse = 9
    smallStraight = 10
    largeStraight = 11
    yahtzee = 12

class Scorecard(object):
    def __init__(self):
        self.card = {}

        for rule in Scoreboard:
            self.card[rule] = [True, 0]

    def __getitem__(self, rule):
        return self.card[rule]

    def __setitem__(self, rule, v):
        self.card[rule] = v

    def update(self, rule, score):
        self.card[rule] = [score==0, score]

    def available(self, rule):
        return self.card[rule][0]

    def score(self, rule):
        return self.card[rule][1]

    def set_score(self, rule, value):
        if self.available(rule):
            self.card[rule][1] = value
