from math import sqrt
print('Trabalho feito pelo aluno Gustavo Santana (APP --> VISUAL STUDIO CODE) - ADS Noturno')
#1.	Implemente o programa que calcule o volume de uma esfera de raio R. O usuário fornecerá o dado necessário.
print('-'*8,'Exercicio número 1','-'*8)
raio = float(input(f'Para descobrir o volume de uma esfera, digite o seu raio (em centimetros) abaixo:\n '))
pi = 3.14
volume = 4/3 * pi * raio**3  

print(f'O volume da esfera de raio {raio:.0f}, é {volume:.2f}cm^3\n')


#2. - A água é um nutriente essencial. Sem ela, o corpo não pode funcionar com perfeição. Cada pessoa precisa 
# de uma quantidade diferente de água para hidratar o corpo. A dose ideal, ou seja, a necessidade diária em 
# litros é calculada através da fórmula: massa (em kg) vezes 0,03. Elabore o programa que realize esse cálculo. 

print('-'*8,'Exercicio número 2','-'*8)

massa = float(input(f'Para descobrir a quantidade ideal de litros de água a ser ingerida diariamente\nDigite seu peso em quilogramas abaixo: \n'))
litros = float(massa * 0.03)
mililitros = int((litros - int(litros)) * 1000)

 
print(f'A sua quantidade ideal é de {int(litros)} litros e {mililitros} mililitros por dia\n')


#3. Construa o programa que tendo como dados de entrada dois pontos quaisquer do plano cartesiano, P(x1, y1) e Q(x2, y2), calcule a distância entre eles. 
print('-'*8,'Exercicio número 3','-'*8)
print('Plano cartesiano, descubra a distancia entre os pontos P e Q.')
x1 = int(input('Para P Digite o X1: '))
y1 = int(input('Para P Digite o Y1: '))
x2 = int(input('Para Q Digite o X2: '))
y2 = int(input('Para Q Digite o Y2: '))
distancia = sqrt(((x2 - x1)**2 + (y2 - y1)**2))

print(f'a distancia entre os pontos P e Q é de {distancia:.0f}')

#4. Desenvolva o programa que classifique dois valores inteiros quaisquer em ordem crescente. Os valores serão fornecidos pelo usuário. 
print('\n','-'*8,'Exercicio número 4','-'*8,'\nDigite dois valores inteiros, para classificar-los')

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

if n1 > n2:
    print(f'A ordem crescente entre os valores digitados são {n2}, {n1}!')

elif n1 < n2:
    print(f'A ordem crescente entre os valores digitados são {n1}, {n2}!')

else:
    print(f'ambos os números {n1} e {n2} possuem o mesmo valor')

#5. Construa o programa que calcule o peso ideal de uma pessoa. Utilize as seguintes fórmulas:
#- Se homem, o peso ideal é calculado assim: (72,7 x altura) - 58;
#- Se mulher, o peso ideal é calculado assim: (62,1 x altura) - 44,7.
# Analise o problema e verifique quais são os dados que o usuário precisa fornecer (digitar).

print(f'\n','-'*8,'Exercicio número 5','-'*8,'\nCalculadora de peso Ideal.')
altura = float(input('Digite sua altura em metros, Exemplo: 1.60\nDigite:'))

print(f'Qual seu gênero?','\n( 1 ) Femino\n( 2 ) Masculino')
genero = int(input('Digite:'))

if genero == 1:
    print(f'O peso ideal para você é {(62.1 * altura) - 44.7:.2f}kg')
else:
    print(f'O peso ideal para você é {(72.7 * altura) - 58:.2f}kg')
print('Trabalho feito pelo aluno Gustavo Santana (APP --> VISUAL STUDIO CODE) - ADS Noturno')