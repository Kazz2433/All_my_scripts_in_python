def collatz():
    print('Qual o numero')
    number = int(input())
    if number % 2 == 1:
        print(str(number) + 'é impar')
    else:
        print(str(number) + 'é par')

while True:
    collatz()

    