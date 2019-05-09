a = "79-900"
b = "80-155"

def zwrocListe(a1,a2):

    lista = []
    poczatek = None
    poczatek = a1[0:2]
    poczatek += a1[3:6]
    poczatek = int(poczatek)
    poczatek += 1
    koniec = None
    koniec = a2[0:2]
    koniec +=a2[3:6]
    koniec = int(koniec)

    for i in range(poczatek,koniec,1):
        i = str(i)
        nowy = i[0:2] + "-" + i[2:5]
        lista.append(nowy)
    print (lista)

zwrocListe(a,b)

