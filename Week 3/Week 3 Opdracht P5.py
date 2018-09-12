pos = 0
neg = 0
nums = 0
cont = 'yes'

while cont == 'yes' or cont == 'Yes':
    nums = int(input("Enter a Positive or Negative value: "))
    if nums > 0:
        pos += 1
        cont = (input("Do you want to continue?: "))
    elif nums < 0:
        neg += 1
        cont = (input("Do you want to continue?: "))
    elif nums == 0:
        cont == 'yes'
    
   
print('The amount of positive values entered is: ', pos, '\n' , 'The amount of negative values entered is: ', neg, sep='')