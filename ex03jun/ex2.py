# Programa que gera os N primeiros termos da sequência de Fibonacci

while True:
    N = int(input("Digite um número inteiro N (N >= 2): "))
    if N >= 2:
        break
    print("Valor inválido. N deve ser maior ou igual a 2.")

fibonacci = [0, 1]

for i in range(2, N):
    proximo = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(proximo)

print("\nSequência de Fibonacci com", N, "termos:")
print(fibonacci)
