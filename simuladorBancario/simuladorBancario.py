from CuentaAhorro import CuentaAhorro
from CuentaCorriente import CuentaCorriente
from CDT import CDT

class SimulacroBancario:
    # Aqui va el codigo de SimuladorBancario
    # Atributos

    Cedula=""
    nombres=""
    MesActual=""

    # Asociaciones

    CuentaCorriente = CuentaCorriente()
    CuentaAhorro = CuentaAhorro()
    CDT = CDT()
    
    # Metodos

    def ConsignarCorriente(self):
    # Aqui va el codigo del metodo
        return self.CuentaCorriente.ConsignarValor(300000)
    
    def CalcularSaldo(self):
    # Aqui va el codigo del metodo
        SaldoTotal= self.CuentaCorriente + self.CuentaAhorro
    
    




    