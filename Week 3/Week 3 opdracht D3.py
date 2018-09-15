# The First-Time Home Buyer Tax Credit
# Develop and test a Python program that determines if an individual qualifies
# for a goverment First-Time Home Buyer Tax Credit of $8,000. The credit
# was only available to those that (a) bought a house that cost less than
# $800.000 (b) had a combined income of under 225,000 and (c) had not owned
# a primary residence in the last three years

print('Check to see if you qualify for the First-Time Home Buyer Tax Credit')

house_value = int(input('How much did your first house cost: '))

if house_value < 800000:
    print("You're within range for The First-Time Home Buyer Tax Credit")
else:
    print('You do not qualify for The First-Time Home Buyer Tax Credit')
    input('Press any key to stop')
    exit()

combined_value = int(input("What's your combined income: "))

if combined_value < 225000:
    print("You're within range for The First-Time Home Buyer Tax Credit")
else:
    print('You do not qualify for The First-Time Home Buyer Tax Credit')
    input('Press any key to stop')
    exit()


primary_residence = input('Did you have a primary residence in the last three years?: ')

if primary_residence == 'yes' or primary_residence == 'Yes':
    print('You do not qualify for The First-Time Home Buyer Tax Credit')
    input('Press any key to stop')
    exit()
else:
    print('You qualify for The First-Time Home Buyer Tax Credit')
    input('Press any key to stop')
    exit()