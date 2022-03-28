import time

# title


print('*****************************')
print('*****************************')
print('* *                       * *')
print('* *      The Hospital     * *')
print('* *         Episode       * *')
print('* *                       * *')
print('*****************************')
print('*****************************')

# into


firstname = input('Enter your first name: ')
surname = input('Enter your surname: ')

print(f'''The weekend has been stressful. You had to work extra shifts to pay for debts.
You Mr. {firstname.capitalize()} {surname.capitalize()} but you were still unable to pay 
the loan sharks in due time.''')

time.sleep(2)

print("Now! you are all bruised and broken on a hospital bed in an unknown place. ")

time.sleep(2)

print("'How did I get here?")

time.sleep(2)

print("These guys must be nuts.")

time.sleep(2)

print("I can barely feel my legs'")

time.sleep(6)

print('KABOOOOOOOOOOMMMMMM')

time.sleep(2)

print('What the hell was that sound?')

time.sleep(2)

print("This game has only two controls 'Left(l) / Right(r) /Back(b)")

time.sleep(2)

print('''You look through your window from the ground floor
and sees a cloud of smoke moving up''')

time.sleep(2)

print('You could smell the smoke')

time.sleep(2)

print("""'Owww! God its fire, who will decide to set this 
hospital ablaze in a moment like this'""")

time.sleep(2)



def choices():
    print('''You turned to your right and sees a door that says washroom
    to your left is a small vent which obviously is a way out.
    Make a choice!''')
    choice = input('Choose which path to take out... Think carefully 😁😁😁😁😁')
    return choice.upper()


# path B and it's resultants
def pathB1():
    print('I see the fire service personnel coming towards me warding me towards an Ambulance I am safe 😪😪😪!')


def pathB2():
    print('''OMG what sort of foolish idea made me use the window. I am stuck
    Now i cannot pull myself in or out.
    Oww I feel something burning my leg HELP MEEEEEEEE!
    Game Over!!''')


def pathB():
    print('''You entered the washroom only to see a window and a water closet
    How ironic 😬. Now, I have to choose between Breaking the closet and committing suicide or
     climbing out through the window. Wait!! that wall on my left looks weak. I can break through
     ''')

    time.sleep(2)

    print('Now, I have to chose between the wall on my left and the window on my right.')

    choiceB = input('Choice between the wall on your left and the window on your right.')

    if choiceB.upper() == 'LEFT' or choiceB.upper() == 'L':
        pathB1()
    elif choiceB.upper() == 'RIGHT' or choiceB.upper() == 'R':
        pathB2()
    elif choiceB.upper() == 'BACK' or choiceB.upper() == 'B':
        print('Back to your ward!!')
        choices()


# path A and it's resultants

def pathA2():
    print('''You see group of cars parked in a park,
    you run speedily to your car and drive off''')


def pathA1():
    print('''You enters a dark clumsy looking place.
    There light in here keeps flickering. This feels like a horror movies.
    Wait did i see a gas cylinder in there?
    This place smells like LP KAAABOOOOM!!!!!!!!!! You are dead!! ''')

    time.sleep(4)

    print('Game Over')


def pathA():
    print('''You enter a dark room with two glimmers from unknown spaces 
    one on your left and the other on your right. Make a choice!''')

    time.sleep(2)

    choiceA = input('Choose which path to take out... Think carefully 😁😁😁😁😁')

    if choiceA.upper() == 'LEFT' or choiceA.upper() == 'L':
        pathA2()
    elif choiceA.upper() == 'RIGHT' or choiceA.upper() == 'R':
        pathA1()
    elif choiceA.upper() == 'BACK' or choiceA.upper() == 'B':
        print('Back to the your ward!')
        choices()


# end result

if choices() in ['LEFT', 'L']:
    pathA()
elif choices() in ['RIGHT', 'R']:
    pathB()
else:
    print('what the hell is happening?')
