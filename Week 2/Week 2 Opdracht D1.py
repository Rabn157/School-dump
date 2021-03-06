# Losing Your Head over Chess   The game of chess is generally believed to have been invented 
# in India in the sixth century for a ruling king by one of his subjects. 
# The king was supposedly very delighted with the game and asked the subject what he wanted in return. 
# The subject, being clever, asked for one grain of wheat on the first square, two grains of wheat on the second square, 
# four grains of wheat on the third square, and so forth, doubling the amount on each next square. 
# The king thought that this was a modest reward for such an invention. However, 
# the total amount of wheat would have been more than 1,000 times the current world production.    
# Develop and test a Python program that calculates how much wheat this would be in pounds, 
# using the fact that a grain of wheat weighs approximately 1/7,000 of a pound. 

# one grain of wheat on the first square
# two grains of wheat on the second square
# three grains of wheat on the third square


wheat_grain = 1
cube = 0
while cube < 64:
    wheat_grain = wheat_grain * 2
    cube += 1
    
wheat_total_pounds = (wheat_grain/ 7000)
print('The inventor will receive: ')
print(format(wheat_grain, ',.2f'), "grain's equal to", format(wheat_total_pounds, ',.2f'), 'pounds')

