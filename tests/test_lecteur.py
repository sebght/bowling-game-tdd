from unittest import TestCase
from unittest.mock import MagicMock
from src.models.Lecteur.lecteur import Lecteur
from src.external.ramasseur import Ramasseur


class TestLecteur(TestCase):
    def setUp(self):
        self.ramasseur = Ramasseur()
        self.lecteur = Lecteur(self.ramasseur)
        self.ramasseur.setPins = MagicMock()

    def test_1er_tir_nul(self):
        self.ramasseur.getPins = MagicMock(return_value=10)
        self.assertEqual(10 - 10, self.lecteur.score_premier_tir())

    def test_1er_tir_non_nul(self):
        self.ramasseur.getPins = MagicMock(return_value=5)
        self.assertEqual(10 - 5, self.lecteur.score_premier_tir())

    def test_1er_tir_strike(self):
        self.ramasseur.getPins = MagicMock(return_value=0)
        self.assertEqual(10 - 0, self.lecteur.score_premier_tir())

    def test_2_tirs_non_nuls(self):
        self.ramasseur.getPins = MagicMock(return_value=5)
        self.lecteur.score_premier_tir()
        self.ramasseur.getPins = MagicMock(return_value=2)
        self.assertEqual(5 - 2, self.lecteur.score_second_tir())
