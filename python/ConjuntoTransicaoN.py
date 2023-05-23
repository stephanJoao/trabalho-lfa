class ConjuntoTransicaoN:
    def __init__(self):
        self.elementos = set()

    def vazio(self):
        return len(self.elementos) == 0

    def inclui(self, elemento):
        self.elementos.add(elemento.clonar())

    def pertence(self, elemento):
        return elemento in self.elementos

    def uniao(self, ce):
        novoConjunto = ConjuntoTransicaoN()
        novoConjunto.elementos = self.elementos.copy()

        for transicaoN in ce.getElementos():
            if not novoConjunto.pertence(transicaoN):
                novoConjunto.inclui(transicaoN.clonar())

        return novoConjunto

    def intersecao(self, ce):
        novoConjunto = ConjuntoTransicaoN()

        for transicaoN in ce.getElementos():
            if self.pertence(transicaoN):
                novoConjunto.inclui(transicaoN.clonar())

        return novoConjunto

    def clonar(self):
        novoConjunto = ConjuntoTransicaoN()

        for transicaoN in self.elementos:
            novoConjunto.inclui(transicaoN.clonar())

        return novoConjunto

    def igual(self, ct):
        flag = True
        aux = ct.clonar()

        for transicaoN in aux.getElementos():
            if not self.pertence(transicaoN):
                flag = False
            if not flag:
                break

        if not flag:
            return False

        aux = self.clonar()

        for transicaoN in aux.getElementos():
            if not ct.pertence(transicaoN):
                flag = False
            if not flag:
                break

        return flag

    def __str__(self):
        s = "{"
        tmp = self.clonar()
        size = len(tmp.getElementos()) - 1

        for transicaoN in tmp.getElementos():
            s += str(transicaoN)

            if size != 0:
                s += ","
            size -= 1

        s += "}"
        return s

    def getElementos(self):
        return self.elementos

    def iterator(self):
        return iter(self.elementos)

    def removerElemento(self, t):
        self.elementos.remove(t)
