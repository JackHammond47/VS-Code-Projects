word = 'fish'
num_char = '_'
guess_count = 0

while len(num_char) < len(word):
    num_char = num_char + '_'

print(f'Your hint is: {num_char}')
guess = input('What is your guess? ')

while len(guess) != len(word):
    print(f'Please guess a word with {len(word)} characters.')
    guess = input('What is your guess? ')

hint = ''
for i,letter in enumerate(word):
    if letter == guess.lower()[i]:
        hint += letter.upper()
    elif word.find(guess):
        hint += letter.lower()
    else:
        hint += '_'
    print(f'Your hint is {hint}')
    guess = input('What is your guess? ')
    
# while guess.lower() != word.lower():
#     guess_count = guess_count + 1
#     print('Your hint is: ', end='')
#     for letter in word:
#         if letter.lower() == guess.lower():
#             print(letter.lower(), end='')
#         else:
#             print('_', end='')
#     print('')
#     guess = input('What is your guess? ')
    

if guess.lower() == word.lower():
    print('Congratulations! You guessed it!')
    guess_count = guess_count + 1
    print(f'It only took you {guess_count} guesses!')