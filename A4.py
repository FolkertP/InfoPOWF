
stapel = [121,2222,2211,54245,453425,23234,234,2,234124,34214,43545,3278654,876,4546,32345,2342354,2,89,71,3,4,5,121,32,84,91,54,42,33,103,71]
resultaten = []
stop = False

def maakSubStapel():
    subStapel = []
    if len(stapel) >= 10:
        lengte = 10
        stop = False
    else:
        lengte = len(stapel)
        stop = True
    for i in range(0,lengte):
        subStapel.append(stapel[i])
    return (subStapel, stop)

def kiesHoogste(subStapel):
    hoogsteWaardering = 0
    for i in range(0,len(subStapel)):
        if subStapel[i] > hoogsteWaardering:
            hoogsteWaardering = subStapel[i]
    return hoogsteWaardering

def verwijderBovenste(hoogsteWaardering, subStapel, stapel):
    locatie = stapel.index(hoogsteWaardering)

    for i in range(0, locatie+1):
        stapel.pop(0)
    return stapel

def voegResultaatToe(hoogsteWaardering):
    resultaten.append(hoogsteWaardering)

while stop != True:
    subStapel, stop = maakSubStapel()
    hoogste = kiesHoogste(subStapel)
    voegResultaatToe(hoogste)
    stapel = verwijderBovenste(hoogste, subStapel, stapel)
    print resultaten