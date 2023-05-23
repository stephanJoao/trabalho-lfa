class Estado:
    def __init__(self, nome=""):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome
    
    def clonar(self):
        e = Estado()
        e.setNome(self.getNome())
        return e
    
    def igual(self, estado):
        if self.getNome() == estado.getNome():
            return True
        else:
            return False
    
    def __str__(self):
        return self.getNome()
