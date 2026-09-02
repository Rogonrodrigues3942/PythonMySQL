
print('\nAulas 11 e 12 - while - repetition structure.\n')

toContinue = input('Deseja inserir mais um cadastro: (sim[s] ou  não[n]): ')

if(toContinue == 'n' or toContinue == 'N'):
    print('\nPrograma encerrado!\n')
    exit()


productName = input('Digite o nome do produto: ')
quantity = int(input('Digite a quantidade; '))

while(toContinue == 's' or toContinue == 'S'):
    print(f'Produto: {productName}.')
    print(f'Quantidade: {quantity}.')
    toContinue = input('Deseja inserir mais um cadastro: (sim[s] ou  não[n]): ')

    if(toContinue == 'n' or toContinue == 'N'):
        print('\nPrograma encerrado!\n')
        exit()

    productName = input('Digite o nome do produto: ')
    quantity = int(input('Digite a quantidade; '))
    
print('\nFim do script.\n')
