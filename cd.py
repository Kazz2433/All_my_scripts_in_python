filename = 'moby_dick.txt'

with open(filename) as f_obj:
    contents = f_obj.read()

b = contents.split()
c = b.count('the') 
print(c)
