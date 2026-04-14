print('\nAula 10 - Estrutura IF/ELSE com AND e OR.\n')

nomeCandidato = input('Por fvr, insira o seu nome: ')
sobrenomeCandidato = input('Por fvr qual seu sobrenome: ')
idadeCandidato = int(input(f'Qual sua idade {nomeCandidato}: '))
renda = float(input('Por fvr, insira a sua renda mensal bruta: '))

print(f'\nNome do cliente: {nomeCandidato} {sobrenomeCandidato}.')
print(f'Idade do candedato:  {idadeCandidato}.')
print(f'Salário do cliente: {renda:.2f}.')

limite = 2000

if idadeCandidato >= 65 or renda >= limite and idadeCandidato >= 18:
    print('PARABÉNS! SEU CRÉDITO FOI APROVADO.')
else:
    print(f'SEU CRÉDITO NÃO FOI APROVADO. RENDA ABAIXO DE {limite:.2f}' )