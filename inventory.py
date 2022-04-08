stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k,v in inventory.items():
        print(str(v)+ ' ' + k) #Printing the value and key of the dic
        item_total += v #Concatening all values from dics to this var
    print("Total number of items: " + str(item_total))

display_inventory(stuff)
