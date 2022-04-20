import time

three = 3 #factor 3
five = 5 #factor 5
mult3 =[]
mult5 =[]
mult35 = []
#iteration from 1 to 50
print('Numbers Divisible by only three are;')
for i in range(1, 51):
    if i % three == 0 and i % five != 0:#test for numbers divisible by three only
        mult3.append(i)#drop the factor which qualifies into the mult3 list
        print(i, ' ==> Fizz')
        time.sleep(1)
lens3 = len(mult3)
time.sleep(1)
print('There are ', lens3, ' numbers divisible by three only in the range\n')
time.sleep(1)


print('Numbers Divisible by only five are;')
time.sleep(1)
for i in range(1, 51):
    if i % five == 0 and i % three != 0:#test for numbers divisible by five only
        mult5.append(i)#drop the factor which qualifies into the mult5 list
        print(i, ' ==> Buzz')
        time.sleep(1)
lens5 = len(mult5)
time.sleep(1)
print('There are ', lens5, ' numbers divisible by five only in the range\n')
time.sleep(1)

print('Numbers Divisible by only five and three;')
time.sleep(1)
for i in range(1, 51):
    if i % five == 0 and i % three == 0:#test for numbers divisible by both three and five
        mult35.append(i)#drop the factor which qualifies into the mult35 list
        print(i, ' ==> FizzBuzz')
        time.sleep(1)
lens35 = len(mult35)
time.sleep(1)
print('There are ', lens35, ' numbers divisible by both three and five in the range\n')
