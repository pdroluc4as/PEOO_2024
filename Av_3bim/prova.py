from datetime import datetime

class Usuario:
    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha

    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email

    def get_senha(self):
        return self.__senha
    def set_senha(self, senha):
        self.__senha = senha

class NascimentoError(Exception):
    def __init__(self, data):
        super().__init__()
        self.__data = data
    def get_data(self):
        return self.__data

class Aluno(Usuario):
    def __init__(self, email, senha, nome, dn):
        super().__init__(email, senha)
        self.__nome = nome
        self.set_nascimento(dn)

    def get_nascimento(self):
        return self.__nascimento
    def set_nascimento(self, dn):
        self.__nascimento = dn
        if dn > datetime.now():
            raise NascimentoError(dn)
    
    def mes_aniversario(self):
        self.__nascimento.month

    def To_dict(self):
        dic = {}
        dic["email"] = self.get_email()
        dic["senha"] = self.get_senha()
        dic["nome"] = self.__nome
        dic["nascimento"] = self.__nascimento.strftime("%d/%m/%Y")
        return dic

def main():
    email = input("Informe o email: ")
    senha = input("Informe a senha: ")
    nome = input("Informe o nome: ")
    data = datetime.strptime(input("Informe a data de nascimento(d/m/Y): "), "%d/%m/%Y")
    try:
        aluno = Aluno(email, senha, nome, data)
        print(aluno.get_email())
        print(aluno.get_senha())
        print(aluno.get_nascimento())
        print(aluno.mes_aniversario())
        print(aluno.To_dict())
    except NascimentoError as erro:
        print("Data não pode estar no futuro:")
        print(erro.get_data())

main()
