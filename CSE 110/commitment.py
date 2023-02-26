word = 'commitment'
fav_lett = input('What is your favorite letter? ')

# for letter in word:
#     if letter.lower() == fav_lett.lower():
#         print(letter.upper(), end='')
#     else:
#         print(letter.lower(), end='')

for letter in word:
    if letter.lower() == fav_lett.lower():
        print('_', end='')
    else:
        print(letter.lower(), end='')