class SaldoError(Exception):
    def __init__(self, mensagem="Saldo insuficiente para realizar a operação."):
        super().__init__(mensagem)