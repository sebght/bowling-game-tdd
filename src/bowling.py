from src.models.Arbitre.arbitre import Arbitre
from src.models.Compteur.compteur import Compteur
from src.models.Lecteur.lecteur import Lecteur
from src.models.Vue.vue import Vue


def initialisation_scoreboard(nombre_joueurs):
    compteurs = []
    for i in range(nombre_joueurs):
        compteurs.append(Compteur())
    return compteurs


class Bowling:

    def __init__(self, nombre_joueurs):
        self.arbitre = Arbitre(nombre_joueurs)
        self.compteurs = initialisation_scoreboard(nombre_joueurs)
        self.lecteur = Lecteur()
        self.vue = Vue()
        self.joueur_actuel = 1
        self.nombre_joueurs = nombre_joueurs

    def annonce_joueur(self):
        self.vue.affiche_invite(self.arbitre.a_qui_le_tour())

    def fin_partie(self):
        return self.arbitre.fin_partie()

    def round(self):
        self.annonce_joueur()
        self.joueur_actuel = self.arbitre.joueur_actuel
        self.tir(1)
        self.vue.affiche_score(self.joueur_actuel, self.compteurs[self.joueur_actuel - 1].get_score())
        if self.arbitre.joueur_actuel == self.joueur_actuel:
            self.annonce_joueur()
            self.tir(2)
            self.vue.affiche_score(self.joueur_actuel, self.compteurs[self.joueur_actuel - 1].get_score())

    def tir(self, numero_tir):
        if numero_tir == 1:
            score_tir = self.lecteur.score_premier_tir()
        else:
            score_tir = self.lecteur.score_second_tir()
        self.arbitre.tir_du_joueur(score_tir)
        self.compteurs[self.joueur_actuel - 1].tir(score_tir)

    def score_final(self):
        print("\n")
        print("Scores finaux :")
        for i in range(1, self.nombre_joueurs+1):
            self.vue.affiche_score(i, self.compteurs[i - 1].get_score())


if __name__ == '__main__':
    n = int(input("Combien de joueurs sur cette partie de Bowling ? "))
    bowling = Bowling(n)
    while not bowling.fin_partie():
        bowling.round()
    bowling.score_final()
