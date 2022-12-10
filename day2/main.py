
'''        oppenent    me
rock =       A         X
paper =      B         Y
scissors =   C         Z 

X = LOSE
Y = TIE
Z = WIN

points******

rock =       1
paper =      2
scissors =   3

win = 6
lose = 0
tie = 3
'''

part1 = False

score = 0

def winner(opponent_move, my_move):

    # ROCK LOGIC 
    if (my_move == "ROCK" and opponent_move == "SCISSORS"):
        # PLAYER WON
        return(6)
    
    elif (my_move == "ROCK" and opponent_move == "PAPER"):
        # PLAYER LOST
        return(0)

    elif (my_move == "ROCK" and opponent_move == "ROCK"):
        # PLAYER TIE
        return(3)


    # PAPER LOGIC 
    elif (my_move == "PAPER" and opponent_move == "SCISSORS"):
        # PLAYER LOST
        return(0)
    
    elif (my_move == "PAPER" and opponent_move == "PAPER"):
        # PLAYER TIE
        return(3)

    elif (my_move == "PAPER" and opponent_move == "ROCK"):
        # PLAYER WON
        return(6)



    # SCISSORS LOGIC 
    elif (my_move == "SCISSORS" and opponent_move == "SCISSORS"):
        # PLAYER TIE
        return(3)
    
    elif (my_move == "SCISSORS" and opponent_move == "PAPER"):
        # PLAYER WON
        return(6)

    elif (my_move == "SCISSORS" and opponent_move == "ROCK"):
        # PLAYER LOST
        return(0)


def move_score(my_move):

    if (my_move == "ROCK"):
        return(1)

    elif (my_move == "PAPER"):
        return(2)

    elif (my_move == "SCISSORS"):
        return(3)


def winnerPart2(opponent_move, my_move):

    # PLAYER  LOSE 
    if (my_move == "LOSE" and opponent_move == "ROCK"):
        return("SCISSORS")
    elif (my_move == "LOSE" and opponent_move =="PAPER"):
        return("ROCK")
    elif (my_move == "LOSE" and opponent_move =="SCISSORS"):
        return("PAPER")


    # PLAYER  TIE 
    elif (my_move == "TIE"):
        return(opponent_move)

    
    # PLAYER  WIN 
    elif (my_move == "WIN" and opponent_move =="SCISSORS"):
        return("ROCK")
    elif (my_move == "WIN" and opponent_move =="ROCK"):
        return("PAPER")
    elif (my_move == "WIN" and opponent_move =="PAPER"):
        return("SCISSORS")



# open input file 
file = open("input.txt", "r")
for line in file:
    # strip the new line char
    line = line.strip("\n") 

    #get the moves 
    opponent_move = line[0]
    my_move = line[2]

    # set move to words 
    if (opponent_move == "A"):
        opponent_move = "ROCK"
    elif (opponent_move == "B"):
        opponent_move = "PAPER"
    else: 
        opponent_move = "SCISSORS"

    #if solving for part 1
    if(part1 == True):
        if (my_move == "X"):
            my_move = "ROCK"
        elif (my_move == "Y"):
            my_move = "PAPER"
        else: 
            my_move = "SCISSORS"

        score += winner(opponent_move, my_move)
        score += move_score(my_move)
    else:
        if (my_move == "X"):
            my_move = "LOSE"
            score += 0
        elif (my_move == "Y"):
            my_move = "TIE"
            score += 3
        else: 
            my_move = "WIN"
            score += 6

        # 
        move = winnerPart2(opponent_move, my_move)
        score += move_score(move)

print(f"player score: {score}")

