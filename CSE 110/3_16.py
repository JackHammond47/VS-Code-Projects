# with open('CSE 110/books.txt') as books_file:
#     for line in books_file:
#         line = line.strip()
#         print(line)

with open('CSE 110/fruits.txt') as fruits_file:
    for line in fruits_file:
        line = line.strip()
        fruit_data = line.split(',')
        fruit_name = fruit_data[0]
        fruit_cost = float(fruit_data[2])
        print(f'{fruit_name.capitalize()} costs ${fruit_cost:.2f} per pound.')
