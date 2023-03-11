print('Welcome to the Shopping Cart Program!')
print('')
choice = None
cart = []
prices = []
amounts = []

while choice != '5':
    print('')
    print('Please select one of the following: ')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    choice = input('Please enter an action: ')
    if choice == '1':
        item = input('What item would you like to add? ')
        cart.append(item)
        price = float(input(f'What is the price of {item}? '))
        prices.append(price)
        amount = int(input(f'How much/many {item} do you want? '))
        amounts.append(amount)
        print(f'{amount} \'{item}\' has been added to the cart.')
    elif choice == '2':
        print('The contents of the shopping cart are: ')
        for index, item in enumerate(cart):
            print(f'{index + 1}. {amounts[index]} {item} - ${prices[index]:.2f}')
    elif choice == '3':
        item_removed = int(input('Which item would you like to remove? '))
        num_removed = item_removed - 1
        if item_removed <= len(cart):
            cart.pop(num_removed)
            prices.pop(num_removed)
            amounts.pop(num_removed)
            print('Item removed.')
        else:
            print('Sorry, that is not a valid item number.')
    elif choice == '4':
        total = 0
        for i in range(len(cart)):
            sub_total = prices[i] * amounts[i]
            total += sub_total
        print(f'The total price of the items in the shopping cart is ${total:.2f}')
    elif choice == '5':
        choice = '5'
    else:
        print('That is not a valid input. Please enter a number 1-5.')


print('Thank you. Goodbye.')