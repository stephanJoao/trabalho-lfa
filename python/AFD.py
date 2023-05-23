import xml.etree.ElementTree as ET

from ConjuntoSimbolo import ConjuntoSimbolo
from ConjuntoEstados import ConjuntoEstados
from ConjuntoTransicaoD import ConjuntoTransicaoD

class AFD:
    def __init__(self, simbolos=None, estados=None, funcaoPrograma=None, estadoInicial=None, estadosFinais=None):
        self.simbolos = simbolos if simbolos is not None else ConjuntoSimbolo()
        self.estados = estados if estados is not None else ConjuntoEstados()
        self.funcaoPrograma = funcaoPrograma if funcaoPrograma is not None else ConjuntoTransicaoD()
        self.estadoInicial = estadoInicial 
        self.estadosFinais = estadosFinais
    
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
    
    def clonar(self):
        return AFD(self.simbolos, self.estados, self.funcaoPrograma, self.estadoInicial, self.estadosFinais)
    
    def ler(self, pathArquivo):
        tree = ET.parse(pathArquivo)
        root = tree.getroot()
        
        simbolos_elem = root.find("simbolos")
        self.simbolos = [elem.get("valor") for elem in simbolos_elem.findall("elemento")]
        
        estados_elem = root.find("estados")
        self.estados = [elem.get("valor") for elem in estados_elem.findall("elemento")]
        
        estadosFinais_elem = root.find("estadosFinais")
        self.estadosFinais = [elem.get("valor") for elem in estadosFinais_elem.findall("elemento")]
        
        funcaoPrograma_elem = root.find("funcaoPrograma")
        self.funcaoPrograma = []
        for elem in funcaoPrograma_elem.findall("elemento"):
            origem = elem.get("origem")
            destino = elem.get("destino")
            simbolo = elem.get("simbolo")
            self.funcaoPrograma.append((origem, destino, simbolo))
    
    def p(self, estado, simbolo):
        for transicao in self.funcaoPrograma:
            origem, destino, simb = transicao
            if origem == estado and simb == simbolo:
                return destino
        return None
    
    def pe(self, estado, palavra):
        eAtual = estado
        for simbolo in palavra:
            eAtual = self.p(eAtual, simbolo)
            if eAtual is None:
                return None
        return eAtual
    
    def aceita(self, palavra):
        return self.pe(self.estadoInicial, palavra) in self.estadosFinais
    
    def toXML(self, filename):
        root = ET.Element("AFD")
        
        simbolos_elem = ET.SubElement(root, "simbolos")
        for simbolo in self.simbolos:
            elem = ET.SubElement(simbolos_elem, "elemento", valor=simbolo)
        
        estados_elem = ET.SubElement(root, "estados")
        for estado in self.estados:
            elem = ET.SubElement(estados_elem, "elemento", valor=estado)
        
        estadosFinais_elem = ET.SubElement(root, "estadosFinais")
        for estadoFinal in self.estadosFinais:
            elem = ET.SubElement(estadosFinais_elem, "elemento", valor=estadoFinal)
        
        funcaoPrograma_elem = ET.SubElement(root, "funcaoPrograma")
        for transicao in self.funcaoPrograma:
            origem, destino, simbolo = transicao
            elem = ET.SubElement(funcaoPrograma_elem, "elemento", origem=origem, destino=destino, simbolo=simbolo)
        
        tree = ET.ElementTree(root)
        tree.write(filename)
