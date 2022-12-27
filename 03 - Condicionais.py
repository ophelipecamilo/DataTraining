
# Comparadores de atributos/variáveis
# == Igualdade
# != Diferente
# > Maior
# >= Maior ou igual
# < Menor
# <= Menor ou igual


vontade = 'Pizza' # input('O que você deseja (Lanche ou Pizza)? : ')
if vontade == 'Lanche':
        print('Ir ao Méqui')
        print('Comer Lanche')
        print('Fome Satisfeita')
else: 
    if vontade == 'Pizza':
        print('Ir ao Hut')
        print('Comer Pizza')
    else:
        print('Ir ao Bell')
        print('Comer Tacos')
print('Fome Satisfeita')
print()
print()
vontade = 'Lanche' # input('O que você deseja (Lanche ou Pizza)? : ')
if vontade == 'Lanche':
        print('Ir ao Méqui')
        print('Comer Lanche')
        print('Fome Satisfeita')
elif vontade == 'Pizza':
        print('Ir ao Hut')
        print('Comer Pizza')
elif vontade == 'Tacos':
        print('Ir ao Bell')
        print('Comer Tacos')
elif vontade == 'Nao':
    print('Sem Fome')

# Teste de Variável
# .isnumeric()  input é numérico
# .isalpha()    input é texto
# .isalnum()    input é texto + num

#Exemplo 2

a = 3 # float(input('Digite um número: '))
b = 3 # float(input('Digite outro número: '))

if a == b:
        print('A é igual a B')
elif a<b:
        print('A é menor que B')
else:
        print('A é maior que B')
print('Fim')


# Exercício 1

a = input('Digite algo: ')
# print(a.isnumeric()) validação
if a.isnumeric() == True:
        print('Esse input é um número')
else: print('Esse input não é um número, tente novamente')

print()
print()

# Exercício 2

a = input('Digite um número: ')
if a.isnumeric() == True and (float(a) % 2 == 0):
        print('O número é par!')
elif a.isnumeric() == False:
        print('Não foi digitado um número')
else:
        print('O número não é par!')

print()
print()

# Exercício 3

a = 71 # float(input('Digite um número: '))
b = 33 # float(input('Digite outro número: '))

if a % b == 0 and b % a == 0:
        print('Os números são divisiveis entre si')
elif a % b == 0:
        print('O número A é divisível por B')
elif b % a == 0:
        print('O número B é divisível por A') 
else: print('Os números não são divisiveis')

print()
print()

# Desafio da Calculadora 

a = 71 # float(input('Digite um número: '))
b = 33 # float(input('Digite outro número: '))

print('Operações: Soma, Subtração, Divisão, Multiplicação ou Potência')
c = input('Digite a operação matemática : ')

if c == 'Soma':
        print(a + b)
elif c == 'Subtração':
        print(a - b)
elif c == 'Divisão':
        print(a / b)
elif c == 'Multiplicação':
        print(a * b)
elif c == 'Potência':
        print(a ** b)
else: print('Operação inválida')

print()
print()

# Exercício de Condicionais

# 1

nome = input('Digite o seu nome: ')
dtNasc = input('Digite o seu ano de nascimento: ')

if (2022 - int(dtNasc) >= 18):
        print('Librado a compra de bebida alcólica')
else: print('Menor de idade!!!! Não vender bebida alcólica')

print()
print()

# 2

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

if (nota1 + nota2 + nota3) / 3 >= 8:
        print('Aprovado!')
else: print('Reprovado.')

print()
print()

# 3

altura = float(input('Qual a sua altura? '))

if altura % 2 == 0:
        print('Sua altura é par')
else: print('Sua altura é ímpar')

print()
print()

# 4

a = int(input('Digite um número que representa um dia entre 1 e 365:  '))

if a >= 1 and a <= 90:
        print('O seu dia está no primeiro trimestre')
elif a >= 91 and a <= 180:
        print('O seu dia está no segundo trimestre')
elif a >= 181 and a <= 270:
        print('O seu dia está no terceiro trimestre')
elif a >= 271 and a <= 365:
        print('O seu dia está no quarto trimestre')
elif a >= 365 and a <= 0:
        print('Número do dia inválido')
else: print('Número inválido')

# 5

a = 71 # float(input('Digite um número: '))
b = 83 # float(input('Digite outro número: '))
c = 81

if a == b and b != c:
        print('Temos números iguais, ', a, ' e ', b)
elif b == c and a != c:
        print('Temos números iguais, ', b, ' e ', c)
elif a > b and a > c and a != b and b != c:
        print('O número A é o maior')
elif b > a and b > c and a != b and b != c:
        print('O número B é o maior')
elif c > b and c > a and a != b and b != c:
        print('O número C é o maior')
else: print('Núemros inválidos')

print()
print()