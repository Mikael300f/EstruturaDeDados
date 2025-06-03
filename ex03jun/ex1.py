# Programa que lê números inteiros e insere em uma lista
# na posição anterior ao primeiro elemento maior ou igual

lista = []

while True:
    numero = int(input("Digite um número inteiro (0 para sair): "))
    
    if numero == 0:
        break

    inserido = False
    for i in range(len(lista)):
        if numero <= lista[i]:
            lista.insert(i, numero)
            inserido = True
            break

    if not inserido:
        lista.append(numero)

print("\nLista final:")
print(lista)