from score import Scoreboard, Scorecard
from dice import Dice
import os #only for my implementation of get_input


class Player(object):
    def __init__(self):
        self.dice = Dice()
        self.scoreCard = Scorecard()
        self.rolls_left = 3
        self.save_indices = []
        self.dice.add_values(self.dice.roll(5))
        self.state = 0

    def save(self, n):
        self.save_indices = n[:]
    
    def purge(self):
        self.dice.remove_indices([i for i in range(5) if i not in self.save_indices])

    def reroll(self):
        self.purge()
        if self.rolls_left > 0:
            newValues = self.dice.roll(6 - len(self.save_indices))
            newDice = [0,0,0,0,0]
            cc = 0
            nc = 0
            for i in range(5):
                if i in self.save_indices:
                    newDice[i] = self.dice.dice[cc]
                    cc+=1
                else:
                    newDice[i] = newValues[nc]
                    nc+=1
            self.dice.dice = newDice
            self.rolls_left -= 1

    def display_dice(self):
        print("dice: {}".format(self.dice))

    def get_input(self):
        os.system('cls' if os.name=='nt' else 'clear')
        if self.state == -1:
            self.rolls_left = 3
            self.save_indices = []
            self.dice = Dice()
            self.dice.add_values(self.dice.roll(5))
            self.state = 0
            return
        elif self.state == 0:
            self.display_dice()
            if (self.rolls_left > 0):
                print("You have {} re-roll{}".format(self.rolls_left, "s" if self.rolls_left > 1 else ""))
                print("1. Save dice")
                print("2. Re-roll")
                print("3. Pick point slot")
                i = int(input("> "))
                self.state = int(i)
                return
            else:
                self.state = 3
                return
        elif self.state == 1:
            self.display_dice()
            print("Saved: {}".format(self.save_indices))
            index = input("save (enter by index): ")
            if index != "q":
                if "," in index:
                    index = [int(i) for i in index.replace(" ", "").split(",")]
                    self.save(index)
                else:
                    self.save([index])
            self.state = 0
            return
        elif self.state == 2:
            self.reroll()
            self.state = 0
            return
        elif self.state == 3:
            self.display_dice()
            dsc = self.dice.calculate()
            print("score card:")
            for i in Scoreboard:
                print("\t{}: {}".format(str(i).split(".")[1], self.scoreCard.score(i)))
            for i in range(13):
                if self.scoreCard.available(Scoreboard(i)) and not dsc.available(Scoreboard(i)):
                    print("{}. {}".format(i, str(Scoreboard(i)).split(".")[1]))
            index = int(input("> "))
            newScore = dsc.score(Scoreboard(index))
            self.scoreCard.set_score(Scoreboard(index), newScore)
            self.state = -1

    def __str__(self):
        dice = "dice: {}".format(self.dice)
        card = "score card:\n"
        for i in Scoreboard:
            card += "\t{}: {}\n".format(i, self.scoreCard.score(i))
        return dice+"\n"+card
