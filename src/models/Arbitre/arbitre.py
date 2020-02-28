class Arbitre:

    def __init__(self, nombre_joueurs):
        self.nombre_joueurs = nombre_joueurs
        self.joueur_actuel = 1
        self.numero_tir = 0
        self.rounds = [0] * nombre_joueurs

    def a_qui_le_tour(self):
        return self.joueur_actuel

    def tir_du_joueur(self, score_tir):
        self.numero_tir += 1
        if self.check_fin_round(score_tir):
            self.changement_joueur()
            self.numero_tir = 0

    def check_fin_round(self, score_tir):
        return score_tir == 10 or self.numero_tir == 2

    def fin_partie_joueur(self, joueur):
        return self.rounds[joueur - 1] == 10

    def fin_partie(self):
        return self.rounds == [10] * self.nombre_joueurs

    def changement_joueur(self):
        self.rounds[self.joueur_actuel - 1] += 1
        self.joueur_actuel = self.joueur_actuel % self.nombre_joueurs + 1
