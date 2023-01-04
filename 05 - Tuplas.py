
# Tuplas = variáveis com mais de um valor

tuplas = ['Teste1', 'Teste2', 'Teste3']
print(tuplas)

tupla1 = ('Lanche','Batata','Refri')
tupla2 = (2, 6, 4, 5, 7)
tupla3 = (True, False , False)
tupla4 = ('Lanche',10.9, False, 2)

print(type(tupla4))
print(type(tupla4[0]))
print(type(tupla4[1]))
print(type(tupla4[2]))
print(type(tupla4[3]))
print()
print()

t1 = (0, 6, 4, 2, 8)
t2 = (1, 3, 3, 5, 3, 5, 7, 3)

print('Tupla 1:', t1)
print('Tupla 2:', t2)


len(t1)
print(len(t1))
sorted(t1)
print(sorted(t1))

t2.count(3)  # Contar quantas vezes o 3 aparece no t2
print(t2.count(3))

t2.index(7)  # Verificar o index do valor 7 aparece no t2
print(t2.index(7))

t2.index(3)  # Verificar o index do valor 3 aparece no t2
print(t2.index(3))

t2.index(3,4)  # Verificar o index do valor 3 aparece no t2 a partir da posição 4
print(t2.index(3,4))


# não é possível somar Tuplas... neste caso somente concatenar as duplcas

tt = t2 + t1
print(tt)


# é possível somar os valores das posições das Tuplas

tt = t1[2] + t2[1]
print(tt)

# Acessando múltiplos valores com [A:B]

print(t2[0:2]) # os 2 primeiros valores da tupla
print(t2[2:4]) # são os valores 3º e 4º da tupla
print(t2[:3]) # considera início até a posição informada
print(t2[3:]) # considera a posição até o final da tupla
print(t2[-1]) # considera o último termo da tupla

print()
print()

# Funções com Tuplas

# len()              -> Qtd de termos
# sorted()           -> Ordernar
# .count("valor")    -> Contar a qtd de "valor"
# .index("valor")    -> achar a posição de "valor"
# index("valor","pos") -> achar "valor" a partir da posição

t1 = ('Lanche','Batata','Refri')
t2 = (0,6,4,2,8,6,4)
t3 = (1,3,3,5,3,5,7)

# verificar tamanho das tuplas

print(len(t1))
print(len(t2))

# imprimir tuplas ordenadas

print(sorted(t1))
print(sorted(t2))
print(sorted(t3))

# contar quantas vezes aparece 3 na t3

print(t3.index(3))

# Aonde aparece 'Refri' na t1

print(t1.index("Refri"))

# Verificar o valor

print(t1.count('Refri'))

# Procurar o valor 5 na t3 após o 4º termo

print(t3.index(5,4))

# Concatenar as tuplas t2 e t3 e depois t3 e t2

print(t2 + t3)
print(t3 + t2)

# ordernar tuplas concatenadas

print(sorted(t3+t2))

# Tuplas dentro de For

for i in t1:
    print('Temos no nosso cardápio: {}'.format(i))
print('Fim do cardápio')

# Exercício 2

print(t2)
soma = 0
for i in t2:
    soma += i
print(soma)

# Trabalhando com o Enumarate()

print(t1)
for i, v in enumerate(t1):
    print('Na posição = {}, temos o valor = {}'.format(i,v))
print('Fim')

print()
print()

# Exercícios

# 1
t1 = ('Doce','Churrasco','Bala','Tapioca','Pizza','Feijão',
        'Arroz','Açaí','Paçoca','Acarajé','Pamonha','Dobradinha','Rapadura')


pedido = input('Digite o item que deseja:  ' )

if t1.count(pedido) > 0:
    print('Foi selecionado o item:', t1.index(pedido),' - ', pedido)
else: print('O item escolhido não consta no cardápio')

print('Itens do cardápio:')
print(sorted(t1))

print()
print()

# 2

t1 = ('Doce',2.3,'Bala',0.15,'Pizza',28.9,'Arroz',4.5,'Paçoca',0.5,'Pamonha',5.4)

ver_card = input('Deseja visualizar o cardápio? (S/N)  ')
if ver_card == 'S':
    print('*'*35)
    print('*'*12,'Cardápio','*'*13)
    print('*'*35)

    n0 = 0
    n1 = 1
    total = len(t1)
    i = 0
    L = 1
    while True:
        print('{} - {:.<20} : R$ {:>5.2f}'.format(L,t1[n0],t1[n1]))
        n0 += 2
        n1 += 2
        i += 2
        L += 1
        if i == total:
            break
print('*'*35)
print()
print()

soma = 0
algoMais = 'S'
while algoMais == 'S':
    valorPedido = int(input('Qual o item você deseja? '))
    qtdPedido = int(input('Quanto você deseja? '))
    n = (valorPedido*2) -1
    totalPedido = t1[n] * qtdPedido
    soma += total
    algoMais = input('Deseja algo mais? ')
print('O valor total do seu pedido foi de R$ {:.2f}'.format(totalPedido))