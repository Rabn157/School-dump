print ("vul de getallen in om je gemiddelde te berekenen")
cijferPI1= int(input("cijferPI1: "))
GewichtPI1= int(input("GewichtPI1: "))
cijferPI2= int(input("cijferPI2: "))
GewichtPI2= int(input("GewichtPI2: "))
cijferPI3= int(input("cijferPi3: "))
GewichtPI3= int(input("GewichtPI3: "))

gewogentotaal = (cijferPI1*GewichtPI1 + cijferPI2*GewichtPI2 + cijferPI3*GewichtPI3)
totaalgewicht = GewichtPI1 + GewichtPI2 + GewichtPI3
eindcijfer = gewogentotaal/totaalgewicht
print ("je gemiddelde is" + eindcijfer)