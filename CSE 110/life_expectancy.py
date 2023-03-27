max_life = 0
min_life = 200
max_data = []
min_data = []
choice = 'invalid'
year_of_interest = 0
country_of_interest = 'A'


while choice == 'invalid':
    choice = input('Would you like to learn more about a specific year or country (type y for year or c for country): ')
    if choice.lower() == 'y':
        year_of_interest = int(input('Enter the year of interest: '))
    elif choice.lower() == 'c':
        country_of_interest = input('Enter the country of interest: ')
    else:
        choice = 'invalid'
        print('Please type only a "y" for year or a "c" for country.')

max_life_year = 0
min_life_year = 200
max_data_year = []
min_data_year = []
year_total = 0
year_amount = 0

max_life_country = 0
min_life_country = 200
max_data_country = []
min_data_country = []
country_total = 0
country_amount = 0


with open('CSE 110/life-expectancy.csv') as life_file:
    life_file.readline()
    for line in life_file:
        line = line.strip()
        life_data = line.split(',')
        country = life_data[0]
        year = int(life_data[2])
        life_expectancy = float(life_data[3])
        if life_expectancy > max_life:
            max_life = life_expectancy
            max_data = life_data
        if life_expectancy < min_life:
            min_life = life_expectancy
            min_data = life_data
        if year_of_interest == year:
            year_total += life_expectancy
            year_amount += 1
            if life_expectancy > max_life_year:
                max_life_year = life_expectancy
                max_data_year = life_data
            if life_expectancy < min_life_year:
                min_life_year = life_expectancy
                min_data_year = life_data
        if country_of_interest.lower() == country.lower():
            country_total += life_expectancy
            country_amount += 1
            if life_expectancy > max_life_country:
                max_life_country = life_expectancy
                max_data_country = life_data
            if life_expectancy < min_life_country:
                min_life_country = life_expectancy
                min_data_country = life_data

         
print()   
print(f'The overall max life expectancy is: {max_life} from {max_data[0]} in {max_data[2]}')
print(f'The overall min life expectancy is: {min_life} from {min_data[0]} in {min_data[2]}')
print()
if choice.lower() == 'y':
    year_average = year_total / year_amount
    print(f'For the year {year_of_interest}:')
    print(f'The average life expectancy across all countries was {year_average:.2f}')
    print(f'The max life expectancy was in {max_data_year[0]} with {max_life_year}')
    print(f'The min life expectancy was in {min_data_year[0]} with {min_life_year}')
elif choice.lower() == 'c':
    country_average = country_total / country_amount
    print(f'For the country {country_of_interest}:')
    print(f'The average life expectancy across all recorded years for this country was {country_average:.2f}')
    print(f'The max life expectancy was in {max_data_country[2]} with {max_life_country}')
    print(f'The min life expectancy was in {min_data_country[2]} with {min_life_country}')



    