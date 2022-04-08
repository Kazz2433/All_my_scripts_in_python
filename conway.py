import random, copy, time

width = 60
height = 20

next_cells =[]
for x in range(width):
    column = []
    for y in range(height):
        if random.randint(0,1) == 0:
            column.append('#')
        else:
            column.append(' ')
    next_cells.append(column)

while True:
    print('\n\n\n\n\n')
    current_cells = copy.deepcopy(next_cells)

    for y in range(height):
        for x in range(width):
            print(current_cells[x][y], end='')
        print()
    
    for x in range(width):
        for y in range(height):
            leftCoord  = (x - 1) % width
            rightCoord = (x + 1) % width
            aboveCoord = (x - 1) % height
            belowCoord = (x + 1) % height

            num_neighbors = 0
            if current_cells[leftCoord[aboveCoord]] == '#':
                num_neighbors += 1
            if current_cells[x][aboveCoord] == '#':
                num_neighbors += 1
            if current_cells[rightCoord][aboveCoord] == '#':
                num_neighbors += 1
            if current_cells[leftCoord][y] == '#':
                num_neighbors += 1
            if current_cells[rightCoord][y] == '#':
                num_neighbors += 1
            if current_cells[leftCoord][belowCoord] == '#':
                num_neighbors += 1
            if current_cells[x][belowCoord] == '#':
                num_neighbors += 1
            if current_cells[rightCoord][belowCoord] == '#':
                num_neighbors += 1

            if current_cells[x][y] == '#' and (num_neighbors == 2 or 
            num_neighbors == 3):
                next_cells[x][y] = '#'
            elif current_cells[x][y] == ' 'and num_neighbors == 3:
                next_cells[x][y] = '#'
            else:
                next_cells[x][y] = ' '
        time.sleep(1)