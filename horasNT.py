import datetime

print('mar = datetime.timedelta(days=0, hours=6, minutes=44, seconds=0)')
h1 = input("pls, ca estamos: ")
h2 = input("pls, combinemos: ")
h1 = eval(h1)
h2 = eval(h2)
h1 += h2
resp = int(input('Do you wanna more?(+1/0) se sim quantas X?'))
if resp != 0:
    for i in range(resp):
        h3 = input("pls, ca estamos: ")
        h3 = eval(h3)
        h1 += h3
    print(h1)
else:
    print(h1)  
