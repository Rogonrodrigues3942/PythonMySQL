print('\nAulas 11 e 12 - while - repetition structure.\n')

productName = input('Digite o nome do produto: ')
quantity = int(input('Digite a quantidade; '))
toContinue = input('Deseja inserir mais um cadastro: (sim[s] ou  não[n]): ')

while(toContinue == 's'):
    print(f'Produto: {productName}.')
    toContinue = input('Deseja inserir mais um cadastro: (sim[s] ou  não[n]): ')
    productName = input('Digite o nome do produto: ')
    quantity = int(input('Digite a quantidade; '))

print('\nFim do script.\n')
