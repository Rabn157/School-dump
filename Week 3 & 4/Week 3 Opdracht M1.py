print('This program will convert temperatures (Celcius-Fahrenheit / Fahrenheit-Celcius)')
print('Enter (F) to convert Fahrenheit to Celcius')
print('Enter (C) to convert Celcius to Fahrenheit')

which = input('Enter selection: ')

while which != 'F' and which != 'C' and which != 'f' and which != 'c':
    which = input("Please enter 'F' or 'C': ")

temp = float(input('Enter temperature to convert: '))


if which == 'F' or which == 'f':
    while temp < -459.67:
        temp = float(input('Enter temperature to convert: '))
    converted_temp = format((temp - 32) * 5/9, '.2f')
    print(temp, 'degrees Fahrenheit equals', converted_temp, 'degrees celcius')
else:
    while temp < -273.15:
        temp = float(input('Enter temperature to convert: '))
    converted_temp = format((9/5 * temp) + 32, '.2f')
    print(temp, 'degrees Celcius equals', converted_temp, 'degrees Fahrenheit')    