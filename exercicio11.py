import json
import os

data = "cadastro_veiculos.json"

def carregar_dados():
    if os.path.exists(data):
        with open(data, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []


def obter_dados():
    marca = input("Digite a marca do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    ano = input("Digite o ano de fabricação: ")
    cor = input("Digite a cor do veículo: ")

    carro = {
        'marca': marca,
        'modelo': modelo,
        'ano': ano,
        'cor': cor
    }
    return (carro)

def cadastrar_veiculo(dados_veiculo):
    carros = carregar_dados()
    carros.append(dados_veiculo)

    with open(data, "w", encoding="utf-8")as arq_json:
        json.dump(carros, arq_json, ensure_ascii=False, indent=4)


def mostrar_veiculos(dados_veiculo):
    if dados_veiculo:
         for carro in dados_veiculo:
            print("="*80)
            print(f"""
                Marca: {carro['marca']}
                Modelo: {carro['modelo']}
                Ano de Fabricação: {carro['ano']}
                Cor: {carro['cor']}
                """)

    else:
        print('Nenhum veículo cadastrado no momento')

def iniciar_sistema():
    carros = carregar_dados()
    while True :

        print(" ")
        print("="*80)
        print("opção 1 - mostrar lista de veiculos")
        print("opção 2 - cadastrar novo veiculo")
        print("opção 3 - sair do sistema")
        print("="*80)

        escolha = input('escolha uma das opção para iniciar: ')

        if escolha == "1":
            mostrar_veiculos(carros)
        elif escolha == "2":
            cadastrar_veiculo(obter_dados())
        elif escolha == "3":
            print('seu sistema foi finalizado. até a proxima!')
            break
        else:
            print('essa escolha é invalida, por favor tente novamente')


iniciar_sistema()
