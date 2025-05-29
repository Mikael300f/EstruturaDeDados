a = int(input())
b = int(input())

ok1 = ((a % 2 == 1) and (b % 2 == 0))
ok2 = ((a % 2 == 0) and (b % 2 == 1))

ok = (ok1 or ok2)

print(ok)