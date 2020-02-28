from unittest import TestCase
from unittest.mock import MagicMock
from src.models.Vue.vue import Vue
from src.external.afficheur import Afficheur


class TestVue(TestCase):
    def setUp(self):
        self.afficheur = Afficheur()

    def test_affiche_score_joueur(self):
        joueur = 0
        score = 66
        self.afficheur.afficher = MagicMock()
        vue = Vue(self.afficheur)
        vue.affiche_score(joueur, score)
        self.afficheur.afficher.assert_called_with("Score du joueur 0 : 66")

    def test_affiche_joueur(self):
        joueur = 3
        self.afficheur.afficher = MagicMock()
        vue = Vue(self.afficheur)
        vue.affiche_invite(joueur)
        self.afficheur.afficher.assert_called_with("Joueur 3, à votre tour")

#
