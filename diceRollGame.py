# -*- coding: utf-8 -*-
"""
a program that rolls a pair of dice and asks the user to guess a number. Based
on the user's guess, the program should determine a winner. If the user's 
guess is greater than the total value of the dice roll, they win! Otherwise, 
the computer wins.
"""
# Step 1 import
from random import randint
# Step 2 import
from time import sleep

# Step 3, 4, 5, 6, 7 Function
def get_user_guess():
 user_guess =  int(raw_input('Guess a number: '))
 return user_guess

# Step 8, 9, 10, 11, 12, 13, 14
def roll_dice(number_of_sides):
    first_roll = radiant(1, number_of_sides)
    second_roll = radiant(1, number_of_sides)
    max_val = number_of_sides * 2
    print('The max possible value is' + str(max_val))
    sleep(1)
    get_user_guess(user_guess)
    if user_guess > max_val:
      print('This value is to large!')

