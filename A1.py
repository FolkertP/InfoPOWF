def halter(n):
    if not 1 < n < 41:
        return False
    convergent = []
    halterLijst = []
    maximaleLengteSterretjes = (2*n)-1

    for i in range(maximaleLengteSterretjes, 0, -2): #Tel vanaf maximaleLengteSterretjes terug met stapjes van 2.
        sterretjes = i*"*"
        streepjes = (maximaleLengteSterretjes - len(sterretjes)) / 2 * "-"
        totaal = streepjes + sterretjes + streepjes
        convergent.append(totaal)

    for item in convergent:
        halterLijst.append(item)

    for j in range((len(convergent)-1), -1, -1):
        halterLijst.append(convergent[j])

    halterLijst.pop(maximaleLengteSterretjes/2)

    return halterLijst

try:
    for item in halter(input("N=")):
        print item
except:
    print "Dat is geen geldige waarde voor N!"