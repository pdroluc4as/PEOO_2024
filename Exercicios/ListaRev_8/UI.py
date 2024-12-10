from conta import Conta
from contacomum import ContaComum
from contaespecial import ContaEspecial
from poupança import ContaPoupanca
from saldoerror import SaldoError

class UI:
    def main():
        print("\nSistema Bancario\n")
        contas = []

        while True:
            print("1. Criar Conta Comum\n")
            print("2. Criar Conta Especial\n")
            print("3. Criar Conta Poupança\n")
            print("4. Realizar Depósito\n")
            print("5. Realizar Saque\n")
            print("6. Verificar Saldo\n")
            print("7. Listar Contas\n")
            print("0. Sair\n")

            op = int(input("Escolha uma opção: "))
        #CONTA COMUM
            if op == 1:
                num = input("Informe o numero da conta: ")
                nome = input("Informe o nome da conta: ")
                saldo = int(input("Informe o saldo inicial da conta: "))
                try:
                    conta = ContaComum(num, nome, saldo)
                    contas.append(conta)
                    print("Conta criada com sucesso!")
                except ValueError as e:
                    print(f"Erro: {e}")
        #CONTA ESPECIAL    
            elif op == 2:
                num = input("Informe o numero da conta: ")
                nome = input("Informe o nome da conta: ")
                saldo = int(input("Informe o saldo inicial da conta: "))
                limite = int(input("Informe o limite da conta: "))
                try:
                    conta = ContaEspecial(num, nome, saldo, limite)
                    contas.append(conta)
                    print("Conta especial criada com sucesso!")
                except ValueError as e:
                    print(f"erro: {e}")
        #CONTA POUPANÇA
            elif op == 3:
                num = input("Informe o numero da conta: ")
                nome = input("Informe o nome do cliente: ")
                try:
                    conta = ContaPoupanca(num, nome)
                    contas.append(conta)
                    print("Conta poupança criada com sucesso!")
                except ValueError as e:
                    print(f"Erro: {e}")
            
            elif op in [4, 5 , 6]:
                num = input("Informe o numero da conta: ")
                conta = None
                for c in contas:
                    if c.num == num:
                        conta = c
                        if conta != None:
                            print(f"conta encontrada: {conta}")
                        break
                if not conta:
                    print("Conta não encontrada.")
                    continue

                elif op == 4:
                    valor = float(input("Valor do depósito: "))
                    
                    if isinstance(conta, ContaPoupanca):
                        data = input("Data do depósito (DD/MM/AAAA): ")
                        conta.depositar(valor, data)
                    
                    else:
                        conta.depositar(valor)
                    print("Depósito realizado com sucesso!")
                
                elif op == 5:
                    valor = float(input("Valor do saque: "))
                    try:
                        conta.sacar(valor)
                        print("Saque realizado com sucesso!")
                    except SaldoError as e:
                        print(f"Erro: {e}")
                
                elif op == 6:
                    print(f"Saldo atual: R$ {conta.ver_saldo():.2f}")
            
            elif op == 7:
                for c in contas:
                    print(c)
                if not contas:
                    print("lista vazia")
            elif op == 0:
                print("Obrigado por usar o sistema bancário!")
                break
UI.main()