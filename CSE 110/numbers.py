print('Enter a list of numbers, type 0 when finished.') 
number = int(input('Enter number: '))
numbers = []
sum = 0
amount = 0
large_num = 0

while number != 0:
    numbers.append(number)
    number = int(input('Enter number: '))
    amount += 1

for number in numbers:
    sum += number
    if number > large_num:
        large_num = number

average = sum / amount
print(f'The sum is: {sum}')
print(f'The average is: {average}')
print(f'The largest number is: {large_num}')
