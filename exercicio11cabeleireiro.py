import json
import os

data = "agenda_cabeleireiro.json"

def carregar_dados():
    if os.path.exists(data):
        with open(data, "r", encoding="utf-8")as arq_json:
            return json.load(arq_json)
    else:
        return []

def obter_dados():
    nome_cliente = input('nome do cliente: ')
    servico_cliente = input('serviço do cliente: ')
    data_cliente = input('data de agendamento: ')
    horario_cliente = input('horario do agendamento: ')
    observacao_cliente = input('observações do cliente: ')

    cabelo = {
        'nome cliente': nome_cliente,
        'servico cliente': servico_cliente,
        'data cliente': data_cliente,
        'horario cliente': horario_cliente,
        'observacao cliente': observacao_cliente,
            }
    return cabelo

def cadastrar_agendamento(dadosAgendado):
    agendar = carregar_dados()
    agendar.append(dadosAgendado)

    with open(data, "w", encoding="utf-8")as arq_json:
        json.dump(agendar, arq_json, ensure_ascii=False, indent=4)


def mostrar_agendamento(dadosAgendado):
    if dadosAgendado:
        for cabelo in dadosAgendado:
            print("<>"*80)
            print(f"""
                  nome cliente: {cabelo['nome_cliente']}
                  servico cliente: {cabelo['servico_cliente']}
                  data cliente: {cabelo['data_cliente']}
                  horario cliente: {cabelo['horario_cliente']}
                  observacao cliente: {cabelo['observacao_cliente']}
                 """)
    else:
        print('nenhum agendamento foi feito ainda')


def iniciar_sistema():
    agendar = carregar_dados()
    while True:

        print('')
        print('<>'*20)
        print("opcao 1 - mostrar agenda completa. ")
        print('opcao 2 - cadastrar um novo agendamento. ')
        print('opcao 3 - sair do sistema. ')
        print('<>'*20)

        opcoes = input('escolha uma das 3 opções para iniciar o sistema: ')

        if opcoes == '1':
            mostrar_agendamento(agendar)
        elif opcoes == '2':
            cadastrar_agendamento(obter_dados())
        elif opcoes == '3':
            print('seu sistema foi finalizado! ate a proxima')
            break
        else:
            print('essa opção nao existe, por favor tente novamente')

iniciar_sistema()


