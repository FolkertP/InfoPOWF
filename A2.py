def invoer():
    naam = raw_input("Naam: ")
    return naam

def maakWoordenLijst(zin):
    startPositie = 0
    woordenLijst = []
    i = 0
    for letter in zin:
        if letter == " ":
            woordenLijst.append(zin[startPositie:i])
            startPositie = i+1
        i += 1
    woordenLijst.append(zin[startPositie:len(zin)])
    return woordenLijst

def maakNaamCode(lijst):
    naamCode = ""
    achternaam = lijst[len(lijst)-1]
    voornaam = lijst[0]
    naamCode += achternaam[0:1]
    naamCode += achternaam[len(achternaam)-1:len(achternaam)]
    naamCode += voornaam[0:1]
    return naamCode.upper()

print maakNaamCode(maakWoordenLijst(invoer()))