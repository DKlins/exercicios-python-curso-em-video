quantidade = 0
soma = 0
for x in range (1, 501, 2):
    if x % 3 == 0:
        soma += x
        quantidade += 1
print(f'A soma dos {quantidade} números solicitados é {soma}')