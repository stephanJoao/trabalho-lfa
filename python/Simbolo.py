class Simbolo:

    def __init__(self, simbolo=None):
        self.simbolo = simbolo
        self.vazia = 'E' # VE ESSA MERDA DEPOIS

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
        return str(self.getSimbolo())
