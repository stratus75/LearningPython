"""
a program that rolls a pair of dice and asks the user to guess a number.
Based on the user's guess, the program should determine a winner.
If the user's guess is greater than the total value of the dice roll, 
they win! Otherwise, the computer wins.
"""
# Step 1 import
from random import randint
# Step 2 import
from time import sleep

# Step 3, 4, 5, 6, 7 Function
def get_user_guess():
    user_guess = int(raw_input('Guess a number: '))
    return user_guess

# Step 8, 9, 10, 11, 12, 13, 14
def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides * 2
    print('The max possible value is:' + str(max_val))
    sleep(1)
    user_guess = get_user_guess()
    if user_guess > max_val:
        print('This value is to large!')
        return #print('Now exiting program')
    else:
        print('Rolling...')
        sleep(2)
        print('This %d is your first roll' % (first_roll))
        sleep(1)
        print('This %d is your second roll' % (second_roll))
        sleep(1)
        total_roll = first_roll + second_roll
        print('The Result is ....')
        sleep(1)
        if user_guess > total_roll:
            print('You have one! dice rolled %d and your guess was %d' % (total_roll, user_guess))
            return
        else:
          print('Sorry but your guess was in correct')
          return
roll_dice(6) 