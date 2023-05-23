class ConjuntoSimbolo:
    def __init__(self):
        self.elementos = set()

    def vazio(self):
        return len(self.elementos) == 0

    def limpar(self):
        self.elementos.clear()

    def inclui(self, elem):
        self.elementos.add(elem)

    def pertence(self, elemento):
        for simbolo in self.elementos:
            if simbolo.igual(elemento):
                return True
        return False

    def uniao(self, ce):
        novoConjunto = self.clonar()
        for simbolo in ce.getElementos():
            if not novoConjunto.pertence(simbolo):
                novoConjunto.inclui(simbolo.clonar())
        return novoConjunto

    def intersecao(self, ce):
        novoConjunto = ConjuntoSimbolo()
        for simbolo in ce.getElementos():
            if self.pertence(simbolo):
                novoConjunto.inclui(simbolo.clonar())
        return novoConjunto

    def clonar(self):
        novoConjunto = ConjuntoSimbolo()
        for simbolo in self.elementos:
            novoConjunto.inclui(simbolo.clonar())
        return novoConjunto

    def igual(self, cs):
        flag = True
        aux = cs.clonar()
        for si in aux.getElementos():
            if not self.pertence(si):
                flag = False
            if not flag:
                break
        if not flag:
            return False
        aux = self.clonar()
        for si in aux.getElementos():
            if not cs.pertence(si):
                flag = False
            if not flag:
                break
        return flag

    def __str__(self):
        s = "{"
        tmp = self.clonar()
        size = len(tmp.getElementos()) - 1
        for si in tmp.getElementos():
            s += si.toString()
            if size != 0:
                s += ","
            size -= 1
        s += "}"
        return s

    def getElementos(self):
        return self.elementos

    def iterator(self):
        return iter(self.elementos)

    def removerElemento(self, s):
        self.elementos.remove(s)
