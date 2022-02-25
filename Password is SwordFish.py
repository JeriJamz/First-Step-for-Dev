#password is SwordFish
import random, sys, os, math

print('Do you know the password?')
response = input()
if response.lower() == 'yes':
    print('Let us continue')
else:
    print('We can not continue')
    sys.exit()

password = ''
while password != 'SwordFish':
    print('Please enter the Password')
    password = input()
print('Welcome to the ThunderDome')

print('Let play a little game of rock paper sissor')
print('are you ready?')
response1 = input()
if response1.lower() == 'yes':
    print('Lets start')
else:
    print('Well comeback when you are in a playful mood.')
    sys.exit()


print('Rock, Paper, Sissors')# this will b the title of the game
#ok this is gonna keep track of score and I dont print
wins = 0
ties = 0 
losses = 0

while True:#this should keep the game in a loop
    print('%s Wins %s Losses %s Ties' %(wins, losses, ties))#this should keep track of % of W\L\T
    while True:#ok this is for the player make sure to put this in the main game loop
        print('It is your move (r)ock, (p)aper, (s)issor, or (q)uit')
        playerMove = input()#this is where the player input matter
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break #this is where the loop breaks
        print('Please enter r,p,s')

    #this is where ima Display the player moves
    if playerMove == 'r':
        print('Rock Versus... ')
    elif playerMove == 'p':
        print('Paper Versus...')
    elif playerMove == 'S':
        print('Sissor Versus...')

    #time to for the computer turn
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('Rock')
    elif randomNumber == 2:
        computerMove = 'p'
        print('Paper')
    elif randomNumber == 3:
        computerMove = 's'
        print('Sissors')

        #this is where the player and computer interact
    if playerMove == computerMove:
        print('It\'s a tie')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You Win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You Win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You Win!')        
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You Lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You Lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You Lose!')
        losses = losses + 1
        
