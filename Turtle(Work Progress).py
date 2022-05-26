#Turtle basics graphics
import turtle, math, random, time, sys, pyinputplus as pyip, pathlib
from pathlib import Path
#turle got 4 basics commands that i dont what the fuck they do yet
#.forward(),.back(),.left(),.right(),
win_length = 2500
win_height = 2500

turtles = 8

turtle.screensize(win_length,win_height)

class racer(object):
    def __init__(self,color,pos):
        self.pos=pos
        self.color=color
        self.turt = turtle.Turtle()
        self.turt.shape('turtle')
        self.turt.color(color)
        self.turt.penup()
        self.turt.setpos(pos)
        self.turt.setheading(90)

    def move(self):
        r = random.randrange(1,20)
        self.pos = (self.pos[0],self.pos[1] + r)
        self.turt.pendown()
        self.turt.forward(r)

    def reset(self):
        self.turt.penup()
        self.turt.setpos(self.pos)

def setupFile(name, color):
    file = open(name, 'w')
    for color in colors:
        file.write(color + ' 0 \n')
    file.close()

def startGame():
    tList = []
    turtle.clearscreen()
    turtle.hideturtle()
    colors = ['orange','yellow','red','green','blue','pink','purple','grey']
    start = -(win_length/2) + 20
    for t in range(turtles):
        newPosX = start + t*(win_length)//turtles
        tList.append(racer(colors[t],(newPosX,-230)))
        tList[t].turt.showturtle()

    run = True
    while run:
        for t in tList:
            t.move()

        maxColor = []
        maxDis = 0
        for t in tList:
            if t.pos[1] > 230 and t.pos[1] > maxDis:
                maxDis = t.pos[1]
                maxColor = []
                maxColor.append(t.color)
            elif t.pos[1] > 230 and t.pos[1] == maxDis:
                maxDis = t.pos[1]
                maxColor.append(t.color)

            if len(maxColor) > 0:
                run = False
                print('The winner is: ')
                for win in maxColor:
                    print(win)

        oldScore = []
        file = open('scores.txt', 'r+')
        for line in file:
            l = line.split()
            color = 1[0]
            score = 1[1]

        file.close()

        file = open('scores.txt', 'w')

        for entry in oldscre:
            for winner in oldScore:
                if entry[0] == winner:
                    entrey[1] = int(entry[1]) + 1

            file.write(str(entry[0]) + '' + str(entry[1]) + '\n')

        file.close()
print('Hello, would you like to play?')
response = input()
if response.lower() !='yes':
    sys.exit()
else:
    start = input('Would like to play?')



startGame()

while True:
    print('----------------------------')
    start = input('would you like play again')
    start()
    
