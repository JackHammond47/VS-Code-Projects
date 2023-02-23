first_age = int(input('What is the age of the first rider? '))
first_height = int(input('What is the height of the first rider? '))
second = input('Is there a second rider (yes/no)? ')
can_ride = False

if second.lower() == 'yes':
    second = True
else:
    second = False


if first_height < 36:
    can_ride = False
else:
    if not second:
        if first_height >= 62 and first_age >= 18:
            can_ride = True
        else:
            can_ride = False
    elif second:
        second_age = int(input('What is the age of the second rider? '))
        second_height = int(input('What is the height of the second rider? '))
        if second_height < 36:
            can_ride = False
        else:
            if second_age >= 18 or first_age >= 18:
                can_ride = True
            else:
                can_ride = False

if can_ride:
    print('Welcome to the ride. Please be safe and have fun!')
else:
    print('Sorry, you may not ride.')

