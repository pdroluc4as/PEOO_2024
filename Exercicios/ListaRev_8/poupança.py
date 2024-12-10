from conta import Conta
from saldoerror import SaldoError


class ContaPoupanca(Conta):
    def __init__(self, numero, nome_cliente):
        super().__init__(numero, nome_cliente, 0)
        self.saldos_por_dia = []  # Lista de (data, saldo)

    def depositar(self, valor, data):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.saldos_por_dia.append((data, valor))
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoError()

        saldo_restante = valor
        for i in range(len(self.saldos_por_dia)):
            data, saldo_dia = self.saldos_por_dia[i]
            if saldo_dia >= saldo_restante:
                self.saldos_por_dia[i] = (data, saldo_dia - saldo_restante)
                break
            else:
                saldo_restante -= saldo_dia
                self.saldos_por_dia[i] = (data, 0)

        # Remove saldos zerados
        self.saldos_por_dia = [(d, s) for d, s in self.saldos_por_dia if s > 0]
        self.saldo -= valor
