Cijfer4 = 0
Gewicht4 = 0
antwoord = 'ja'


while antwoord == 'ja' or antwoord == 'Ja':

    module = input('Selecteer een module: ')

    if module == 'B1A01':
        print('U hebt gekozen voor', module)
        #Gewicht PI's
        Gewicht1 = 1
        Gewicht2 = 3
        Gewicht3 = 2
        #invoer
        Cijfer1 = float(input('Vul het cijfer voor PI3 in: '))
        Cijfer2 = float(input('Vul het cijfer voor PI5 in: '))
        Cijfer3 = float(input('Vul het cijfer voor PI8 in: '))

    elif module == 'B1A02':
        print('U hebt gekozen voor', module)
        
        Gewicht1 = 1
        Gewicht2 = 2
        Gewicht3 = 1
        
        Cijfer1 = float(input('Vul het cijfer voor PI3 in: '))
        Cijfer2 = float(input('Vul het cijfer voor PI5 in: '))
        Cijfer3 = float(input('Vul het cijfer voor PI9 in: '))

    elif module == 'B1A03':
        print('U hebt gekozen voor', module)

        Gewicht1 = 1
        Gewicht2 = 3
        Gewicht3 = 2
        
        Cijfer1 = float(input('Vul het cijfer voor PI2 in: '))
        Cijfer2 = float(input('Vul het cijfer voor PI5 in: '))
        Cijfer3 = float(input('Vul het cijfer voor PI9 in: '))

    elif module == 'B1A04':
        print('U hebt gekozen voor', module)

        Gewicht1 = 1
        Gewicht2 = 1
        Gewicht3 = 1
        Gewicht4 = 1
        
        Cijfer1 = float(input('Vul het cijfer voor PI2 in: '))
        Cijfer2 = float(input('Vul het cijfer voor PI5 in: '))
        Cijfer3 = float(input('Vul het cijfer voor PI6 in: '))
        Cijfer4 = float(input('Vul het cijfer voor Pi9 in: '))

    elif module == 'B1A05':
        print('U hebt gekozen voor', module)
        
        Gewicht1 = 1
        Gewicht2 = 3
        Gewicht3 = 2
        
        Cijfer1 = float(input('Vul het cijfer voor PI3 in: '))
        Cijfer2 = float(input('Vul het cijfer voor PI6 in: '))
        Cijfer3 = float(input('Vul het cijfer voor PI8 in: '))
        
    elif module == 'B1A06':
        print('U hebt gekozen voor', module)
        
        Gewicht1 = 1
        Gewicht2 = 3
        Gewicht3 = 2
        
        Cijfer1 = float(input('Vul het cijfer voor PI3 in: '))
        Cijfer2 = float(input('Vul het cijfer voor PI6 in: '))
        Cijfer3 = float(input('Vul het cijfer voor PI8 in: '))
        
    elif module == 'B1A07':
        print('U hebt gekozen voor', module)
        
        Gewicht1 = 2
        Gewicht2 = 2
        Gewicht3 = 4
        
        Cijfer1 = float(input('Vul het cijfer voor PI1 in: '))
        Cijfer2 = float(input('Vul het cijfer voor PI4 in: '))
        Cijfer3 = float(input('Vul het cijfer voor PI5 in: '))
        
    elif module == 'B1A08':
        print('U hebt gekozen voor', module)
        
        Gewicht1 = 2
        Gewicht2 = 2
        Gewicht3 = 4
        
        Cijfer1 = float(input('Vul het cijfer voor PI1 in: '))
        Cijfer2 = float(input('Vul het cijfer voor PI4 in: '))
        Cijfer3 = float(input('Vul het cijfer voor PI5 in: '))
        
    elif module == 'B1A09':
        print('U hebt gekozen voor', module)
        
        Gewicht1 = 2
        Gewicht2 = 2
        Gewicht3 = 4
        
        Cijfer1 = float(input('Vul het cijfer voor PI1 in: '))
        Cijfer2 = float(input('Vul het cijfer voor PI4 in: '))
        Cijfer3 = float(input('Vul het cijfer voor PI5 in: '))
        
    elif module == 'B1A10':
        print('U hebt gekozen voor', module)
        
        Gewicht1 = 2
        Gewicht2 = 2
        Gewicht3 = 4
        
        Cijfer1 = float(input('Vul het cijfer voor PI1 in: '))
        Cijfer2 = float(input('Vul het cijfer voor PI4 in: '))
        Cijfer3 = float(input('Vul het cijfer voor PI5 in: '))
        
    elif module == 'B1B01':
        print('U hebt gekozen voor', module)
        
        Gewicht1 = 1
        Gewicht2 = 4
        Gewicht3 = 2
        
        Cijfer1 = float(input('Vul het cijfer voor PI2 in: '))
        Cijfer2 = float(input('Vul het cijfer voor PI6 in: '))
        Cijfer3 = float(input('Vul het cijfer voor PI8 in: '))
        
    elif module == 'B1S01':
        print('U hebt gekozen voor', module)
        
        Gewicht1 = 1
        Gewicht2 = 4
        Gewicht3 = 2
        
        Cijfer1 = float(input('Vul het cijfer voor PI2 in: '))
        Cijfer2 = float(input('Vul het cijfer voor PI6 in: '))
        Cijfer3 = float(input('Vul het cijfer voor PI8 in: '))
        
    elif module == 'B1D01':
        print('U hebt gekozen voor', module)
        
        Gewicht1 = 1
        Gewicht2 = 4
        Gewicht3 = 2
        
        Cijfer1 = float(input('Vul het cijfer voor PI3 in: '))
        Cijfer2 = float(input('Vul het cijfer voor PI5 in: '))
        Cijfer3 = float(input('Vul het cijfer voor PI8 in: '))
        
    else:
        print('U heeft voor een incorrecte optie gekozen')

    #berekening
    Totale_som = (Cijfer1*Gewicht1 + Cijfer2*Gewicht2 + Cijfer3*Gewicht3 + Cijfer4*Gewicht4)
    Gewichttotaal = Gewicht1 + Gewicht2 + Gewicht3 + Gewicht4

    gemiddelde = Totale_som / Gewichttotaal

    if Cijfer1 < 5.5 and gemiddelde < 5:
        gemiddelde = 5

    print('Uw gemiddelde is: ', format(gemiddelde, '.2f'))
    
    antwoord = input('Wil je nog een module berekenen?: ')