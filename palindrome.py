import random
import sys
import time

compl = ['Hello', 'Hey', 'Big Brain', 'Hey Einstein']  # complimentary words for a correct word
com = random.choice(compl)
compl1 = ['Boo', 'Sugar Plum', 'Candy']  # complimentary words for a wrong word
com1 = random.choice(compl1)
while True:
    getinput = input('Enter a palindrome word!: ')  # taking user input and storing it in a variable
    lists = getinput[::-1]  # reversing the input
    if getinput == lists:  # condition for execution if the word is a palindrome
        print(com, ' your word is a palindrome Hurrayy!\n',getinput, ' ==> ', lists)
        print()
    else:  # condition for execution if the word is not a palindrome
        print(com1, ' you need to stop missing english classes!\n',getinput, ' ==> ', lists)

    print('Do you want to continue?\nYes(y) or No(n)')
    option = input('Make a choice: ').lower()
    if option in ['yes','y']:
        print('Lets do this again')
    elif option in ['no', 'n']:
        print('See you later...')
        time.sleep(2)
        sys.exit()
