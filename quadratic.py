import math
# creating variables
a_num = int(input('enter the "a" number: '))
b_num = int(input('enter the "b" number: '))
c_num = int(input('enter the "c" number: '))

# creating variable for complex numbers
ac4 = 4 * a_num * c_num
a2 = 2 * a_num

# creating determinant variable
det = ((b_num ** 2) - ac4)




def formular():
    if (b_num ** 2) < ac4:
        div = -b_num/a2
        answer = f'{div} + (squared root({det})/{a2})'
        print(answer)
    else:
        # creating root of det variable
        rotdet = math.sqrt(det)

        answer = ((-b_num) + rotdet) / a2
        print(answer)
    return


def formular1():
    if (b_num ** 2) < ac4:
        div = -b_num / a2
        answer = f'{div} - (squared root({det})/{a2})'
        print(answer)
    else:
        # creating root of det variable
        rotdet = math.sqrt(det)

        answer = ((-b_num) - rotdet) / a2
        print(answer)
    return

formular()
formular1()
