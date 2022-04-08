filename = 'learning_python.txt'

with open(filename) as file_object:
    b = file_object.readlines()

for i in b:
    a = i.rstrip()
    print(a.replace('python','C'))
