while True:
    try:
        a=int(input('Number 1: '))
        b=int(input('Number 2: '))
        c = a + b
    except ValueError:
        print("Voce esta querendo somar letras?")
    else:
        print('O resultado é ' + str(c))