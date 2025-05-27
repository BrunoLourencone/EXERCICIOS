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
    data = int(input("lançado em: "))
    tempo = input("duração do filme: ")
    descricao = input("descrição do filme: ")

    filmes = {
        "filme": filme,
        "classificacao": Classificacao,
        "data": data,
        "tempo": tempo,
        "descricao": descricao
    }

    return filmes

def cadastrar_filme(dadosFilme):
    filmes = cadastrarFilmes()
    filmes.append(dadosFilme)

    with open(cadastro, "w", encoding="utf-8")as arq_json:
        json.dump(filmes, arq_json, indent=4, ensure_ascii=False)



def mostrarDados_filme():
    if cadastro:
        for filmes in ObterCadastroFilme():
            print(f"""
                nome do filme: {filmes["filme"]}
                classificacao do filme: {filmes["classificacao"]}
                data do filme: {filmes["data"]}
                tempo do filme: {filmes["tempo"]}
                descricao do filme: {filmes["descricao"]}
                """)
    else:
        print('nao existe nenhum filme cadastrado.')


def inciar_sistema():
    filmes = cadastrarFilmes()
    while True:
        
        print(" ")
        print("="*80)
        print("opção 1 - mostrar lista de filmes")
        print("opção 2 - cadastrar filmes")
        print("opção 3 - sair do sistema")
        print("="*80)

        opcao = input("escolha uma das opções do menu: ")

        if opcao == "1" :
            mostrarDados_filme(filmes)
        elif opcao == "2" :
            cadastrar_filme(ObterCadastroFilme())
        elif opcao == "3" :
            print("sistema finalizado.")
        else:
            print("opcao invalida, escolha uma das opções dos menos")

inciar_sistema()

