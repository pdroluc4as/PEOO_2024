from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, num, nome, saldo):
        self.num = num
        self.nome = nome
        self.saldo = saldo
        if self.nome == "":
            raise ValueError("Nome do cliente invalido")
    
    def __str__(self):
        return f"Nome do cliente: {self.nome} | Numero da conta: {self.num} | Saldo da conta: {self.saldo}"
    
    def depositar(self, valor):
        if valor <= 0:
            raise("Quantia de deposito invalida.")
        self.saldo += valor

    def sacar(self, valor):
        pass

    def ver_saldo(self):
        return self.saldo
    