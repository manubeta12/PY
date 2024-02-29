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

    SaldoCorriente = CuentaCorriente()
    SaldoAhorro = CuentaAhorro()
    CDT = CDT()
    
    # Metodos

    def ConsignarCorriente(self,saldo):
    # Aqui va el codigo del metodo
        return self.SaldoCorriente.ConsignarValor(saldo)
    
    def CalcularSaldos(self):
    # Aqui va el codigo del metodo
        return"su saldo total es:"(self.SaldoAhorro.saldo+self.SaldoCorriente.saldo)
    
    def PasarSaldo(self):
        self.CuentaCorriente= self.SaldoAhorro + self. SaldoCorriente
        return self.SaldoAhorro

    def ConsultarSaldoCorriente(self):
        # Aqui va el codigo del metodo
        return self.SaldoCorriente.saldo()

    def RetirarTodo(self):
        # Aqui va el codigo del metodo
        return":"(self.SaldoCorriente.saldo-self.SaldoAhorro.saldo-self.CDT.saldo)
    
    def DuplicarTodo(self):
        # Aqui va el codigo del metodo
        nahorro= self.CuentaAhorro.saldo *2
        return"Su ahoro es" + nahorro



        

    
    




    