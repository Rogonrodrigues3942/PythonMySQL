print('\nAula 08 - Exemplo completo - Programando com Pyhton na Prática.\n')

produto = 'Computador'
preco = 201.99
quantidade = input('Digite quantas unidades deseja comprar: ')
resultado = int(quantidade) * preco
nomeCliente = input('Digite seu nome completo: ')
doctoCliente = input('Insira seu documento de identidade: ')

print('\nDados da compra')
print(f'Produto: {produto}')
print(f'Preço unitário: R$ {preco}')
print(f'Unidades compradas: {quantidade}; o valor total da compra: {resultado:.2f}')
print(f'Cliente (Emissão Nota Fiscal): {nomeCliente}')
print(f'Documento do cliente: {doctoCliente}')
