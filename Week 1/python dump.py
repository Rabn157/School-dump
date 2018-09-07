cijfer1 = 5
cijfer2 = 10
cijfer3 = 7
Weging1 = 3
Weging2 = 2
Weging3 = 3
uitkomst = 0
Totaleuitkomst = 0


def gemiddelde():
    uitkomst = (cijfer1*Weging1 + cijfer2*Weging2 + cijfer3*Weging3)
    totaleweging = Weging1 + Weging2 + Weging3
    Totaleuitkomst = uitkomst/totaleweging
    print (uitkomst)
    print (Totaleuitkomst)


gemiddelde()