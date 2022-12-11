#JSA
import sys, time

def dprint(c):
    for s in c:
        sys.stdout.write(s)
        sys.stdout.flush()
        time.sleep(.5)

def qdprint(c):
    for s in c:
        sys.stdout.write(s)
        sys.stdout.flush()
        time.sleep(.25)
        
def fprint(c):
    for s in c:
        sys.stdout.write(s)
        sys.stdout.flush()
        time.sleep(.05)
def ffprint(c):
    for s in c:
        sys.stdout.write(s)
        sys.stdout.flush()
        time.sleep(.05)


qdprint('.... \n')
qdprint('|....Lo')
fprint('ading ........... \n')
fprint('|Loaded| \n')
choice = input('Would you like to hear the announcemts. Yes or no? \n')

if choice == 'No':
    print('We will save the good news for next time')
    sys.exit()
elif choice == 'Yes':
    dprint('Let us begin the annoucements \n')
    pass
else:
    fprint('I cannont register that input \n')

ffprint(''' Just a couple of new things. Python is moving along great. An interpid lingo based\n
As you see C is under construction and soon enough X86 will be too. As far as the game is going... \n
Wait on it. It is the best I can tell you.
''')
