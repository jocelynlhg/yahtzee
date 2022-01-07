from functions import *
from score import Scoreboard, Scorecard

class Dice(object):
    def __init__(self):
        self.dice = []
    
    def roll(self, n):
        return random_list(n, 7, 1)

    def remove_indices(self, indices):
        if type(indices) == int:
            self.dice.pop(indices)
        elif type(indices) == list:
            self.dice = [self.dice[i] for i in range(len(self.dice)) if i not in indices]
    
    def add_values(self, values):
        if type(values) == int:
            self.dice.append(values)
        elif type(values) == list:
            self.dice += values
    def upper(self, v):
        return v * self.dice.count(v)

    def straight(self, length):
        diceRange = list(range(1, 7))
        for i in range(len(diceRange)-length+1):
            if is_subset(diceRange[i:i+length], self.dice):
                return True
        return False

    def calculate(self):
        sc = Scorecard()

        sc.update(Scoreboard.chance, sum(self.dice))
        sc.update(Scoreboard.aces, self.upper(1))
        sc.update(Scoreboard.twos, self.upper(2))
        sc.update(Scoreboard.threes, self.upper(3))
        sc.update(Scoreboard.fours, self.upper(4))
        sc.update(Scoreboard.fives, self.upper(5))
        sc.update(Scoreboard.sixes, self.upper(6))
        
        sc.update(Scoreboard.threeOfAKind, sum(self.dice) if max_duplicates(self.dice) >= 3 else 0)
        sc.update(Scoreboard.fourOfAKind, sum(self.dice) if max_duplicates(self.dice) >= 4 else 0)

        sc.update(Scoreboard.fullHouse, 25 if len(set(self.dice)) == 2 else 0)
        sc.update(Scoreboard.smallStraight, 30 if self.straight(4) else 0)
        sc.update(Scoreboard.largeStraight, 30 if self.straight(5) else 0)
        sc.update(Scoreboard.yahtzee, 50 if len(set(self.dice)) == 1 else 0)

        return sc
    def __str__(self):
        return str(self.dice)
