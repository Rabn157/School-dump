College_credits = int(input('Enter your number of college credits: '))

if College_credits > 90:
    print('Senior status')
elif College_credits > 60:
    print('Junior status')
elif College_credits > 30:
    print('Sophmore status')
else:
    print('Freshman')