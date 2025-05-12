#ATIVIDADE 3 - GUSTAVO SANTANA, ADS NOTURNO.
#1:
contadorM20 = 0
contador = 0
soma = 0
print('Questão 1!')
while True:
    num1 = int(input('Digite um numero, caso queira sair digite -1: '))
    if num1 == -1:
        break
    soma += num1
    contador += 1
    
    if num1 > 20:
        contadorM20 += 1
    
media = soma / contador

print(f'A soma dos números digitados é {soma}')
print(f'A media aritmetica é {media:.2f}')
print(f'Houve {contadorM20} números com digito maior que 20!')


print('\nQuestão 2!')
contador = 0
ctAprovados = 0
ctReprovados = 0

while True:
    notas = int(input('Digite sua nota, caso queira sair digite -1: '))
    if notas == -1:
        break
    if notas >= 5:
        ctAprovados += 1
    else:
        ctReprovados += 1
    contador += 1
print(f'Houve {ctAprovados} alunos aprovados e {ctReprovados} alunos REPROVADOS!')
print(f'{contador} alunos fizeram a prova')


print('\nQuestão 3!')
mediapar = 0
mediaImpar = 0 
ctPar = 0
ctImpar = 0
somaPar = 0
somaImpar = 0
while True:
    num1 = int(input('Digite o número, para sair digite 0: '))
    if num1 == 0:
        break
    if num1 % 2 == 0:
        ctPar += 1
        somaPar += num1
    else:
        ctImpar += 1
        somaImpar += num1
mediapar = somaPar/ctPar
mediaImpar = somaImpar/ctImpar
print(f'A media de numeros par é de {mediapar:.2f}, e a media de numeros impares é {mediaImpar:.2f}')
