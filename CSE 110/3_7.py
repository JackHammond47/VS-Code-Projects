things = []
print('Please enter the items of the shopping list (type: quit to finish):')
thing = input('Item: ')

while thing != 'quit':
    things.append(thing)
    thing = input('Item: ')

print()
print('The shopping list is: ')
for thing in things:
    print(thing)

print()
print('The shopping list with indexes is:')
for i,thing in enumerate(things):
    print(f'{i}. {thing}')

print()
item_changed = int(input('Which item would you like to change? '))
new_item = input('What is the new item? ')
print()

print('The shopping list with indexes is:')
for i,thing in enumerate(things):
    if i == item_changed:
        print(f'{i}. {new_item}')
    else:
        print(f'{i}. {thing}')

# for i in range(len(things)):
#     print(f'{i}. {things[i]}')