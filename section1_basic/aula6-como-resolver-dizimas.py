print('Aula 06 - Como  resolver dízimas.\n')

print('\n\nVenda de produto.\n')
nomeComprador = 'Melissa Rezende'
produto = 'Celular'
precoCell = 1507.27
quantidade = 3
total = quantidade * precoCell

print(f'Nome do cliente: {nomeComprador}')
print(f'Produto: {produto}')
print(f'Quantidade: {quantidade}')
print(f'Preço da unnidade: {precoCell:.2f}')
print(f'Total a pagar: R$ {total:.2f}')

print('\n')

print('Cálculo de índice de massa corporal (imc).\n')
peso = 92
altura = 1.74
imc = peso/altura
print(f'O seu IMC é: {imc:.3f} ')