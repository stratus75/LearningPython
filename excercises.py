def shout(phrase):
    if phrase == phrase.upper():
        return "Your're shouting"
    else:
        return "Can you speak up ?"


phrase = input('Please type in up or lower case')


def cube(number):
    return number ** 3


def by_three(number):
    # If that number is divisible by 3
    if number % 3 == 0:
        return cube(number)
    else:
        return by_three == False
