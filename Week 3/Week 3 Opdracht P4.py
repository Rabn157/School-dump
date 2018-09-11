#input value moet tussen 0 - 100 zitten



print('The maximum value is 100')
num1 = float(input('Vul het eerste getal in: '))

while num1 < 0 or num1 > 100:
    num1 = float(input('Vul het eerste getal in: '))

num2 = float(input('Vul het tweede getal in: '))

while num2 < 0 or num2 > 100:
    num2 = float(input('Vul het tweede getal in: '))

num3 = num1 + num2

print(num1, '+', num2, '=', num3, sep='')



