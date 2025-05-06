def listaNumerica(lista):
    somar = 0
    for i in lista:
        somar += i
    return somar

numeros_ale = [9, 23, 76, 19, 10, 25, 20]
resultado = listaNumerica(numeros_ale)
print(resultado)
 