n = int(input())

sequence = []

for itm in range(1, n+1):
    mul = min(n, itm)
    n = n - mul
    sequence += [str(itm)] * mul
    if n <= 0:
        break

print("".join(sequence))
