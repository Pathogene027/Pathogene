import random
def numba():
    count = 0
    random_number = random.randrange(1, 6)
    while count < 3:
        userGuess = input('Guess number 1 to 5: ')
        # if count < 3: # you don't need this, you already have while loop.
        if int(userGuess) == random_number:
            print(f'''Yaay you guessed right 
            The secret number is {random_number}''')
            # User guessed it right! Stop the while loop.
            break
        elif int(userGuess) < random_number:
            print(f'''HINT
            Guessed number is less than secret number {random_number}''')
        elif int(userGuess) > random_number:
            print(f'''HINT
            Guessed number is more than secret number {random_number}''')
        else:
            print('so close yet so far!!')
        count +=1
numba()