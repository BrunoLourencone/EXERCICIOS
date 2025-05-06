def cadastro(nome, email, serie, nota1, nota2, nota3):
    lista = []
    dicionario = {
        'nome' : nome,
        'email' : email,
        'serie' : serie,
        "notas" : [nota1, nota2, nota3]
    }
    lista.append(dicionario)
    return dicionario

print(cadastro("bruno", "brunolourencone12@gmail.com", "2tb", 10, 9, 5))
