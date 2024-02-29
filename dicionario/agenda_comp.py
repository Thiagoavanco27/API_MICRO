agenda = {}
def consulta(agenda, pessoa):
    if pessoa in agenda:
        return agenda[pessoa]
    else:
        return "Pessoa não encontrada na agenda."

def adiciona(agenda, pessoa, telefone, idade):
    agenda[pessoa] = {'Nome': pessoa, 'telefone': telefone, 'idade': idade}

def verifica_pessoa(agenda, pessoa):
    return pessoa in agenda.keys()

def add_pessoa(agenda):
    pessoa = input("digite o nome da pessoa: ")
    telefone = input("digite o telefone: ")
    idade = input("digite a idade: ")
    adiciona (agenda, pessoa, telefone, idade)

adiciona(agenda, "Thiago", 230657, 29)
print(consulta(agenda,"Thiago"))

add_pessoa(agenda)

consultar_nome = input("Nome para consultar: ")
print(consulta(agenda, consultar_nome))

verifica_nome = input("Verifique os dados de:")
print(verifica_pessoa(agenda, verifica_nome))