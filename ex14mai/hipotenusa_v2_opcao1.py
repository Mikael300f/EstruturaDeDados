a_str = input("Digite um valor para o cateto a: ")
b_str = input("Digite um valor para o cateto b: ")

a = float(a_str)
b = float(b_str)

c = ((a * a) + (b * b)) ** (1 / 2)
print(c)