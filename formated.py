def formated(pname, sname):
    fullname = pname + ' ' + sname
    return fullname.title()

while True:
    print('\nwhats your name')
    print('Press q to quit')
    vai = input('first name: ')
    if vai == 'q':
        print('Saindo...')
        break
    logo = input('last name: ')
    if logo == 'q':
        print('Saindo...')
        break
    ei = formated(vai, logo)
    print('\nOla ' + ei + ' !')
