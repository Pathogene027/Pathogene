

def cal():
    password = '1234qwerty'
    count = 0
    while count < 3:
        user_password = input('Enter your password: ')
        if user_password == password:
            print('''Correct password
            Welcome to the page!''')
            break
        else:
            print('Incorrect password!')
        count+=1


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

cal()
print("Let's see how old you are!!" )
age()