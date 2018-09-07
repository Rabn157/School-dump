# Modify the Temperature Conversion program in section 2.4.6 to convert from Celsius to Fahrenheit  instead. 
# The formula for the conversion is f = (c * 9/5) + 32. 

print('This program will convert degrees Celcius to degrees Fahrenheit')

Celcius = float(input('Enter degrees Celcius: '))

fahren = (Celcius * 9/5) + 32

print(Celcius, 'Degrees Celcius equals',
     format(fahren, '.1f'), 'degrees Fahrenheit')