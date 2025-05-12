#atv 1
print('Questão 1')
ct = 0

for i in range(0, 14, 1):
    if i == 13:
        print(i, end='.')
        ct += 1
        break
    if i % 2 == 1:
        ct += 1
        print(i, end=', ')
print(f'\nhouve {ct} números gerados...\n')

#atv 2
print('Questão 2')
soma = 0

for i in range(0, 22, 3):
    if i == 21:
        print(i, end='.')
        soma += i
        break
    print(i, end=', ')
    soma += i
print(f'\nA soma dos multiplos de 3 é {soma}')

#atv 3
print('\nQuestão 3')
soma = 0
ct = 0
for i in range(1, 11):
    if i == 10:
        print(i*2, end='.')
    else:
        print(i*2, end=', ')
    soma += i*2
    ct += 1
media = soma/ct
print(f'\nA média do dobro dos números naturais até dez é {media:.0f} e a soma é {soma}')

#atv 4
print('\nQuestão 4')
n = int(input('Digite um valor para a sequencia: '))
ct = 0
for i in range(1, n+1):
    ct += 1
    if i == n:
        print(i, end='.')
        break
    print(i, end=', ')
print(f'\nHouve {ct} valores')

#atv 5
print('\nQuestão 5')
n = int(input('Digite um valor para iniciar sequencia decrescente: '))
ct = 0

for i in range(n, -1, -1):
    ct += 1
    if i == 0:
        print(i, end='.')
        break
    print(i, end=', ')
print(f'\nHouve {ct} valores')   