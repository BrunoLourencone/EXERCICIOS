import json
import os
cadastro = "CadastroDeFimes.json"

def cadastrarFilmes():
    if os.path.exists(cadastro):
        with open(cadastro, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return[]

def ObterCadastroFilme():
    filme = input("nome do filme: ")
    Classificacao = input("classificação do filme: ")
    data = input("lançado em: ")
    tempo = input("duração do filme: ")
    descricao = input("descrição do filme: ")

    filmes = {
        "filme": filme,
        "classificacao": Classificacao,
        "data": data,
        "tempo": tempo,
        "descricao": descricao
    }

    return ObterCadastroFilme

def cadastrar_filme(dadosFilme):
    filmes = cadastrarFilmes()
    filmes.append(dadosFilme)


def mostrarDados_filme():
    for filmes in ObterCadastroFilme:
        print(f"""
              nome do filme: {filmes["nome do filme"]}
              classificacao do filme: {filmes["classificacao do filme"]}
              data do filme: {filmes["lançamento do filme"]}
              tempo do filme: {filmes["duração do filme"]}
              descricao do filme: {filmes["descrição do filme"]}
              """)


mostrarDados_filme()