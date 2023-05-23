class TransicaoD:
    def __init__(self):
        self.origem = None
        self.destino = None
        self.simbolo = None

    def getDestino(self):
        return self.destino.clonar()

    def setDestino(self, destino):
        self.destino = destino.clonar()

    def getOrigem(self):
        return self.origem.clonar()

    def setOrigem(self, origem):
        self.origem = origem.clonar()

    def getSimbolo(self):
        return self.simbolo

    def setSimbolo(self, simbolo):
        self.simbolo = simbolo.clonar()

    def clonar(self):
        td = TransicaoD()
        td.setOrigem(self.origem)
        td.setDestino(self.destino)
        td.setSimbolo(self.simbolo)
        return td

    def igual(self, transicao):
        return (
            self.destino.igual(transicao.getDestino())
            and self.origem.igual(transicao.getOrigem())
            and self.simbolo.igual(transicao.getSimbolo())
        )

    def __str__(self):
        s = "("
        s += str(self.getOrigem()) + ","
        s += str(self.getSimbolo()) + ","
        s += str(self.getDestino()) + ","
        s += ")"
        return s
