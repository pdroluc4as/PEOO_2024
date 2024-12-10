from conta import Conta
from saldoerror import SaldoError

class ContaComum(Conta):
    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoError()
        self.saldo -= valor