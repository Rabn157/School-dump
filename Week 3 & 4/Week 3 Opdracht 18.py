#The following while loop is meant to multiply a series of integers 
# input by the user, until a sentinel value of 0 is entered. 
# Indicate any errors in the code given. 

product = 1
num = ()

while num != 0:
    num = int(input('Enter a number: '))
    product = product * num
    print('Product = ', product)