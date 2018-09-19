module = input('Selecteer een module: ')

if module == 'B1A01':
    print('U hebt gekozen voor', module)
    
    Gewicht1 = 1
    Gewicht2 = 3
    Gewicht3 = 2
    
    Cijfer1 = float(input('Vul het cijfer voor PI3 in: '))
    Cijfer2 = float(input('Vul het cijfer voor PI5 in: '))
    Cijfer3 = float(input('Vul het cijfer voor PI8 in: '))
    
    Totale_som = (Cijfer1*Gewicht1 + Cijfer2*Gewicht2 + Cijfer3*Gewicht3)
    Gewichttotaal = Gewicht1 + Gewicht2 + Gewicht3

    gemiddelde = Totale_som / Gewichttotaal

    if Cijfer2 < 5 and gemiddelde > 5:
        gemiddelde = 5

    print('Uw gemiddelde is: ', format(gemiddelde, '.2f'))

elif module == 'B1A02':
    print('U hebt gekozen voor', module)
elif module == 'B1A03':
    print('U hebt gekozen voor', module)
elif module == 'B1A04':
    print('U hebt gekozen voor', module)
elif module == 'B1A05':
    print('U hebt gekozen voor', module)
elif module == 'B1A06':
    print('U hebt gekozen voor', module)
elif module == 'B1A07':
    print('U hebt gekozen voor', module)
elif module == 'B1A08':
    print('U hebt gekozen voor', module)
elif module == 'B1A09':
    print('U hebt gekozen voor', module)
elif module == 'B1A10':
    print('U hebt gekozen voor', module)
elif module == 'B1B01':
    print('U hebt gekozen voor', module)
elif module == 'B1S01':
    print('U hebt gekozen voor', module)
elif module == 'B1D01':
    print('U hebt gekozen voor', module)
else:
    print('U heeft voor een incorrecte optie gekozen')
    