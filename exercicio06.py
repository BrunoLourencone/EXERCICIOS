def cadastrar_filmes(nome, clascificacao, categoria1, categoria2):
    lista = []
    dicionario = {
        "nome" : nome,
        "clascificacao" : clascificacao,
        "categoria" : [categoria1, categoria2]
    }
    lista.append(dicionario)
    return dicionario

print(cadastrar_filmes("de volta pro futuro", 16, "acao", "aventura"))
