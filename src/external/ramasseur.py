class Ramasseur:

    def __init__(self):
        self.pins = 10

    def setPins(self, pins):
        print("Je remets " + str(pins) + " quilles.")
        self.pins = pins

    def getPins(self):
        return input("Quilles restantes après le tir:[0.." + str(self.pins) + "] ")


if __name__ == '__main__':
    ps = Ramasseur()
    ps.setPins(10)
    standing = ps.getPins()
    ps.setPins(standing)
    ps.getPins()
