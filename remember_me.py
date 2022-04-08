import json

def get_storae_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input('Whats your name? ')
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username,f_obj)
    print('We will come back to you '+ username)
    return username


def greet_user():
    username = get_storae_username()
    a = input("Your name is "+ username+' right?')
    if a == 'n':
        get_new_username()
    else:
        print('welcome back'+ username)

greet_user()