import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("Maito", 3)
        self.marsu = Tuote("Marsu", 30)
        
    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_yhden_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.marsu)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_tuotteen_lisaamisen_jalkeen_korin_hinta_tavaroiden_summa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.marsu)
        self.assertEqual(self.kori.hinta(),33)

    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_tuotteen_lisaamisen_jalkeen_korin_hinta_on_tuotteiden_hinta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.hinta(), 6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)
        ostokset = self.kori.ostokset 
        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_ostos_jolla_tuotteen_nimi_ja_maara(self):
        self.kori.lisaa_tuote(self.maito)
        ostokset = self.kori.ostokset 
        self.assertEqual(ostokset[0].tuotteen_nimi(), "Maito")
        self.assertEqual(ostokset[0].lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.marsu)
        ostokset = self.kori.ostokset 
        self.assertEqual(len(ostokset), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        ostokset = self.kori.ostokset 
        self.assertEqual(len(ostokset), 1)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_ostos_jolla_tuotteen_nimi_ja_maara(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        ostokset = self.kori.ostokset 
        self.assertEqual(ostokset[0].tuotteen_nimi(), "Maito")
        self.assertEqual(ostokset[0].lukumaara(), 2)    
        
    def test_korissa_kaksi_samaa_tuotetta_ja_poiston_jalkeen_vain_yksi(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        self.kori.poista_tuote(self.maito)
        ostokset = self.kori.ostokset 
        self.assertEqual(ostokset[0].lukumaara(), 1)

    def test_korissa_tuote_ja_poiston_jalkeen_kori_tyhja(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.poista_tuote(self.maito)
        ostokset = self.kori.ostokset 
        self.assertEqual(len(ostokset), 0)