from src.external.afficheur import Afficheur


class Vue:

    def __init__(self, afficheur=Afficheur()):
        self.afficheur = afficheur

    def affiche_score(self, joueur, score):
        self.afficheur.afficher("Score du joueur " + str(joueur) + " : " + str(score))

    def affiche_invite(self, joueur):
        self.afficheur.afficher("Joueur " + str(joueur) + ", à votre tour")
