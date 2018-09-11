num1 = (0)
num2 = (0)
num3 = (0)

print('The maximum value is 100')

while num1 >= 0 and num1 <= 100 and num2 <= 100:
    num1 = float(input('Enter the first number: '))
    if num1 <= 100:
        print('Wrong number')
    else:
        num2 = float(input('Enter the second number: '))
        print('Wrong number')
    if num2 <= 100:
        num3 = num1 + num3
        print(num1, '+', num2,'=',num3,sep='')

