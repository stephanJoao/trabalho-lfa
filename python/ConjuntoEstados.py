class ConjuntoEstados:
    def __init__(self):
        self.elementos = set()

    def vazio(self):
        return len(self.elementos) == 0

    def limpar(self):
        self.elementos.clear()

    def inclui(self, elemento):
        self.elementos.add(elemento.clonar())

    def pertence(self, elemento):
        if elemento is None:
            return False
        for estado in self.elementos:
            if estado.igual(elemento):
                return True
        return False

    def retornaIgual(self, elemento):
        if elemento is None:
            return None
        for estado in self.elementos:
            if estado.igual(elemento):
                return estado
        return None

    def uniao(self, ce):
        novoConjunto = ConjuntoEstados()
        novoConjunto.elementos = self.clonar().elementos
        for estado in ce.getElementos():
            if not novoConjunto.pertence(estado):
                novoConjunto.inclui(estado.clonar())
        return novoConjunto

    def intersecao(self, ce):
        novoConjunto = ConjuntoEstados()
        for estado in ce.getElementos():
            if self.pertence(estado):
                novoConjunto.inclui(estado.clonar())
        return novoConjunto

    def clonar(self):
        novoConjunto = ConjuntoEstados()
        for estado in self.elementos:
            novoConjunto.inclui(estado.clonar())
        return novoConjunto

    def igual(self, ce):
        flag = True
        aux = ce.clonar()
        for e in aux.getElementos():
            if not self.pertence(e):
                flag = False
            if not flag:
                break
        if not flag:
            return False
        aux = self.clonar()
        for e in aux.getElementos():
            if not ce.pertence(e):
                flag = False
            if not flag:
                break
        return flag

    def __str__(self):
        s = "{"
        tmp = self.clonar()
        size = len(tmp.getElementos()) - 1
        for e in tmp.getElementos():
            s += str(e)
            if size != 0:
                s += ","
            size -= 1
        s += "}"
        if s == "":
            s = "{}"
        return s

    def getElementos(self):
        return self.elementos

    def size(self):
        return len(self.elementos)

    def iterator(self):
        return iter(self.elementos)

    def removerElemento(self, e):
        self.elementos.remove(e)
