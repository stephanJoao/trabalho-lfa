import python.ConjuntoEstados as ConjuntoEstados

class TransicaoN:
    def __init__(self):
        self.origem = None
        self.destino = ConjuntoEstados()
        self.simbolo = None

    def getDestino(self):
        return self.destino.clonar()

    def setDestino(self, destino):
        self.destino = destino.clonar()

    def getOrigem(self):
        if self.origem is not None:
            return self.origem.clonar()
        else:
            return None

    def setOrigem(self, origem):
        self.origem = origem.clonar()

    def getSimbolo(self):
        return self.simbolo.clonar()

    def setSimbolo(self, simbolo):
        self.simbolo = simbolo.clonar()

    def clonar(self):
        tn = TransicaoN()
        tn.setOrigem(self.origem)
        tn.setDestino(self.destino)
        tn.setSimbolo(self.simbolo)
        return tn

    def igual(self, transicao):
        if (
            self.destino.igual(transicao.getDestino())
            and self.origem.igual(transicao.getOrigem())
            and self.simbolo.igual(transicao.getSimbolo())
        ):
            return True
        else:
            return False

    def __str__(self):
        s = "("
        if self.origem is not None:
            s += self.getOrigem().toString()
        s += ","
        if self.simbolo is not None:
            s += self.getSimbolo().toString()
        s += ","
        s += self.getDestino().toString()
        s += ")"
        return s