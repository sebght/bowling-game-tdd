from unittest import TestCase
from src.models.Arbitre.arbitre import Arbitre


class TestArbitre1joueur(TestCase):
    def setUp(self):
        self.arbitre = Arbitre(1)

    def test_1joueur_pas_de_tir(self):
        self.assertEqual(1, self.arbitre.a_qui_le_tour())

    def test_1joueur_tir_non_strike(self):
        self.arbitre.tir_du_joueur(5)

        self.assertEqual(1, self.arbitre.a_qui_le_tour())

    def test_1joueur_tir_strike(self):
        self.arbitre.tir_du_joueur(10)

        self.assertEqual(1, self.arbitre.a_qui_le_tour())

    def test_1joueur_joue_plusieurs_rounds(self):
        self.arbitre.tir_du_joueur(1)
        self.arbitre.tir_du_joueur(3)
        self.assertEqual(1, self.arbitre.a_qui_le_tour())


class TestArbitreDeuxJoueurs(TestCase):
    def setUp(self):
        self.arbitre = Arbitre(2)

    def test_2joueurs_pas_tir(self):
        self.assertEqual(1, self.arbitre.a_qui_le_tour())

    def test_2joueurs_tir_non_strike(self):
        self.arbitre.tir_du_joueur(3)
        self.assertEqual(1, self.arbitre.a_qui_le_tour())

    def test_2joueurs_tir_strike(self):
        self.arbitre.tir_du_joueur(10)
        self.assertEqual(2, self.arbitre.a_qui_le_tour())

    def test_2joueurs_tirs0_10(self):
        self.arbitre.tir_du_joueur(0)
        self.arbitre.tir_du_joueur(10)
        self.assertEqual(2, self.arbitre.a_qui_le_tour())

    def test_2joueurs_tirs3_2(self):
        self.arbitre.tir_du_joueur(3)
        self.arbitre.tir_du_joueur(2)
        self.assertEqual(2, self.arbitre.a_qui_le_tour())

    def test_2joueurs_tirs3_2_2(self):
        self.arbitre.tir_du_joueur(3)
        self.arbitre.tir_du_joueur(2)
        self.arbitre.tir_du_joueur(2)
        self.assertEqual(2, self.arbitre.a_qui_le_tour())

    def test_2joueurs_tirs3_2_10(self):
        self.arbitre.tir_du_joueur(3)
        self.arbitre.tir_du_joueur(2)
        self.arbitre.tir_du_joueur(10)
        self.assertEqual(1, self.arbitre.a_qui_le_tour())

    def test_2joueurs_tirs3_2_2_2(self):
        self.arbitre.tir_du_joueur(3)
        self.arbitre.tir_du_joueur(2)
        self.arbitre.tir_du_joueur(2)
        self.arbitre.tir_du_joueur(2)
        self.assertEqual(1, self.arbitre.a_qui_le_tour())

    def test_2joueurs_tirs3_2_2_2_10(self):
        self.arbitre.tir_du_joueur(3)
        self.arbitre.tir_du_joueur(2)
        self.arbitre.tir_du_joueur(2)
        self.arbitre.tir_du_joueur(2)
        self.arbitre.tir_du_joueur(10)
        self.assertEqual(2, self.arbitre.a_qui_le_tour())


class TestArbitreTroisJoueurs(TestCase):
    def setUp(self):
        self.arbitre = Arbitre(3)

    def test_3J_3_2_2_2_10(self):
        self.arbitre.tir_du_joueur(3)
        self.arbitre.tir_du_joueur(2)
        self.arbitre.tir_du_joueur(2)
        self.arbitre.tir_du_joueur(2)
        self.arbitre.tir_du_joueur(10)
        self.assertEqual(1, self.arbitre.a_qui_le_tour())

    def test_3J_fin_partie_J1(self):
        for i in range(3*2*9):
            self.arbitre.tir_du_joueur(3)
        self.arbitre.tir_du_joueur(1)
        self.arbitre.tir_du_joueur(1)
        self.assertEqual(2, self.arbitre.a_qui_le_tour())
        self.assertEqual(True, self.arbitre.fin_partie_joueur(1))
        self.assertEqual(False, self.arbitre.fin_partie_joueur(2))

    def test_3J_fin_partie_J1_et_J2(self):
        for i in range(3*2*9 + 2):
            self.arbitre.tir_du_joueur(3)
        self.arbitre.tir_du_joueur(1)
        self.arbitre.tir_du_joueur(1)
        self.assertEqual(3, self.arbitre.a_qui_le_tour())
        self.assertEqual(True, self.arbitre.fin_partie_joueur(1))
        self.assertEqual(True, self.arbitre.fin_partie_joueur(2))
        self.assertEqual(False, self.arbitre.fin_partie_joueur(3))

    def test_3J_fin_partie(self):
        for i in range(3*2*10):
            self.arbitre.tir_du_joueur(3)
        self.assertEqual(True, self.arbitre.fin_partie_joueur(1))
        self.assertEqual(True, self.arbitre.fin_partie_joueur(2))
        self.assertEqual(True, self.arbitre.fin_partie_joueur(3))
        self.assertEqual(True, self.arbitre.fin_partie())
