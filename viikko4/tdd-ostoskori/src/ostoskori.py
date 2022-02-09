from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostokset = []

    def tavaroita_korissa(self):
        sum = 0
        for ostos in self.ostokset:
            sum += ostos.lukumaara()
        return sum

    def hinta(self):
        sum = 0
        for ostos in self.ostokset:
            sum += ostos.hinta()
        return sum


    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self.ostokset:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                return
        ostos = Ostos(lisattava)
        self.ostokset.append(ostos)

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self.ostokset:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                ostos.muuta_lukumaaraa(-1)
                if ostos.lukumaara() == 0:
                    self.ostokset.remove(ostos)
                
    def tyhjenna(self):
        self.ostokset.clear()

    def ostokset(self):        
        return self.ostokset
