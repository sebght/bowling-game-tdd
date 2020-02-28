from src.external.ramasseur import Ramasseur


class Lecteur:

    def __init__(self, ramasseur=Ramasseur()):
        self.ramasseur = ramasseur
        self.standing_pins = 10

    def score_premier_tir(self):
        self.ramasseur.setPins(10)
        self.standing_pins = self.ramasseur.getPins()
        return 10 - int(self.standing_pins)

    def score_second_tir(self):
        self.ramasseur.setPins(self.standing_pins)
        score_second_tir = int(self.standing_pins) - int(self.ramasseur.getPins())
        return score_second_tir
