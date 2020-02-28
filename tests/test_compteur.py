from unittest import TestCase
from src.models.Compteur.compteur import Compteur


class TestCompteur(TestCase):
    def setUp(self):
        self.compteur = Compteur()


class TestTir(TestCompteur):
    def test_pas_de_tir_egal_0(self):
        self.assertEqual(self.compteur.get_score(), 0)

    def test_premier_tir_nul(self):
        self.compteur.tir(0)
        self.assertEqual(self.compteur.get_score(), 0)

    def test_premier_tir_non_nul(self):
        self.compteur.tir(6)
        self.assertEqual(self.compteur.get_score(), 6)

    def test_deux_tirs_non_nuls(self):
        self.compteur.tir(3)
        self.compteur.tir(6)
        self.assertEqual(self.compteur.get_score(), 9)


class TestSpare(TestCompteur):
    def test_spare_0_10_puis_3(self):
        self.compteur.tir(0)
        self.compteur.tir(10)
        self.compteur.tir(3)
        self.assertEqual(self.compteur.get_score(), 0 + 10 + 3 + 3)

    def test_spare_puis_tir_compte_double(self):
        self.compteur.tir(3)
        self.compteur.tir(7)
        self.compteur.tir(3)
        self.assertEqual(self.compteur.get_score(), 3 + 7 + 3 + 3)

    def test_round_sans_spare_puis_spare_puis_un_tir_compte_double(self):
        self.compteur.tir(3)
        self.compteur.tir(2)
        self.compteur.tir(5)
        self.compteur.tir(5)
        self.compteur.tir(3)
        self.assertEqual(self.compteur.get_score(), 3 + 2 + 5 + 5 + 3 + 3)

    def test_faux_spare_sur_deux_rounds(self):
        self.compteur.tir(2)
        self.compteur.tir(3)
        self.compteur.tir(7)
        self.compteur.tir(2)
        self.assertEqual(self.compteur.get_score(), 2 + 3 + 7 + 2)

    def test_deux_spares_separes_d_un_round_sans_spare(self):
        self.compteur.tir(7)
        self.compteur.tir(3)
        self.compteur.tir(2)
        self.compteur.tir(0)
        self.compteur.tir(5)
        self.compteur.tir(5)
        self.compteur.tir(3)
        self.assertEqual(self.compteur.get_score(), 7 + 3 + 2 + 2 + 0 + 5 + 5 + 3 + 3)

    def test_deux_spares_d_affilee(self):
        self.compteur.tir(7)
        self.compteur.tir(3)
        self.compteur.tir(2)
        self.compteur.tir(8)
        self.compteur.tir(5)
        self.assertEqual(self.compteur.get_score(), 7 + 3 + 2 + 2 + 8 + 5 + 5)


class TestStrike(TestCompteur):
    def test_un_strike_rien_d_autre(self):
        self.compteur.tir(10)
        self.assertEqual(self.compteur.get_score(), 10)

    def test_un_strike_puis_0_0(self):
        self.compteur.tir(10)
        self.compteur.tir(0)
        self.compteur.tir(0)
        self.assertEqual(self.compteur.get_score(), 10 + 0 * 2 + 0 * 2)

    def test_un_strike_puis_un_tir_normal_non_nulle(self):
        self.compteur.tir(10)
        self.compteur.tir(3)
        self.assertEqual(10 + 3 * 2, self.compteur.get_score())

    def test_un_strike_puis_deux_tirs_normaux_non_nulles(self):
        self.compteur.tir(10)
        self.compteur.tir(3)
        self.compteur.tir(4)
        self.assertEqual(10 + 3 * 2 + 4 * 2, self.compteur.get_score())

    def test_deux_tirs_normaux_non_nulles_puis_un_strike_puis_deux_tirs_normaux(self):
        self.compteur.tir(3)
        self.compteur.tir(4)
        self.compteur.tir(10)
        self.compteur.tir(3)
        self.compteur.tir(2)
        self.assertEqual(3 + 4 + 10 + 3 * 2 + 2 * 2, self.compteur.get_score())

    def test_strike_deux_tirs_normaux_puis_un_strike_puis_deux_tirs_normaux(self):
        self.compteur.tir(10)
        self.compteur.tir(3)
        self.compteur.tir(2)
        self.compteur.tir(10)
        self.compteur.tir(3)
        self.compteur.tir(4)
        self.assertEqual(10 + 3 * 2 + 2 * 2 + 10 + 3 * 2 + 4 * 2, self.compteur.get_score())

    def test_deux_strikes_puis_deux_tirs_normaux(self):
        self.compteur.tir(10)
        self.compteur.tir(10)
        self.compteur.tir(2)
        self.compteur.tir(3)
        self.assertEqual(10 + 10 * 2 + 2 * 3 + 3 * 2, self.compteur.get_score())

    def test_strike_puis_spare_puis_deux_tirs_normaux(self):
        self.compteur.tir(10)
        self.compteur.tir(3)
        self.compteur.tir(7)
        self.compteur.tir(2)
        self.compteur.tir(3)
        self.assertEqual(10 + 3 * 2 + 7 * 2 + 2 * 2 + 3, self.compteur.get_score())

    def test_spare_puis_strike_puis_deux_tirs_normaux(self):
        self.compteur.tir(3)
        self.compteur.tir(7)
        self.compteur.tir(10)
        self.compteur.tir(2)
        self.compteur.tir(3)
        self.assertEqual(3 + 7 + 10 * 2 + 2 * 2 + 3 * 2, self.compteur.get_score())


class TestLastRound(TestCompteur):
    def test_tous_les_tirs_0(self):
        for x in range(20):
            self.compteur.tir(0)
        self.assertEqual(0, self.compteur.get_score())

    def test_tous_les_tirs_0_puis_3(self):
        for x in range(20):
            self.compteur.tir(0)
        self.compteur.tir(3)
        self.assertEqual(0, self.compteur.get_score())

    def test_9_premiers_rounds_full_0_puis_2_3_4(self):
        for x in range(18):
            self.compteur.tir(0)
        self.compteur.tir(2)
        self.compteur.tir(3)
        self.compteur.tir(4)
        self.assertEqual(2 + 3, self.compteur.get_score())

    def test_9_premiers_rounds_full_0_puis_spare_puis_4(self):
        for x in range(18):
            self.compteur.tir(0)
        self.compteur.tir(7)
        self.compteur.tir(3)
        self.compteur.tir(4)
        self.assertEqual(7 + 3 + 4, self.compteur.get_score())

    def test_9_premiers_rounds_full_0_puis_strike_puis_3_4(self):
        for x in range(18):
            self.compteur.tir(0)
        self.compteur.tir(10)
        self.compteur.tir(3)
        self.compteur.tir(4)
        self.assertEqual(10 + 3 + 4, self.compteur.get_score())

    def test_9_premiers_rounds_full_0_puis_deux_strike_puis_2(self):
        for x in range(18):
            self.compteur.tir(0)
        self.compteur.tir(10)
        self.compteur.tir(10)
        self.compteur.tir(2)
        self.assertEqual(10 + 10 + 2, self.compteur.get_score())

    def test_8_premiers_rounds_full_0_puis_spare_puis_deux_strike_puis_2(self):
        for x in range(17):
            self.compteur.tir(0)
        self.compteur.tir(10)
        self.compteur.tir(10)
        self.compteur.tir(10)
        self.compteur.tir(2)
        self.assertEqual(10 + 10 * 2 + 10 + 2, self.compteur.get_score())

    def test_8_premiers_rounds_full_0_puis_deux_strikes_puis_8_2(self):
        for x in range(16):
            self.compteur.tir(0)
        self.compteur.tir(10)
        self.compteur.tir(10)
        self.compteur.tir(8)
        self.compteur.tir(2)
        self.assertEqual(10 + 10 * 2 + 8 * 2 + 2, self.compteur.get_score())

    def test_partie_parfaite(self):
        for x in range(12):
            self.compteur.tir(10)
        self.assertEqual(300, self.compteur.get_score())

    def test_partie_parfaite_puis_tir_en_plus(self):
        for x in range(12):
            self.compteur.tir(10)
        self.compteur.tir(4)
        self.assertEqual(300, self.compteur.get_score())

# 0 * 20
# 0 * 20, 3
# 0 * 18 , 2 3 4
# 0 * 18, 7 3 4
# 0 * 18, 10 3 4
# 0 * 18, 10 10 2
# 0 * 17 10, 10 10 2
# 0 * 16 10, 10 8 2
# 12 * 10 la
# 12 * 10, 4
