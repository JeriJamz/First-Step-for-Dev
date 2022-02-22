#ask for the player name
import random
print("Hi, what is your name?")
name = input()
secrectNumber = random.randint(1,25)
print('Hello ' + name + ' ,Were going to play the number game')

#ask player to make Six Guesses
for guessTaken in range(1,7):
    print("Guess what number i'm thinking of")
    guess = int(input())
    if guess < secrectNumber:
        print("You're guess is too low")
    elif guess > secrectNumber:
        print("You're guess is too high")
    else:
        break
#should be if the player guess right

if guess == secrectNumber:
    print("Good job " + name + " you guessed my number in " + str(guessTaken) + " turns")
else:
    print("nope I was thinking of " + str(secrectNumber))
          
