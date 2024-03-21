from enum import Enum

class Tipo(Enum):
    PAPELERIA = 1
    SUPERMERCADO = 2
    FARMACIA = 3

class productos:
    __subsidio = False
    __calidad = 'A'
    
    #Constante
    
    __IVA_PALERIA = 0.16
    __IVA_SUPERMERCADO = 0.04
    __IVA_FARMACIA = 0.12
    
    #Atributos
    
    __nombre = None
    __tipo = Enum ('Tipo',['PAPELERIA','SUPERMERCADO','FARMACIA'])
    __valorUnitario = 0.0
    __cantidadBodega = 0
    __cantidadMinima = 0
    __cantidadUnidadesVendidas = 0
    
    def getNombre (self):
        return self.__nombre
    
    def getTipo (self):
        return self.__tipo
    
    def getValorUnitario(self):
        return self.__valorUnitario
    
    def getCantidadBodega (self):
        return self.__cantidadBodega
    
    def getCantidadMinima (self):
        return self.__cantidadMinima
    
    def getCantidadUnidadesVendidas (self):
        return self.__cantidadUnidadesVendidas
    
        
    