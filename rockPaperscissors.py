# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 19:55:23 2017

@author: spook
"""

"""The program should do the following:

Prompt the user to select either Rock, Paper, or Scissors
Instruct the computer to randomly select either Rock, Paper, or Scissors
Compare the user's choice and the computer's choice
Determine a winner (the user or the computer)
Inform the user who the winner is
"""

from random import randint
from time import sleep

options = ["R", "P", "S"]
lost = ('Sorry_you_have_lost')
win = ('You_have_one')

# Steps 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,18 ,19.
def decide_winner(user_choice, computer_choice):
    print('You choose: %s ' % (user_choice))
    print('Computer selecting...')
    #sleep(1)
    print('The computer choose: %s' % (computer_choice))
    user_choice_index = options.index(user_choice)
    computer_choice_index = options.index(computer_choice)
    if computer_choice == user_choice:
        print('It is a tie')
    elif user_choice == options[0] and computer_choice == options[2]:
      print('Congradulations you win!')
    elif user_choice == options[1] and computer_choice == options[0]:
      print('Congradulations you win!')
    elif user_choice == options[2] and computer_choice == options[1]:
      print('Congradulations you win!')
    elif user_choice > 2:
      print('So you pick an invalid option')
      return  
    else:
      print('Sorry better luck next time computer won!')  
   
  
  # Steps 20
def play_RPS():
  print('Welcome to Paper, Rock, Scissors')
  user_choice = raw_input('select R for Rock, P for Paper, or S for Scissors: ')
  sleep(1)
  user_choice = user_choice.upper()
  computer_choice = options[randint(0,len(options)-1)]
  decide_winner(user_choice, computer_choice)

play_RPS()