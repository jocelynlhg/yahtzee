import random

def main():
    #method holding the game play for our Yatzy game.
    #defining what we work with on the top part of the game.
    game_list_top = ['aces','twos','threes','fours','fives','sixes']
    game_list_top_values = [1,2,3,4,5,6]

    #create a player and a dice to play.
    player1 = Player('Martin')
    dice1 = Roll()

    #loop through the top part and start rolling some dice!
    for index,item in enumerate(game_list_top):

        #just one way to print info on the current rolling
        print ('-'*40)
        print ('rolling for {item}')
        print ('-'*40)

        #first roll:
        dice1.roll_dice()
        keep1 = dice1.keep_dice()

        #second roll:
        dice1.reroll_dice(keep1)
        keep2 = dice1.keep_dice()

        #third roll:
        roll3 = dice1.reroll_dice(keep2)
        dice1.forced_keep(roll3)

        #the final roll collection of dice goes in for check:
        final_roll_collection = dice1.get_kept_dice()

        print ('final roll collection: {final_roll_collection}')

        #check what the score is for this particular roll:
        check_score = dice1.single_values(final_roll_collection,game_list_top_values[index] )

        #create the key in the dictionary and add the score to the total top score.
        #this score will later determine if we get a bonus or not.
        player1.add_rolled(item , check_score)
        player1.add_top_score(check_score)

    #let's hope we get a bonus?
    player1.add_top_bonus()

    #print current score:
    player1.print_scoreboard()
    
class Roll:
    def init_(self):
        #class holding all the dice functionality for rolling the dice, but also checking dice values for the gameplay
        self.current_dice_list = []
        self.current_kept_dice = []
        
    def roll_dice(self):
        #initial roll
        #function that allows users to keep the dice that they want
        #method function returning a dice list with random values between 1 to 6 like a die would function in real life. returns list
        
        self.current_kept_dice = []
        self.current_dice_list = [random.randint(1,6) for die in range(0,5)]
        print('you rolled {self._current_dice_list} ! \n')
        return self.current_dice_list
        
    
    def reroll_dice(self,dice_list):
         
        #method function returning current dice list just like the initial roll.
        #This time it uses the returned list after the player keeps some dice.
        #(This could probably be refactored into roll so roll and reroll are the same, but with different arguements.)
        #reroll whatever dice list is passed
        self.current_dice_list = [random.randint(1,6) for die in range(0, len(dice_list))]
        print('you rolled {self._current_dice_list} ! \n')
        return self.current_dice_list
        
    def keep_dice(self):
        #method function returning a dice list to reroll.
        #It also stores the dice you want to keep in a separate keep list.
        keep_input = input('which dice do you want to keep (comma separated: e.g. 1,1,5? ')
        split_input = keep_input.split(',')
        
        #if user types nothing, keep all:
        if keep_input == '':
            return self.current_dice_list
        split_input_int = [int(item) for item in split_input]
        
        for die in split_input_int:
            self.current_kept_dice.append(die)
        
        #cycle through list user wants to keep for value in split_input)int:
            if value in self.current_dice_list:
                self.current_dice_list.remove(value)
        return self.current_dice_list
        
    def get_current_dice(self):
        #return the current dice list
        return self.current_dice_list
        
    def get_kept_dice(self):
        #return the current kept dice list
        return self.current_kept_dice
        
    def forced_keep(self,dice_list):
        #last roll is forced
        #third time player rolls a die or dice, it must be added to the list
        for die in dice_list:
            self.current_kept_dice.append(die)
        
    def check_one_pair(self,dice_list):
        #function check if there are at least two equal dice in the dice list, updates score, and returns bool
        dice_list.sort()
        if dice_list[0] == dice_list[1] or dice_list[1] == dice_list[2] or dice_list[2] == dice_list[3] or dice_list[3] == dice_list[4] or dice_list[0] == dice_list[2] or dice_list[0] == dice_list[3] or dice_list[0] == dice_list[4] or dice_list[1] == dice_list[3] or dice_list[1] == dice_list[4] or dice_list[2] == dice_list[4]:
            return True
        return False
        
    def check_two_pairs(self,dice_list):
        #function checks if there are two pairs in the dice list, updates school, and returns bool
        dice_list.sort()
        if (dice_list[0] == dice_list[2] and dice_list[2] == dice_list[3]) or (dice_list[0] == dice_list[1] and dice_list[3] == dice_list[4]) or (dice_list[1] == dice_list[2] and dice_list[3] == dice_list[4]):
            return True
        return False
        
    def check_three_kind(self,dice_list):
        #checks if there are at least three identical dice in the dice list, updates scores, returns bool
        dice_list.sort()
        if dice_list[0] == dice_list[1] or dice_list[1] == dice_list[3] or dice_list[2] == dice_list[4]:
            return True
        return False
        
    def check_four_kind(self,dice_list):
        #function checks if there are at lease four equal dice in the dice list, updates score, returns bool
        dice_list.sort()
        if dice_list[0] == dice_list[3] or dice_list[1] == dice_list[4]:
            return True
        return False
        
    def check_low_straight(self,dice_list):
        #function checks if the dice in the dice list are in sequence 1-5, updates score, returns bool
        dice_list.sort()
        if len(set(dice_list)) == 5 and dice_list[4] == 5 and dice_list[0] == 1:
            return True
        return False
        
    def check_high_straight(self,dice_list):
        #function checks if the dice in the dice list are in sequence 2-6, updates score, returns bool
        dice_list.sort()
        if len(set(dice_list)) == 5 and dice_list[4] == 6 and dice_list[0] == 2:
            return True
        return False
        
    def check_full_house(self,dice_list):
        #function checks if the dice are two equal plus three equal in the dice list, updates score, returns bool
        #sorting the list makes it easier to check items against eachother
        dice_list.sort()
        #if the set representation of the list is 2, there is a possible full house
        if (len(set(dice_list))) != 2:
            return False
        #to differentiate it from four of a kind we check this:
        elif dice_list[0] != dice_list[3] or dice_list[1] != dice_list[4]:
            return True
        return False
        
    def add_chance(self,dice_list):
        #function updates the score with the sum of the dice list, and returns bool
        pass
        
    def check_yahtzee(self,dice_list):
        #function checks if all the dice in the dice list are equal, updates score, and returns bool
        if len(set(dice_list)) == 1:
            return True
        return False
        dices = Roll()
        print('is it yahtzee? {dices.check_yahtzee([1,1,1,1,1]}')
    
    def check_single_value(self,dice_list,check_value):
        roll_score == 0
        for die in dice_list:
            if die == check_value:
                roll_score += die
        return roll_score
    
    def keep_dice(self):
        #method function returning a dice list to reroll. also stores the dice player wants to keep in a separate keep list and returns list
        keep_input = input('which dice do you want to keep (comma separated: e.g. 1,1,5)? ')
        split_input = keep_input.split(',')
        if keep_input == '':
            return self.current_dice_list
        split_input_int = [int(item) for item in split_input]
        for die in split_input_int:
            self.current_kept_dice.append(die)
            
        #cycle through list user wants to keep
        for value in split_input_int:
            if value in self.current_dice_list:
                self.current_dice_list.remove(value)
        return self.current_dice_list
    
class Player:
    def __init__(self, name):
       #method holding all player data like name and all the scores.
        self.name = name
        self.scoreboard = {}

        self.top_score = 0
        self.bottom_score = 0
        self.bonus_bottom = 0
        self.total_score = 0

    def add_rolled(self, rolled_type , value):
        #method adding scores to the player scoreboard
        self.scoreboard[rolled_type] = value

    def add_top_score(self,value):
        #method adding a rolled score to the top part score.
        self.top_score += value

    def add_top_bonus(self):
        #method that checks for top part score. If it is high enough, a bonus is added to the scoreboard.
        #keep this a variable for easy updates.
        needed_score_for_bonus = 63

        if self.get_top_score() >= needed_score_for_bonus:
            self.scoreboard['top_bonus'] = 50
        else:
            self.scoreboard['top_bonus'] = 0

        self.top_bonus = self.scoreboard['top_bonus']

    def get_top_score(self):
        #method function returning current top part score
        return self.top_score

    def print_scoreboard(self):
        #method printing all the values in the scoreboard.
        for key, value in self.scoreboard.items():
            print ('{key} : {value}')
            
#import random
#from player import Player
#from roll import Roll

main()
                            
              
