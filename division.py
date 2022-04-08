print('Give me two numbers, and i"ll divde them')
print('Enter "q" to quit')

while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break
    second_number = input('Second number: ')
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('You cant divide any number by 0')
    else:
        print(answer)


"""
try:
    print(5/0)
except ZeroDivisionError:
    print('You cant divide by zero!')
"""
