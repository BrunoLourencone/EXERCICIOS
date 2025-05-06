def verficar_idade(nome, idade):
    if idade >= 18:
        return f"{nome} é maior de idade"
    else:
        return f"{nome} é menor de idade"
    
nome = input('digite seu nome: ')
idade = int(input('digite sua idade: '))

resultado = verficar_idade(nome, idade)

print(resultado)

