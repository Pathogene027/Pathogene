# title

print('Exercise')

lst = []

count = 0  # counter for the number of times a user will be asked to enter a number
print(f'You will be prompted to enter 10 numbers '
      f'which are all between 1 and 12. Repetition is allowed')
while count < 10:

    numb = int(input('Enter a number between 1 and 12'))
    if numb in range(2, 12):  # what happens after he enters each number & what happens if he enters numbers within the
        # range given
        if numb > 10:
            lst.append(10)
        elif numb <= 10:
            lst.append(numb)
        count += 1
    # what happens if he enter numbers outside the range
    elif numb not in range(2, 12):
        print('Number is below or above range')

print(f'The list of numbers chosen are:\n{lst}')
