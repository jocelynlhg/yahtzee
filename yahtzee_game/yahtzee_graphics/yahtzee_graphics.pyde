a = 0
def setup():
    size(800,600)
    background(200)
    noStroke()
                 
def draw():
    background(200)
    global a
    
    a = (a + 3) % width
    noStroke()
    rect(a,200,550,110)
    fill(105)
    textSize(75)
    text("press f to start",a,275)
    fill(10,122,15,51)
    textSize(100)
    text("YAHTZEE",175,100)
    
    def dice():
        #assign 5 2D square dice a random number from 1 to 6
        roll = range(1,6)
        roll_list = ['roll',['roll1', 'roll2', 'roll3', 'roll4', 'roll5']]
        
        #assign each possible roll a 2D square dice
        dice1 = rect(x,y,50,50) and ellipse(x,y,10,10)
        dice2 = rect(x,y,50,50) and 2*(ellipse(x,y,10,10))
        dice3 = rect(x,y,50,50) and 3*(ellipse(x,y,10,10))
        dice4 = rect(x,y,50,50) and 4*(ellipse(x,y,10,10))
        dice5 = rect(x,y,50,50) and 5*(ellipse(x,y,10,10))
        dice6 = rect(x,y,50,50) and 6*(ellipse(x,y,10,10))
        
        if roll in roll_list == 1:
            print(dice1)
        elif roll in roll_list == 2:
            print(dice2)
        elif roll in roll_list == 3:
            print(dice3)
        elif roll in roll_list == 4:
            print(dice4)
        elif roll in roll_list == 5:
            print(dice5)
        elif roll in roll_list == 6:
            print(dice6)
    
    def firstRoll():
        #display first 5 random dice from roll
        if keyPressed:
            if key == '\n':
                #display 5 random dice
                pass
        
    def secondRoll():
        #display new random dice for remaining rolls
        if keyPressed:
            if key == '\n':
                #display remaining random dice
                pass
        
    def lastRoll():
        #display final random dice for remaining rolls
        if keyPressed:
            if key == '\n':
                #display remaining random dice
                pass
    
    def playGame():
        background(200)
        textSize(70)
        fill(50)
        text("first roll",250,90)
        textSize(32)
        text("press enter to roll",245,130)
        
        if keyPressed:
            if key == '\n':
                firstRoll()
    
    def score():
        #track the player's roll choices, scan for special combinations, calculate total score
        pass
        
    if keyPressed:
        if key == 'f':
            playGame()
