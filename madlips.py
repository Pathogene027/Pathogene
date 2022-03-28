from datetime import date
#take user input
def whilli():
    count = 0
    while count < 3:
        name = input('Enter your name in full: ')
        dayOfbirth = input('Enter day of birth in numbers: ')
        monthOfbirth = input('Enter month of birth in numbers: ')
        yearOfbirth = input('Enter year of birth in numbers: ')
        age = 2022- int(yearOfbirth)
        favoriteColor = input('Enter your favorite color: ')
        sentence = f'''Hello {name.upper()}, welcome to our page make yourself comfortable,
choose {age} in year age limit and do not forget to customize your dashboard to {favoriteColor}'''
        print(sentence)
        count =+1
whilli()

