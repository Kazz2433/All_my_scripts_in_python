pizza={
    'crust':'thick',
    'topping': ['queijo','4qjo'],
}
print('You ordered to '+ pizza['crust'] +' -crust pizza '+
' with the followings to:')
for i in pizza['topping']:
    print('\t'+ i)