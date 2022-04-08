import sys


a = 'y'
while a == 'y':

    num1 = float(input('\nYour first number: '))
    num2 = float(input('Your second number: '))

    real = (num2 * 100) / num1

    print('your percent is: %.2f' %real)
    a = input('do you wanna continue?(y/n) ')