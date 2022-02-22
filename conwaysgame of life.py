#so side note on a graph the chart works x =Left,Right y= up,down. ya know jus alil reminder.
#this is activity for list. but were playing conway's game of life
import random, time, copy
WIDTH = 60
HEIGHT = 20


#create a list of list for the cells

nextCells = []
for x in range(WIDTH):
    column = []# so this creates a new coumn
    for y in range(HEIGHT):
        if random.randint(0,1)==0:
            column.append('#')#add a living cells
        else:
            column.append(' ')#add a dead cell
    nextCells.append(column)#next cells is a list of column list\

while True:#main programn loop
    print('\n\n\n\n\n')#seprate each step with newlines
    currentCells = copy.deepcopy(nextCells)

#wanna makw sure that currentCells are being printed on the screen while new ones are being generated
    for y in range(HEIGHT):
        print(currentCells[x][y], end='')#print the # or space
    print()#this will print a newline at the end of the row.


#calculare the next step's cells based on current step's cells:
    for x in range(HEIGHT):
        #getting neighbors coordinates:
        #`% WIDTH` EBSURES leftcoord is alwats between 0 and WIDTH  -1
        leftCoord = (x - 1)%WIDTH
        rightCoord = (x + 1)%WIDTH
        aboveCoord = (y - 1)%HEIGHT
        belowCoord = (y + 1)%HEIGHT

        #OK NOW its time to count the living neighbors
        numNeighbors = 0
        if currentCells[leftCoord][aboveCoord] == '#':
            numNeighbors +=1 # this means if the top left neighbor is alive
        if currentCells[x][aboveCoord] == '#':
            numNeighbors +=1#thats for if the top neighbor is alive
        if currentCells[rightCoord][aboveCoord] == '#':
            numNeighbors +=1# thats for the top right neighbor
        if currentCells[leftCoord][y] == '#':
            numNeighbors +=1# thats for the left neighbor is alive
        if currentCells[rightCoord][y] == '#':
            numNeighbors +=1#thats for the right neighbor
        if currentCells[leftCoord][belowCoord]=='#':
            numNeighbors +=1#that's for the bottem left
        if currentCells[x][belowCoord] =='#':
            numNeighbors +=1# for the neighbor below is alive
        if currentCells[rightCoord][belowCoord] =='#':
            numNeighbors +=1#thats for bottem right neighbors


        #ok time now to set the logic that the cells will follow
        if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
            #living cells with 2 or 3 neighbors alive:
            nextCells[x][y] = '#'
        else:
            #this line should make it where everthing dies or stay dead:
            nextCells[x][y] = ' '
        time.sleep(1)#this module is what gives the game a second break before it makes it next steps
