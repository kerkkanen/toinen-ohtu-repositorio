
from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu
from ihmispelaaja import Ihmispelaaja

class KPS:
    def __init__(self, tuomari, peli):
        self._tuomari = tuomari
        self._peli = peli

    def pelaa(self):

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto, viesti = self._toisen_siirto()
        print(f"{viesti} {tokan_siirto}")

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            self._tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(self._tuomari)

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto, viesti = self._toisen_siirto()
            
            print(f"{viesti} {tokan_siirto}")
            self._peli.aseta_siirto(ekan_siirto)

        print("Kiitos!")
        print(self._tuomari)
    
    def _ensimmaisen_siirto(self):
      return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self):
      return self._peli.anna_siirto()

    def _onko_ok_siirto(self, siirto):
        return siirto in ("k", "p", "s")

    @staticmethod
    def ihmispeli():
        return KPS(Tuomari(), Ihmispelaaja())

    @staticmethod
    def tekoalypeli():
        return KPS(Tuomari(), Tekoaly())

    @staticmethod
    def parannettu_tekoalypeli():
        return KPS(Tuomari(), TekoalyParannettu())

    