print('\nAula 07 - Captura de teclado - Input em Python.\n')

peso = input('Por favor insira o seu peso: ')
altura = input('Insira sua altura para calcular o IMC: ')

# ^ - Realizando a conversão (conversão) de str para number 

peso = float(peso)
altura = float(altura)

# ^ - Foim do bloco de conversão (conversão) de str para number 

imc  = peso/altura
print(f'O seu IMC é: {imc:.3f}')


#^ - Exemplo #2 de captura de teclado e casting 
print('\nCalculando resultado de um operação adição')
numb1 = float(input('Insira o primeiro número: '))
numb2 = float(input('Insira o segundo  número: '))
adicao = numb1 + numb2
print(f'O resultado da soma é: {adicao:.3f}')