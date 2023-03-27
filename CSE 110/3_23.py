largest_salary = 0
smallest_salary = 99999999
job_title = input('Which job would you like to learn about?')

with open('CSE 110/hr_system.txt') as hr_file:
    for line in hr_file:
        line = line.strip()
        hr_data = line.split(' ')
        salary = int(hr_data[3])
        if job_title.lower() == hr_data[2].lower():
            if salary > largest_salary:
                largest_salary = salary
            if salary < smallest_salary:
                smallest_salary = salary

if largest_salary != 0:
    print(f'The largest salary for {job_title}\'s is ${largest_salary:.2f} and the smallest is ${smallest_salary:.2f}.')
else:
    print(f'No data was found for {job_title}')
