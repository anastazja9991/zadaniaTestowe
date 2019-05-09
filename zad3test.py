from decimal import Decimal

def generuj(poczatek=2, koniec=5.5):
    poczatek = Decimal(poczatek)
    koniec = Decimal(koniec)
    while poczatek <= koniec:
        yield poczatek
        poczatek += Decimal(0.5)

print([liczby for liczby in generuj()])
