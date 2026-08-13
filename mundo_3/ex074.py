from random import randint
numbers = (randint(1, 10) , randint (1, 10), randint(1,10), randint(1,10), randint(1,10))
print(f'Cinco números aleatórios gerados:', end=' ')
for numero in numbers:
    print(numero, end= '')
print(f'\nO maior valor sorteado foi {max(numbers)} \nO menor valor sorteado foi {min(numbers)}')
