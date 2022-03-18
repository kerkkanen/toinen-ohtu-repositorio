class Tekoaly:
    def __init__(self):
        self._siirto = 0

    def anna_siirto(self):
        viesti = "Tietokone valitsi: "
        self._siirto = self._siirto + 1
        self._siirto = self._siirto % 3

        if self._siirto == 0:
            return "k", viesti
        elif self._siirto == 1:
            return "p", viesti
        else:
            return "s", viesti

    def aseta_siirto(self, siirto):
        # ei tehdä mitään
        pass
