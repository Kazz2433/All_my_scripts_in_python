unprintedesign=['iphone', 'jorge', 'marcao']
complete=[]

def printmodel(unprinted, complete):
    while unprinted:
        current = unprinted.pop()

        print('printing', current)
        complete.append(current)

def show(complete):
    print('Os completos sao:')
    for i in complete:
        print(i)

printmodel(unprintedesign, complete)
show(complete)