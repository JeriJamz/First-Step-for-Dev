#dont forget to fiinsh turtle
import turtle, pyinputplus as pyip, time,random
#time.sleep() pauses the program for some time
WIDTH,HEIGHT = 500,500#set a height and length
COLORS=['cyan','black','purple','yellow','pink','grey','salmon','green','blue','red']

screen = turtle.Screen()#makes a screen variable and sets it to the turtle screem
screen.setup(WIDTH,HEIGHT)#sets the turtle screem to the WIDTH/HEIGHT 
screen.title('Turtle Racer!!!')#gives the screen a name


def get_number_of_racers():
    racers = 0
    while True:#makes sure we get a vaild number of racers
        racers = input('Please pick betweeen 2-10 racers: ')
        if racers.isdigit():#check to see if it was a digit
            racers = int(racers)#converts number to int
        else:
            print('Your response was not a number.')
            continue#reutrns the value to the top if it isnt a number

        if 2<= racers <=10:#checks btw 2-10
            return racers
        else:
            print('Your response wasn\'t between 2 through 10')

def race():
    create_turtles(colors)

    while True:
        for racer in turtles:
            distance = randrange(1,20)
            racer.forward(distance)

            x,y = racer.pos()
            if y >= HEIGHT //2-10:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turtles=[]
    spacingx = WIDTH //(len(colors) +1)#this will space out the turtles by dividing the width by 2 for every racers
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        #need to set pos
        racer.setpos(-WIDTH//2 +(i + 1) * spacingx, -HEIGHT//2+ 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def init_turtle():
    screen = turtle.Screen()#makes a screen variable and sets it to the turtle screem
    screen.setup(WIDTH,HEIGHT)#sets the turtle screem to the WIDTH/HEIGHT 
    screen.title('Turtle Racer!!!')#gives the screen a name
           
racers = get_number_of_racers()#sets the number of racers to the users input
#print(racers)
racers = random.shuffle(COLORS)
colors = COLORS[:racers]
racer = turtle.Turtle()
#print(colors)
