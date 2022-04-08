from typing import Tuple


while True:
    a=input('Porque tu gosta de programar?')
    

    filename = 'pool.txt'

    with open(filename , 'a') as file_object:
        file_object.write(a+'\n')