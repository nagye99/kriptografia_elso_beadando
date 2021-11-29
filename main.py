import felhasznalo
from tranzakcio import tranzakcio
from epit import epit

def main():
    blokLanc = []
    tranzakciok = []
    t1 = tranzakcio(felhasznalo.A, felhasznalo.B, 10)
    tranzakciok.append(t1)
    t2 = tranzakcio(felhasznalo.C, felhasznalo.D, 50)
    tranzakciok.append(t2)
    t3 = tranzakcio(felhasznalo.B, felhasznalo.D, 40)
    tranzakciok.append(t3)
    t4 = tranzakcio(felhasznalo.D, felhasznalo.A, 19)
    tranzakciok.append(t4)

    uj_elem = epit(tranzakciok, blokLanc)
    blokLanc.append(uj_elem)

    tranzakciok = []
    t1 = tranzakcio(felhasznalo.A, felhasznalo.B, 10)
    tranzakciok.append(t1)
    t2 = tranzakcio(felhasznalo.C, felhasznalo.D, 50)
    tranzakciok.append(t2)
    t3 = tranzakcio(felhasznalo.B, felhasznalo.D, 40)
    tranzakciok.append(t3)
    t4 = tranzakcio(felhasznalo.D, felhasznalo.A, 19)
    tranzakciok.append(t4)

    uj_elem = epit(tranzakciok, blokLanc)
    blokLanc.append(uj_elem)
    print(blokLanc)

##############################################################################

if __name__ == "__main__":
    main()