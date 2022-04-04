
number_of_days = []
numb = input('How many days do you want to add up?: ')
for i in range(int(numb)):
    count = int(input('Enter a number and wait for prompt: '))
    number_of_days.append(count)
print('The total of the attendance is ' , sum(number_of_days))
divisor = len(number_of_days)
average = (sum(number_of_days))/divisor
print('The average attendance is ', average)
