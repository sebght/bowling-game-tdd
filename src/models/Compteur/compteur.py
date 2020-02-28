class Compteur:
    def __init__(self):
        self.score = 0
        self.numero_tir = 0
        self.spare = False
        self.strike = False
        self.double_strike = False
        self.score_tir_prec = -1
        self.tir_bonus_dernier_round = False

    def get_score(self):
        return self.score

    def tir(self, score_tir):
        self.numero_tir += 1
        if self.partie_pas_terminee():
            self.score += score_tir
            if not self.dernier_round():
                if self.spare:
                    self.appliquer_bonus_spare(score_tir)
                self.spare = self.check_spare(score_tir)
                if self.strike:
                    self.appliquer_bonus_strike(score_tir)
                if self.check_strike(score_tir):
                    self.strike = True
                    self.numero_tir += 1
                    self.double_strike = self.check_double_strike()
            else:
                if self.spare and self.numero_tir == 19:
                    self.appliquer_bonus_spare(score_tir)
                if self.strike and self.numero_tir <= 20:
                    self.appliquer_bonus_strike(score_tir)
                if score_tir == 10 or self.check_spare(score_tir):
                    self.tir_bonus_dernier_round = True
                if self.numero_tir == 21:
                    self.tir_bonus_dernier_round = False
            self.score_tir_prec = score_tir

    def appliquer_bonus_spare(self, score_tir):
        self.score += score_tir
        self.spare = False

    def appliquer_bonus_strike(self, score_tir):
        self.score += score_tir
        if self.is_second_tir_du_round():
            self.strike = False
        elif self.double_strike:
            self.score += score_tir
            self.double_strike = False

    def check_strike(self, score_tir):
        return score_tir == 10 and self.is_premier_tir_du_round()

    def check_double_strike(self):
        return self.score_tir_prec == 10

    def check_spare(self, score_tir):
        return score_tir + self.score_tir_prec == 10 and self.is_second_tir_du_round()

    def is_premier_tir_du_round(self):
        return self.numero_tir % 2 == 1

    def is_second_tir_du_round(self):
        return not self.is_premier_tir_du_round()

    def partie_pas_terminee(self):
        return self.tir_bonus_dernier_round or self.numero_tir <= 20

    def dernier_round(self):
        return self.numero_tir > 18
