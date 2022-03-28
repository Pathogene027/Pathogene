Fname = input('Enter your Firstname: ')
Sname = input('Enter your Surname: ')
dayd = input('Enter the day of date of birth(eg; 05:) ')
monthd = input('Enter the month of date of birth(eg; April): ')
yeard = input('Enter the year of date of birth: ')
yeardi = int(yeard)
birthy = str(2021-yeardi)
print('My name is ' + Fname + ' ' + Sname + ' ' +
      'born on the ' + dayd + ' ' + 'of '+monthd+
      ' ' + yeard + '. Approximately, I am ' + birthy + ' ' + 'years old')