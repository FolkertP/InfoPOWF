def invoer():
    invoerLijst = []
    nieuweWaarde = 1
    while nieuweWaarde != 0:
        nieuweWaarde = input()
        invoerLijst.append(nieuweWaarde)
    return invoerLijst[0:len(invoerLijst)-1]

def zitErEenZevenIn(getal):
    for letter in str(getal):
        if letter == "7":
            return True
    return False

def zevenachtig(lijst):
    zevenachtigLijst = []
    for getal in lijst:
        if getal % 7 == 0 or zitErEenZevenIn(getal):
            zevenachtigLijst.append(getal)
    return len(zevenachtigLijst)

print zevenachtig(invoer())