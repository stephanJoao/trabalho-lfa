class ConjuntoTransicaoD:
    def __init__(self):
        self.elementos = set()

    def vazio(self):
        return len(self.elementos) == 0

    def limpar(self):
        self.elementos.clear()

    def inclui(self, elemento):
        self.elementos.add(elemento.clonar())

    def pertence(self, elemento):
        return elemento in self.elementos

    def uniao(self, ce):
        novoConjunto = self.clonar()
        for elemento in ce.getElementos():
            if elemento not in novoConjunto.elementos:
                novoConjunto.inclui(elemento.clonar())
        return novoConjunto

    def intersecao(self, ce):
        novoConjunto = ConjuntoTransicaoD()
        for elemento in ce.getElementos():
            if self.pertence(elemento):
                novoConjunto.inclui(elemento.clonar())
        return novoConjunto

    def clonar(self):
        novoConjunto = ConjuntoTransicaoD()
        for elemento in self.elementos:
            novoConjunto.inclui(elemento.clonar())
        return novoConjunto

    def igual(self, ct):
        flag = True
        aux = ct.clonar()
        for elemento in aux.getElementos():
            if not self.pertence(elemento):
                flag = False
            if not flag:
                break
        if not flag:
            return False
        aux = self.clonar()
        for elemento in aux.getElementos():
            if not ct.pertence(elemento):
                flag = False
            if not flag:
                break
        return flag

    def __str__(self):
        s = "{"
        tmp = self.clonar()
        size = len(tmp.getElementos()) - 1
        for i, elemento in enumerate(tmp.getElementos()):
            s += str(elemento)
            if i < size:
                s += ","
        s += "}"
        return s

    def getElementos(self):
        return self.elementos

    def removerElemento(self, t):
        self.elementos.remove(t)
