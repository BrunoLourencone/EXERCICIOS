from exercicio04 import listaNumerica 

def cadastro(nome, email, serie, nota1, nota2, nota3):
    lista = []

    notas = [nota1, nota2, nota3]

    dicionario = {
        'nome' : nome,
        'email' : email,
        'serie' : serie,
        "notas" : notas,
        "media" : listaNumerica(notas)
    }
    lista.append(dicionario)
    media = listaNumerica(dicionario["notas"])
    return dicionario

print (cadastro("bruno", "brunolourencone12@gmail.com", "2TB", 10, 23, 7))
