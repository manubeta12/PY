class CuentaAhorro:
    saldo=""
    InteresMensual=""
#aqui va el codigo de CuentaAhorro
def ConsignarValor (self):
    nsaldo= self.saldo + 100000
    self.saldo= nsaldo
    return" El nuevo saldo mas el valor consignado es" + self.saldo 
def RetirarValor(self):
    nSaldo= self.saldo - 100000
    self.saldo = nSaldo
    return" El nuevo saldo menos el valor retirado es" + self.saldo 
def InteresMensual (self):
    nSaldo= self.saldo * 0.6
    nSaldo= self.saldo + nSaldo
    self.saldo = nSaldo
    return" El nuevo saldo mas el inetres mensual es" + self.saldo

