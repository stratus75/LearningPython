# use must choose one of 2 shapes and the calcultor will give the area of the
# shape.

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()
print('just a micro second while I warn up')
print('The date is %s/%s/%s the current time is %s:%s ' % (now.month,
                                                           now.day, now.year,
                                                           now.hour,
                                                           now.minute))

# sleep the program for a specific amount of time
sleep(1)

hint = ('Dont\'t forget to include the correct units! \nExiting...')
option = input('Enter C for circle or T for triangle: ')
option = option.upper()

if option == 'C':
    radius = float(input('What is the radius of your circle: '))
    area = pi * radius**2
    print(' The pie is baking..')
    sleep(1)
    print(str('%.2f' '\n %s' % (area, hint)))
elif option == 'T':
    base = float(input('What is the base sieze of the triangle: '))
    height = float(input('What is the height of the triangle: '))
    area = base * height / 2
    print('Uni Bi Tri...')
    sleep(1)
    print('Area of the triangle is %.2f' '\n %s' % (area, hint))
else:
    print('You entered garbage, so program is exiting')
