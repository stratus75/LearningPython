def distance_from_zero(foo):
    if type(foo) == int or type(foo) == float:
        return abs(foo)
    else:
        return 'Nope'
        print(distance_from_zero(foo))


distance_from_zero(0.5)
distance_from_zero(5)


def answer():
    x = int(input('Enter the number four and two: '))
    if x == int and 42:
        return True
        print(x)
    else:
        return 'Please try again.'
    answer()


def rental_car_cost(days):
    cost = days * 40          # Number of days rented + the daily rate.
    if days >= 7:           # If rented more than 7 days $50 discount
        cost - 50
        return cost
    elif (days > 3) - 20:           # If rented more > 3 but < 7 $20 discount
        return cost
