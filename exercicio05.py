from exercicio04 import listaNumerica 

lista = []

def obter_dados_aluno():
    nome = input("informe o nome completo do aluno: ")
    email = input("informe o email do aluno: ")
    serie = input("informe a serie do aluno: ")
    nota1 = int(input("informe a nota1 do aluno: "))
    nota2 = int(input("informe a nota2 do aluno: "))
    nota3 = int(input("informe a nota3 do aluno: "))
    return cadastro(nome, email, serie, nota1, nota2, nota3)

def cadastro(nome, email, serie, nota1=0, nota2=0, nota3=0):

    notas = [nota1, nota2, nota3]

    dicionario = {
        'nome' : nome,
        'email' : email,
        'serie' : serie,
        "notas" : notas,
        "media" : listaNumerica(notas)
    }
    lista.append(dicionario)
    
    return dicionario


obter_dados_aluno()

def  mostrar_dados_alunos(dados_alunos):
    for lista in dados_alunos:
        print(f"nome do aluno: {lista["nome"]}")
    

