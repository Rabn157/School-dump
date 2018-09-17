temperature = int(input('Vul de graden in Fahrenheit: '))
humidity = int(input('Vul de vochtigheid in: '))

if temperature >= 85 and humidity > 60:
    print('Muggy day today')
elif temperature >= 85:
    print('Warm, but not muggy today')
elif temperature >= 65:
    print('Pleasant today')
elif temperature <= 45:
    print('cold today')
else:
    print('cool today')
     