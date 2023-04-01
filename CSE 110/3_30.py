def compute_area_square(length):
    area_square = length * length
    return area_square

def compute_area_rectangle(length, width):
    area_rectangle = length * width
    return area_rectangle

def compute_area_circle(radius):
    area_circle = 3.1415 * radius * radius
    return area_circle

choice = input('What shape would like the area of? (Type "square", "rectangle", or "circle". Or type "quit" to quit.) ')
while choice != 'quit':
    if choice == 'square':
        length = float(input('What is the length of one side? '))
        area_square = compute_area_square(length)
        print(f'The area of the square is {area_square:.2f} units squared.')
    elif choice == 'rectangle':
        length = float(input('What is the length? '))
        width = float(input('What is the width? '))
        area_rectangle = compute_area_rectangle(length, width)
        print(f'The area of the rectangle is {area_rectangle:.2f} units squared.')
    elif choice == 'circle':
        radius = float(input('What is the radius? '))
        area_circle = compute_area_circle(radius)
        print(f'The area of the circle is {area_circle:.2f} units squared.')
    else:
        print('Please type "square", "rectangle", "circle" or "quit".')
    choice = input('What shape would like the area of? (Type "square", "rectangle", or "circle". Or "quit" to quit.) ')


