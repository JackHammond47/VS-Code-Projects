print('Welcome to the Shopping Cart Program!')
print('')
choice = 0
cart = []

while choice != 5:
    print('')
    print('Please select one of the following: ')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    choice = int(input('Please enter an action: '))
    if choice == 1:
        item = input('What item would you like to add? ')
        cart.append(item)
        print(f'\'{item}\' has been added to the cart.')
    elif choice == 2:
        print('The contents of the shopping cart are: ')
        print(cart)
    elif choice == 3:
        print('I will add this soon.')
    elif choice == 4:
        print('I will add this soon.')
    
    

   




print('Thank you. Goodbye.')