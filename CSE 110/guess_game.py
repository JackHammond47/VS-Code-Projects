import random

print('Guess a random number between 1 and 100, I will tell you if the number is higher or lower.')
number = random.randint(1, 100)
guess = int(input('What is your guess? '))
guess_count = 0

while guess < number:
    print('Higher.')
    guess = int(input('What is your guess? '))
    guess_count = guess_count + 1

while guess > number:
    print('Lower.')
    guess = int(input('What is your guess? '))
    guess_count = guess_count + 1

print('You guessed it!')
print(f' And to think it only ')