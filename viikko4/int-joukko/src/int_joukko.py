KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kapasiteetti2")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.joukko = [0] * self.kapasiteetti

        self.alkiomaara = 0

    def kuuluu(self, luku):
        for i in range(self.alkiomaara):
            if self.joukko[i] == luku:
                return True
        return False

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            self.joukko[self.alkiomaara] = luku
            self.alkiomaara = self.alkiomaara + 1

            if self.alkiomaara % len(self.joukko) == 0:
                vanha_joukko = self.joukko
                self.kopioi_taulukko(self.joukko, vanha_joukko)
                self.joukko = [0] * (self.alkiomaara + self.kasvatuskoko)
                self.kopioi_taulukko(vanha_joukko, self.joukko)

            return True

        return False

    def poista(self, luku):
        indeksi = -1
        temp = 0

        for i in range(self.alkiomaara):
            if luku == self.joukko[i]:
                indeksi = i  # siis luku löytyy tuosta kohdasta :D
                self.joukko[indeksi] = 0
                break

        if indeksi != -1:
            for j in range(indeksi, self.alkiomaara - 1):
                temp = self.joukko[j]
                self.joukko[j] = self.joukko[j + 1]
                self.joukko[j + 1] = temp

            self.alkiomaara = self.alkiomaara - 1
            return True

        return False

    def kopioi_taulukko(self, vanha, uusi):
        for i in range(len(vanha)):
            uusi[i] = vanha[i]

    def mahtavuus(self):
        return self.alkiomaara

    def to_int_list(self):
        alkiolista = []
        for i in range(self.alkiomaara):
            alkiolista.append(self.joukko[i])
        return alkiolista

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        a_joukko = a.to_int_list()
        b_joukko = b.to_int_list()

        for i in range(len(a_joukko)):
            yhdiste.lisaa(a_joukko[i])
            yhdiste.lisaa(b_joukko[i])

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        a_joukko = a.to_int_list()
        b_joukko = b.to_int_list()

        for i in range(len(a_joukko)):
            if a_joukko[i] in b_joukko:
                leikkaus.lisaa(a_joukko[i])
        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        a_joukko = a.to_int_list()
        b_joukko = b.to_int_list()

        for i in range(len(a_joukko)):
            if a_joukko[i] not in b_joukko:
                erotus.lisaa(a_joukko[i])
        return erotus

    def __str__(self):
        joukko = "{"
        for i in range(self.alkiomaara):
            joukko += f"{str(self.joukko[i])}"
            if i != self.alkiomaara - 1:
                joukko += ", "
        joukko += "}"
        return joukko
