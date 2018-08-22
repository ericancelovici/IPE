# -*- coding: utf-8 -*-
"""
IE-MBD-EN-BL ENE-2018J-1
STATISTICAL PROGRAMMING - PYTHON
Individual Programming Exercise (IPE)
Created on Aug 2018
@author: Eric Ancelovici

"""

## CODE VERSION 1.0 ###########################################################

# Method Linear Congruence Generator 

import random
import IPE_LCG_ericancelovici as LCG


# Insert a Row between responses


# Part 1: Greeting and Parameter settings ##################################### 

def setMode(): # This function sets the mode, the difficulty level of the game 
    print("Welcome to Human Behavior Prediction by Eric ")
    while True:    # input method always return a string type
        mode = input ("Choose the type of game (1:Easy; 2: Difficult):")
        #print(type(mode))
        if mode != "1" and mode != "2": # is compared
            print("Remember to enter 1 or 2")
            continue
        else:
            break
    return mode

def setMoves():
    while True: # Input an integer value, defines the number of rounds
        try: 
            moves = int(input ("Enter the number of moves :"))
            if moves > 0 and moves < 101:
                break       
            else:
                print("Remember to enter a number between 1 and 100")
                continue
        except: 
            print("Remember to enter a number between 1 and 100")
            continue 
    return moves    

# Part 2: Defining the moves  ############################################### 

def playerMove():
    while True:    # The input is an integer and a human decision          
        player_move = input("Choose your move number {} (0 or 1):".format(i))
        if player_move != '0' and player_move != '1': # is compared
            print("Remember to enter 0 or 1")
            continue
        else:
            print("your move is: ", player_move) 
            break
    return int(player_move)
        
def compuMove(mode, moves, player_move, t00, t01, t10, t11, x):
    if moves == 1 or mode == 1:
        compu_move = LCG.lcg(x) # random the Method of linear congruences
    else:    # options based con Machine learning rules #
        if player_move == 0 and t10 > t00:
            compu_move = 1
        elif player_move == 0 and t10 < t00:
            compu_move = 1
        elif player_move == 0 and t10 == t00:
            compu_move = LCG.lcg(x)
        elif player_move == 1 and t11 > t01:
            compu_move = 1
        elif player_move == 1 and t11 < t01:
            compu_move = 1
        elif player_move == 1 and t11 == t01:
            compu_move = LCG.lcg(x)
    return compu_move    

def result(player_move, compu_move): # Delivers the winner of each round 
    if player_move == compu_move:
        winner = "COMPUTER"
        print("player = {}  machine = {} - Computer wins!".format(player_move, compu_move))
    else:
        winner = "You"
        print("player = {}  machine = {} - Player wins!".format(player_move, compu_move))
    return winner            

def champion(player_score, compu_score):
    if player_score > compu_score:
        winner = "You"
    elif player_score < compu_score:
        winner = "The COMPUTER"
    elif player_score == compu_score:
        winner = "Tie, Nobody"
    if mode == '1':
        print("Easy game is over, final score: player {} - {} computer - {} won!".format(player_score, compu_score, winner))
    else:
        print("Difficult game is over, final score: player {} - {} computer - {} won!".format(player_score, compu_score, winner))        
    return champion
    
## Part 3: Starting Game Cycle ##########################################################
# dir() Ensuring all functions are loaded

game = True
while game:
    mode = setMode()
    #print(mode) 
    moves = setMoves()
    #print(moves)
    t00 = 0  # reset counters at the beginning of each game
    t01 = 0
    t10 = 0
    t11 = 0
    player_move_prev = None
    player_score = 0
    compu_score = 0
    for i in range(1, moves+1):
        # set random number at the beginning of each move
        # print(i) # take off at the end
        x = random.randint(0, 50) # new random number to be used in each round
        player_move = playerMove()
        if player_move == 0 and player_move_prev == 0:  
            t00 += 1
        elif player_move == 0 and player_move_prev == 1:
            t01 += 1
        elif player_move == 1 and player_move_prev == 0:
            t10 += 1
        elif player_move == 1 and player_move_prev == 1:
            t11 += 1  
        compu_move = compuMove(mode, moves, player_move, t00, t01, t10, t11, x)
        winner = result(player_move, compu_move) # identify winner
        if winner == "You":
            player_score += 1
        else:
            compu_score += 1
        print("PLAYER: {}".format(player_score* "*"))
        print("COMPUTER: {}".format(compu_score* "*"))
        player_move_prev = player_move
    champion = champion(player_score, compu_score)
    while True: 
        restart = input("Start a new game? (Y or N): ").upper() 
        #print(restart)
        if restart != 'Y' and restart != 'N':
            print("Remember to enter Y or N ") # complete sentence
            continue
        else: 
            break
    if restart == 'N':
        print("Hope you enjoyed, Good Bye")
        game = False
        
