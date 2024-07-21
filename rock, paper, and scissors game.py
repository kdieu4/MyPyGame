import random
import pygame as game
while True:
    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input('rock, paper, or scissors: ').lower()

    if player == computer:
        print('Computer: ',computer)
        print('Player: ',player)
        print('Tie')

    elif player == 'rock':
        if computer == 'paper':
            print('Computer: ' + computer)
            print('Player: ' + player)
            print('You Lose!')
        if computer == 'scissors':
            print('Computer: ' + computer)
            print('Player: ' + player)
            print('You Win!')
    elif player == 'paper':
        if computer == 'scissors':
            print('Computer: ' + computer)
            print('Player: ' + player)
            print('You Lose!')
        if computer == 'rock':
            print('Computer: ' + computer)
            print('Player: ' + player)
            print('You Win!')
    elif player == 'scissors':
        if computer == 'rock':
            print('Computer: ' + computer)
            print('Player: ' + player)
            print('You Lose!')
        if computer == 'paper':
            print('Computer: ' + computer)
            print('Player: ' + player)
            print('You Win!')

    play_again = input('Do you want to play? (yes/no): ')
    if play_again == 'no':
        break
print('Thanks for playing!')