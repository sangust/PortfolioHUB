

#atv 1
print('Questão 1')
print('Fahreinheit | Celsius ')
for i in range(45, 81):
    f = float(i)
    c = float(5/9 * (f-32))
    print(f'{f}ºF | {c:.2f} ºC')
    f += 1

#atv 2
print('\nQuestão 2')
fahr_inicial = int(input('Digite o valor de graus fahrenheit inicial: '))
fahr_final = int(input('Digite o valor de graus fahrenheit final: '))
if fahr_inicial <= fahr_final:
    for i in range(fahr_inicial, fahr_final):
        f = float(i)
        c = float(5/9 * (f-32))
        print(f'{f}ºF | {c:.2f} ºC')
        f += 1
else:
    for i in range(fahr_inicial, fahr_final-1, -1):
        f = float(i)
        c = float(5/9 * (f-32))
        print(f'{f}ºF | {c:.2f} ºC')
        f += 1

#atv 3
print('\nQuestão 3')
soma = 0
for i in range(1, 501):
    soma += i
print(f'A soma de 1 a 500 é {soma}')

#atv 4
print('\nQuestão 4')
soma = 0
for i in range(1, 500, 3):
    if i % 2 == 1:
        soma += 1
print(f'A soma dos multiplos de 3 impares é {soma}')

#atv 5
print('\nQuestão 5')
for i in range(1, 11):
    print(f'{i} x 5 = {i*5}')

#atv 6
print('\nQuestão 6')
mult = int(input('Digite um valor para ver sua tabuada: '))
for i in range(1, 11):
    print(f'{i} x {mult} = {i*mult}')