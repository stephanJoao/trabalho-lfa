from ConjuntoEstados import ConjuntoEstados

class ConjuntoConjuntoEstados:
    def __init__(self):
        self.elementos = set()

    def vazio(self):
        return len(self.elementos) == 0

    def limpar(self):
        self.elementos.clear()

    def inclui(self, elemento):
        self.elementos.add(elemento.clonar())

    def pertence(self, elemento):
        for conjuntoEstados in self.elementos:
            if conjuntoEstados.igual(elemento):
                return True
        return False

    def uniao(self, cce):
        novoConjunto = ConjuntoConjuntoEstados()
        novoConjunto.elementos = self.clonar().elementos
        for conjuntoEstados in cce.getElementos():
            if not novoConjunto.pertence(conjuntoEstados):
                novoConjunto.inclui(conjuntoEstados.clonar())
        return novoConjunto

    def intersecao(self, cce):
        novoConjunto = ConjuntoConjuntoEstados()
        for conjuntoEstados in cce.getElementos():
            if self.pertence(conjuntoEstados):
                novoConjunto.inclui(conjuntoEstados.clonar())
        return novoConjunto

    def clonar(self):
        novoConjunto = ConjuntoConjuntoEstados()
        for conjuntoEstados in self.elementos:
            novoConjunto.inclui(conjuntoEstados.clonar())
        return novoConjunto

    def igual(self, cce):
        flag = True
        aux = cce.clonar()
        for conjuntoEstados in aux.getElementos():
            if not self.pertence(conjuntoEstados):
                flag = False
            if not flag:
                break
        if not flag:
            return False
        aux = self.clonar()
        for conjuntoEstados in aux.getElementos():
            if not cce.pertence(conjuntoEstados):
                flag = False
            if not flag:
                break
        return flag

    def getElementos(self):
        return self.elementos

    def iterator(self):
        return iter(self.elementos)

    def removerElemento(self, ce):
        self.elementos.remove(ce)

    def uniaoInterna(self):
        conjunto = self.getElementos()
        novo = ConjuntoEstados()
        for conjuntoEstados in conjunto:
            novo.uniao(conjuntoEstados)
        return novo.clonar()

    def __str__(self):
        resp = "{"
        for i, conjuntoEstados in enumerate(self.elementos):
            resp += str(conjuntoEstados)
            if i < len(self.elementos) - 1:
                resp += ","
        return resp + "}"
