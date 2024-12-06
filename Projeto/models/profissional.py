from models.crud import CRUD
import json

class Profissional:
    def __init__(self, id, nome, especialidade, conselho):
        self.id = id
        self.nome = nome
        self.especialidade = especialidade
        self.conselho = conselho
    
    def __str__(self):
        return f"{self.nome} - {self.especialidade} - {self.conselho}"
    

class Profissionais(CRUD):

  @classmethod
  def salvar(cls):
    with open("profissionais.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, indent=4, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("profissionais.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          p = Profissional(obj["id"], obj["nome"], obj["especialidade"], obj["conselho"])
          cls.objetos.append(p)
    except FileNotFoundError:
      pass