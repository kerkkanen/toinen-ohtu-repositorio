from kps import KPS

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        peli = ""

        if vastaus.endswith("a"):
            peli = KPS.ihmispeli()
        elif vastaus.endswith("b"):
            peli = KPS.tekoalypeli()
        elif vastaus.endswith("c"):
            peli = KPS.parannettu_tekoalypeli()
        else:
            break
        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )
        peli.pelaa()


if __name__ == "__main__":
    main()
