cidade = str(input('Digite o nome da cidade: ')).strip()
city = cidade.split()
print(f'O nome da cidade começa com "Santo": {'santo' in city[0].lower()}')