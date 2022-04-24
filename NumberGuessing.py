import random, sys, time


# function to for printing a sentence slowly
def impress(text, delay):
    for t in text:
        sys.stdout.write(t)  # type in line an element of the text
        sys.stdout.flush()
        time.sleep(delay)  # delay


# function for printing a element of a list slowly
def complim(text):
    for comp in random.choice(text):
        for i in comp:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.1)
    print('\n')


# printing title
title = 'Number Guessing Game'
titleline = 5 * '*'

impress(title, delay=0.2)
impress(titleline, delay=0.1)



addressing = '''Welcome to the guessing game,
the roulette has been spun'''
comple = ['Heyyo! You are a magician.', 'Genius well done', 'Christ he just made a miracle']
check = True
check1 = True
while check:
    print('\n')
    name = input('Enter your name: ').capitalize()
    welc = f'Hello {name}'
    impress(welc, delay=0.1)

    print('\n')
    impress(addressing, delay=0.1)  # running the impress function with the addressing variable

    # loop for running program
    while check1:
        check2 = True
        while check2:
            # creating essential variables
            count = 0
            container = random.randint(2, 9)  # the randomint with interval
            while count < 3:
                # essential variables for the loop
                countsolve = 2 - count
                complet = [f"Merhn guessing is hard!! You've got {countsolve} more chances",
                           f'Quit dear one, QUIT 😂😂😂 {countsolve} more chances!',
                           f'Doing great {countsolve} more chances!']

                userinput = int(input('\nGuess a number between 1 and 10: '))  # take user input and convert to integer for comparison
                # comparing user input to the randint variable
                if userinput == container:
                    complim(comple)
                    break
                else:
                    # hints
                    if userinput < container:
                        print('Guess is less than the secret number ')
                    elif userinput > container:
                        print('Guess is more than secret number')
                    complim(complet)
                    count += 1
            break
        # option to quit or continue
        print('\nContinue?\nChoose Yes(y) or No(n)')
        opt = input('Make a choice!')

        if opt.lower() in ['yes', 'y']:
            pass

        elif opt.lower() in ['no', 'n']:
            sab = 'See you again Bruv!'
            qu = 'Quiting...'
            impress(sab, delay=0.1)
            print('\n')
            impress(qu, delay=0.1)
            sys.exit()
        else:
            pass
