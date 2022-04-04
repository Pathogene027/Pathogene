count = float('inf')
while count > 0:
    password = '1234qwerty'
    user_password = input('Enter your password: ')
    if user_password == password:
        print('''Correct password
        Welcome to the page!''')
    else:
        print('Incorrect password!')
        continue


    def age():
        age = int(input('Enter your age please! '))
        if age <= 17:
            print('You are an adolescent woow!')
        elif 17 < age < 40:
            print('''Do you know you can drink any alcohol you want?
            Hell you are a youth and an Adult!''')
        elif 40 <= age < 60:
            print('Hello Dad how are the kids?')
        elif 60 <= age < 100:
            print('You leaved a life worth celebrating!')
        else:
            print('Hello Methuselah!')
    print("Let's see how old you are!!")
    age()
    print(f'Do you want to continue \n'
          f'Yes(y) or No(n)?')
    ask = input('Enter your choice here').lower()

    if ask in ['yes', 'y']:
        print('Here we go again')
        continue
    elif ask in ['no', 'n']:
        print('Aureviore Friend!')
        SystemExit()
    else:
        print('Hello make a good choice!')
    count += 1