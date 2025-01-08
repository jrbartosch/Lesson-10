num = int(input('Please Enter a Number to Calculate: '))
sum = 0
for i in range(1, num+1):
    sum += i
print (f'The sum of all the numbers from 1 to {num} is {sum}.')