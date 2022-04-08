import sys
import random

wins = 0
losses = 0
ties = 0

while True:
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or 'p' or 's':
            break
        print("type one of r,p,s or q")

    if playerMove == 'r':
        print('Rock VERSUS...')
    elif playerMove == 'p':
        print('papel VERSUS...')
    elif playerMove == 's':
        print('scissors VERSUS...')

    random_number = random.randint(1,3)
    if random_number == 1:
        computer_move = 'r'
        print('rock')
    
    if random_number == 2:
        computer_move = 'p'
        print('paper')
    
    if random_number == 3:
        computer_move = 's'
        print('scissor')

    if playerMove == computer_move:
        print("TIE")
        ties += 1
    elif playerMove == 'r' and computer_move == 's': 
        print('You win!') 
        wins = wins + 1 
    elif playerMove == 'p' and computer_move == 'r': 
        print('You win!') 
        wins = wins + 1 
    elif playerMove == 's' and computer_move == 'p': 
        print('You win!') 
        wins = wins + 1 
    elif playerMove == 'r' and computer_move == 'p': 
        print('You lose!')
        losses = losses + 1 
    elif playerMove == 'p' and computer_move == 's': 
        print('You lose!') 
        losses = losses + 1 
    elif playerMove == 's' and computer_move == 'r': 
        print('You lose!') 
        losses = losses + 1