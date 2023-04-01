unit = False

def calculate_windchill(temp):
    wind_speed = 5
    wind_chill = 35.47 + (0.6215 * temp) - (35.75 * (wind_speed **0.16)) + (0.4275 * temp * (wind_speed **0.16))
    print(f'At temperature {temp:.0f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F')
    while wind_speed < 60:
        wind_speed += 5
        wind_chill = 35.47 + (0.6215 * temp) - (35.75 * (wind_speed **0.16)) + (0.4275* temp * (wind_speed **0.16))
        print(f'At temperature {temp:.0f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F')

while not unit:
    temp_unit = input('Fahrenheit or Celsius (F/C)? ')
    temp_unit = temp_unit.lower()
    if temp_unit =='f' or temp_unit == 'c':
        unit = True
    else:
        print('Please type an "F" for Fahrenheit or a "C" for celsius.')
        unit = False


if temp_unit == 'f':
    temp = int(input('What is the temperature? '))
elif temp_unit == 'c':
    temp = int(input('What is the temperature? '))
    temp = temp * (9 / 5) + 32

calculate_windchill(temp)