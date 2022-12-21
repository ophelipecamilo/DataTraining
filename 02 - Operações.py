

# Operadores
# + Soma 
# - Subtração
# * Multiplicação
#  / Divisão
# ** Potência
# // Divisão inteira
# % resto da divisão
# == Igualdade


print('-'*21)
print(' '*6 + 'Bem Vindo!' + ' '*4)
print('-'*21)
print()
nascimento_teste = 1996 # input('Qual o ano de nascimento?')
idade = 2022 - int(nascimento_teste)
print(idade)
print()
print()
a = 2
b = 3
print('Primeira variáve {}, segunda variável {}, e terceira variável'.format(a,b))
print()
print()
a = 245
b = 2.835895
print('|{0:10d}| e | {1:10.2f}|'.format(a,b))
# 0 -> posição da variável dentro do format
# : -> separador
# 10 -> separar 10 espaços para o número
# d -> número inteiro
# . -> separador decimal
# 4f -> limitar em 4 floats
print()
print()
print('-'*21)
print(' '*5 + 'Exercícios!' + ' '*5)
print('-'*21)
print()
print()
a = 7
b = 2
print('Número 1: {}, e número 2: {}'.format(a,b))
soma = a + b
print('Soma: {}'.format(soma))
subtracao = a - b
print('Subtração: {}'.format(subtracao))
multiplicacao = a * b
print('Multiplicação: {}'.format(multiplicacao))
divisao = a / b
print('Divisão: {}'.format(divisao))
potencia = a ** b
print('Potência: {}'.format(potencia))
divisao_inteira = a // b
print('Divisão inteira: {}'.format(divisao_inteira))
resto_div = a % b
print('Resto da divisão: {}'.format(resto_div))
print()
print()
print('Olá '*5)
print()
print()
print('_' *60)
print(' ' *10, 'Seja Bem Vindo ao curso de Python da DNC!')
print('_' *60)
print()
print()
a = 5
b = 7
c = 3.45
d = 5.50
print(a + b * d)
print((a + b)* d)
print(b ** a * c)
print(b ** (a * c))
print()
print()
lanchePreco = 10.90
lancheQtd = 2
refriPreco = 4.5
refriQtd = 3
batataPreco = 8.45
batataQtd = 1
# Resposta Item 1
totalConta = (lanchePreco * lancheQtd) + (refriPreco * refriQtd) + (batataPreco * batataQtd)
print('1. Qual foi o valor total da conta? R$',totalConta)
# Resposta Item 2
nota10Qtd = totalConta // 10
valorFaltante = totalConta - nota10Qtd * 10
print('2. Quantas notas de 10 reais eu usei? ', nota10Qtd)
# Repostas Item 3
nota5Qtd = valorFaltante // 5 + 1
valorFaltante = valorFaltante - nota5Qtd * 5
print('3. Quantas notas de 5 reais eu usei? ', nota5Qtd)
# Respostas Item 4
nota2Qtd = (-valorFaltante) // 2
valorFaltante = valorFaltante + nota2Qtd * 2
print('2. Quanto voltou de troco para mim em notas? ', nota2Qtd)
# Reposta Item 5
moedaValor = 0 - valorFaltante
valorFaltante = moedaValor + valorFaltante
print('5. Quanto voltou de troco para mim em moedas? ', valorFaltante)
print()
print()
a = 1.857
b = '4'
c = True
d = False
e = 'tex34'
print('Variável {}, para inteiro será: '.format(a),int(a))
print()
print()
# Tabuada
numeroInteiro = input('Digite um número inteiro para tabuada: ')
if type(numeroInteiro) == type(2.5) : print('Número decimal, retorne e digite um número inteiro!') 
else: print('Tabuada de: ',int(numeroInteiro))

for i in range(1,11):
    if type(numeroInteiro) == type(2.5) : print()
    else: print(int(numeroInteiro), ' x ', i, ' = ', int(numeroInteiro) * i)