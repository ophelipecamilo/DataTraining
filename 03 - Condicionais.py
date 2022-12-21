
# Comparadores de atributos/variáveis
# == Igualdade
# != Diferente
# > Maior
# >= Maior ou igual
# < Menor
# <= Menor ou igual


vontade = input('O que você deseja (Lanche ou Pizza)? : ')
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
vontade = input('O que você deseja (Lanche ou Pizza)? : ')
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