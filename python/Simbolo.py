class Simbolo:
    def __init__(self, simbolo=None):
        self.simbolo = simbolo

    def getSimbolo(self):
        return self.simbolo

    def setSimbolo(self, simbolo):
        self.simbolo = simbolo

    def clonar(self):
        s = Simbolo()
        s.setSimbolo(self.getSimbolo())
        return s

    def igual(self, simbolo):
        return self.getSimbolo() == simbolo.getSimbolo()

    def __str__(self):
        return self.getSimbolo()
