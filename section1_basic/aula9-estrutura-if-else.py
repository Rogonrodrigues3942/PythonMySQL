print('\nAula 09 - Estrutura IF/ELSE.\n')

nomeCandidato = input('Por fvr, insira o seu nome: ')
renda = float(input('Por fvr, insira a sua renda mensal bruta: '))

print(f'Nome do cliente: {nomeCandidato}')
print(f'Salário do cliente: {renda}')

limite = 2000
if renda >= limite:
    print('PARABÉNS! SEU CRÉDITO FOI APROVADO.')
else:
    print(f'SEU CRÉDITO NÃO FOI APROVADO. RENDA ABAIXO DE {limite:.2f}' )