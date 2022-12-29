
# Durante o looping ele desconsidera o último valor.

for contador in range(1,20,2):
    print('Ler página', contador)
print('Fim')


# range(inicio, fim, passo)
    # inicio    -> número inteiro inicial
    # fim       -> número inteiro final
    # passo     -> quantidade somada em cada loop (assume 1 como padrão)

soma = 0
for i in range(1,9+1,2):
    soma = soma + i
    print('i = {} e soma = {}'.format(i,soma))
print('soma = {}'.format(soma))


print()
print()

# outro exemplo

soma = 0
for i in range(1,3+1):
    n = int(input('Digite um número: '))
    soma += n
    print('n = {} e soma = {}'.format(n,soma))
print('soma = {}'.format(soma))


print()
print()

# novo exemplo com while

fim = 'n'
while fim == 'n':
    print('Ler página')
    fim = input('Terminou?')
print('Fim')

print()
print()
# novo exemplo com while

soma = 0
while soma < 20:
    n = float(input('Digite um número: '))
    soma += n
print('A soma final foi de {:.2f}'.format(soma))


print()
print()
# novo exemplo com while + break

soma = 0
while soma < 20:
    n = float(input('Digite um número: '))
    soma += n
    continua = input('Quer continuar (s/n)? ')
    if continua == 'n':
        break
print('A soma final foi de {:.2f}'.format(soma))



print()
print()

# ###################### EXERCÍCIOS ######################


# Exercício 1 - Digitar 5 "Olás"

passo = range(1,5+1)
for contador in passo:
    print('Olá')
print('Fim')


print()
print()

# Exercício 2 - Ler páginas - Adicionei complemento de informar o número de páginas

qtPaginas = int(input('Quantas páginas deve-se ler hoje?  '))
passo = range(1,qtPaginas+1)
for contador in passo:
    print('Leia a página:', contador)
print('Fim')


print()
print()

# Exercício 3 - Somar 5 números digitados pelo user

soma = 0
qtNum = int(input('Quantaos números devme ser somados?  '))
passo = range(1,qtNum+1)
for contador in passo:
    n = int(input('Digite um número: '))
    soma += n
print('A soma final foi de {:.2f}'.format(soma))

print()
print()

# Exercício 4 - Somar números ímpares consecutivos começando em 1 e terminando em 9

passo = range(1,9+1,2)
soma = 0
for i in passo:
    soma += i
    print('i = {}, e soma = {}'.format(i,soma))
print(soma)


print()
print()

# Exercício 5 - Média de números digitados pelo user

soma = 0
qtNum = int(input('Quantaos números devme ser digitados para a média?  '))
passo = range(1,qtNum+1)
for contador in passo:
    n = float(input('Digite o {}º número: '.format(contador)))
    soma += n
media = soma / qtNum
print('A média final foi de {:.2f}'.format(media))

print()
print()


# Exercício 6 - While - Somar até que passe 20

soma = 0
while soma < 20:
    n = float(input('Digite um número: '))
    soma += n
print('A soma final foi de {:.2f}'.format(soma))

print()
print()


# Exercício 7 - 

soma = 0
while soma < 20:
    n = float(input('Digite um número: '))
    soma += n
    continua = input('Quer continuar (s/n)? ')
    if continua == 'n':
        break
print('A soma final foi de {:.2f}'.format(soma))


print()
print()