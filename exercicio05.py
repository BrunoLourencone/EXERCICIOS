def cadastro(nome, email, serie):
    lista = []
    dicionario = {
        'nome' : nome,
        'email' : email,
        'serie' : serie
    }
    lista.append(dicionario)
    return dicionario

print(cadastro("bruno", "brunolourencone12@gmail.com", "2tb"))
