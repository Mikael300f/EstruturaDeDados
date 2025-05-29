# Página 15 – Condições Simples

print("Condições Simples")
print("A = 0, B = -3 ->", 0 > -3)
print("X = 3.7 ->", 3.7 <= 10.0)
print("A = 9, B = 16 ->", 9 - 16 >= 0)
print("A = 2, B = 4, N = 10 ->", 2 * 4 < 10)
print("A = 3, B = 9, C = 5 ->", 10 * 3 >= 9 * 5)
print("A = 3, B = 6, C = 5 ->", 10 * 3 >= 6 * 5)
print("N = 7 ->", 7 % 2 == 0)
print("N = 8 ->", 8 % 2 == 0)
print('T = "Morango" ->', "Morango" == "Banana")
print('T = "Morango" > "Banana" ->', "Morango" > "Banana")

# Página 15 – Condições Compostas

print("\nCondições Compostas")
print(10 < 15 and 10 < 4)
print(10 < 15 or 10 < 4)
print(1 >= 0 and 9 == 0)
print(1 >= 0 and 9 == 9)
print(1 >= 0 or 9 == 0)
print(1 >= 0 or 9 == 9)
print(0 != 0 and 0 != 0)
print(0 != 0 and 0 != 25)
print(0 != 0 or 0 != 0)
print(0 != 0 or 0 != 25)

# Página 16 – Condições Mistas

print("\nCondições Mistas")
print(10 < 15 and 10 < 4 or 4 != 0)
print(10 < 15 and (10 < 4 or 4 != 0))
print(not (1 >= 0 and 9 == 0))
print(not (1 >= 0) and not (9 == 9))
print((1 >= 0 or 9 == 0) and 9 > 1)
print(0 == 0 and 1 != 0 and 0 == 0)
print(not (-2 <= 0) or 2 > 0)
print(not (-2 <= 0 or 2 > 0))
print(5 == 0 and 0 != 0 and 0 == 0)
print(5 == 0 or 0 != 0 or 0 == 0)

# Página 16 – Par ou Ímpar

print("\nPar ou Ímpar")
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# Página 17 – Faturamento com valor fixo
print("\nFaturamento Fixo")
salario_fixo = 500.00
vendas = 12398.00
comissao = vendas * 0.06
faturamento = salario_fixo + comissao
print(f"Faturamento: R$ {faturamento:.2f}")

# Página 17 – Faturamento com entrada de teclado
print("\nFaturamento com entrada do usuário")
vendas_usuario = float(input("Digite o valor das vendas do mês: "))
comissao_usuario = vendas_usuario * 0.06
faturamento_usuario = salario_fixo + comissao_usuario
print(f"Faturamento: R$ {faturamento_usuario:.2f}")