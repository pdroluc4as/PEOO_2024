from conta import Conta
from saldoerror import SaldoError

class ContaEspecial(Conta):
    def __init__(self, num, nome, saldo, limite):
        super().__init__(num, nome, saldo)
        self.limite = limite
    
    def sacar(self, valor):
        if valor > self.limite + self.saldo:
            raise SaldoError()
        self.saldo -= valor