import math

while True:
    # deriving the variables
    first_number = int(input('Enter your first: '))
    second_number = int(input('Enter your second: '))
    third_number = int(input('Enter your third: '))
    fourAC = 4 * (first_number * third_number)
    twoA = 2 * first_number
    dis = ((second_number ** 2) - fourAC)

    # trying the quadratic equation to handle errors
    try:
        disSqrt = math.sqrt(dis)
        numerator1 = -second_number + disSqrt
        numerator2 = -second_number - disSqrt
        denominator = 2 * first_number
        global eq1
        eq1 = (-second_number + disSqrt)/twoA
        global eq2
        eq2 = (-second_number - disSqrt) / twoA

    # checking if the function gets a zero division error
    except ZeroDivisionError:
        print('The denominator is 0 hence')
        print('The roots of the equation = 0 , 0')
    except ValueError:
        disSqrt = f'√ {dis}'
        if dis < 0:
            eq1 = f'(-{second_number} + {disSqrt}) / {twoA}'
            eq2 = f'(-{second_number} - {disSqrt}) / {twoA}'
            print(f'This quadratic, mmm has no real roots!\n'
                  f'The roots of the equation = {eq1} , {eq2}')
        elif dis > 0:
            print(f'This quadratic is amazingly an origin with real roots ...Ace!!\n'
                  f'The roots of the equation =  {eq1} , {eq2}')

    # if the equation do not meet errors
    else:
        if dis == 0:
            print(f'Wow this quadratic, has only one real root!\n'
                  f'The roots of the equation =  {eq1} , {eq2}')
        elif dis < 0:
            print(f'This quadratic, mmm has no real roots!\n'
                  f'The roots of the equation = {eq1} , {eq2}')
        elif dis > 0:
            print(f'This quadratic is amazingly an origin with real roots ...Ace!!\n'
                  f'The roots of the equation =  {eq1} , {eq2}')

    print(f'Do you want to do another calculation? \n'
          f'1. Yes or N \n'
          f'2. No or Y')
    option = input('Enter your option: ').lower()
    if option in ['1', 'yes', 'y']:
        print('Lets do it again')
        continue
    elif option in ['2', 'no', 'n']:
        print('Hello hope you come back again another time!')
        break
