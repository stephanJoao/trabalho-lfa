import xml.etree.ElementTree as ET

from ConjuntoSimbolo import ConjuntoSimbolo
from ConjuntoEstados import ConjuntoEstados
from ConjuntoTransicaoN import ConjuntoTransicaoN

class AFN:
    def __init__(self, simbolos=None, estados=None, funcaoPrograma=None, estadoInicial=None, estadosFinais=None):
        self.simbolos = simbolos.clonar() if simbolos is not None else ConjuntoSimbolo()
        self.estados = estados.clonar if estados is not None else ConjuntoEstados()
        self.funcaoPrograma = funcaoPrograma.clonar() if funcaoPrograma is not None else ConjuntoTransicaoN()
        self.estadoInicial = estadoInicial
        self.estadosFinais = estadosFinais.clonar() if estadosFinais is not None else ConjuntoEstados()

    def getEstadoInicial(self):
        return self.estadoInicial

    def setEstadoInicial(self, estadoInicial):
        self.estadoInicial = estadoInicial

    def getEstados(self):
        return self.estados

    def setEstados(self, estados):
        self.estados = estados

    def getEstadosFinais(self):
        return self.estadosFinais

    def setEstadosFinais(self, estadosFinais):
        self.estadosFinais = estadosFinais

    def getFuncaoPrograma(self):
        return self.funcaoPrograma

    def setFuncaoPrograma(self, funcaoPrograma):
        self.funcaoPrograma = funcaoPrograma

    def getSimbolos(self):
        return self.simbolos

    def setSimbolos(self, simbolos):
        self.simbolos = simbolos

    def p(self, e, s):
        fp = self.getFuncaoPrograma()
        for t in fp:
            if t.getOrigem() == e and t.getSimbolo() == s:
                return t.getDestino()
        return set()

    def pe(self, e, p):
        if p == "":
            return e
        else:
            enovo = set()
            s = p[0]
            for est in e:
                enovo = enovo.union(self.p(est, s))
            return self.pe(enovo, p[1:])

    def Aceita(self, p):
        cestadoInicial = {self.getEstadoInicial()}
        cestadoFinal = self.getEstadosFinais()
        for e in self.pe(cestadoInicial, p):
            if e in cestadoFinal:
                return True
        return False

    def toAFD(self):
        novoCsi = self.getSimbolos()
        novoCe = set()
        novoCtD = []
        novoEi = self.getEstadoInicial()
        novoCef = set()
        novoE = None

        atualCef = self.getEstadosFinais()

        cceAtual = set()
        ceAtual = set()
        eAtual = self.getEstadoInicial()
        siAtual = None

        ceAtual.add(eAtual)
        cceAtual.add(ceAtual)

        if eAtual in atualCef:
            novoCef.add(novoEi)

        novoCe.add(novoEi)

        while cceAtual:
            ceAtual = cceAtual.pop()

            ceTemp = set()

            efinal = False

            for siAtual in novoCsi:
                ceTemp = set()
                for eAtual in ceAtual:
                    ceTemp = ceTemp.union(self.p(eAtual, siAtual))

                if ceTemp:
                    novoNome = str(ceTemp)
                    novoNome = novoNome[1:-1]
                    novoE = "<" + novoNome + ">"
                    for estadoFinal in ceTemp:
                        if estadoFinal in atualCef:
                            efinal = True

                    novoCtD.append((ceAtual, siAtual, ceTemp))
                    novoCe.add(novoE)
                    if efinal:
                        novoCef.add(novoE)

                    if ceTemp not in cceAtual:
                        cceAtual.add(ceTemp)

        novoFuncaoPrograma = []
        for (origem, simbolo, destino) in novoCtD:
            novoOrigem = str(origem)
            novoOrigem = novoOrigem[1:-1]
            novoDestino = str(destino)
            novoDestino = novoDestino[1:-1]
            novoFuncaoPrograma.append((novoOrigem, simbolo, novoDestino))

        novoAFD = AFD(novoCsi, novoCe, novoFuncaoPrograma, novoEi, novoCef)
        return novoAFD
