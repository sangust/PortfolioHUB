#ATIVIDADE 2 - GUSTAVO SANTANA, ADS NOTURNO.
#1- Desenvolva o programa que classifique dois valores inteiros quaisquer em ordem crescente. Os valores serão fornecidos pelo usuário. 

print('Questão 1, Descubra a ordem crescente de dois numeros!')
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))

if num1 < num2:
    print(f'A ordem crescente é {num1} e {num2}')
elif num1 > num2:
    print(f'A ordem crescente é {num2} e {num1}')
else:
    print('Os números são iguais!')

#Elabore o programa que selecione o maior valor de três valores fornecidos pelo usuário. Resolva sem usar operador lógico (e, ou, não).
print('\nQuestão 2, Descubra o maior numero digitado!')
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
num3 = int(input('Digite um numero: '))

if num1 > num2:
    if num1 > num3:
        maior = num1
    
elif num2 > num3:
    if num2 > num1:
        maior = num2
    
elif num3 > num1:
    if num3 > num2:
        maior = num3
if num1 == num2 == num3:
    print('Todos os número tem o mesmo valor')
else:
    print(f'O maior número é o {maior}')
    

#3- Refaça o exercício anterior utilizando também operador lógico (e, ou, não).
print('\nQuestão 3, Descubra o maior numero digitado, com operadores logicos!')
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
num3 = int(input('Digite um numero: '))

if num1 > num2 and num1 > num3:
    print(f'O número {num1} é o maior número dentre os digitos {num2} e {num3}')
elif num2 > num1 and num2 > num3:
    print(f'O número {num2} é o maior número dentre os digitos {num1} e {num3}')
elif num3 > num1 and num3 > num2:
    print(f'O número {num3} é o maior número dentre os digitos {num2} e {num1}')
else:
    print('Todos os número tem o mesmo valor')

#4- Elabore o programa que simule a calculadora com as quatro operações aritméticas básicas.
#O usuário fornecerá dois números e a operação aritmética desejada.
#Mostre o menu com estes símbolos (+ , - , * , / ) para o usuário escolher a operação aritmética. Utilize o comando “se . . . senão . . . ” encadeado, ou seja, “if . . . else . . . ” encadeado. 
print('\nQuestão 4, Mini calculadora')
operacao = int(input('Escolha a operação aritmetica\n[1] Soma -> +\n[2] Subtração -> -\n[3] Multiplicação -> *\n[4] Divisão -> /\nDigite sua escolha: '))
num1 = float(input('Digite um numero: '))
num2 = float(input('Digite um numero: '))

if operacao == 1:
    soma = num1 + num2
    print(f'A soma entre os numeros {num1} e {num2} é {soma}!')
elif operacao == 2:
    subtracao = num1 - num2
    print(f'A subtração entre os numeros {num1} e {num2} é {subtracao}!') 
elif operacao == 3:
    multiplicar = num1 * num2
    print(f'A multiplicação entre os numeros {num1} e {num2} é {multiplicar}!') 
elif operacao == 4:
    divisao = num1 / num2
    print(f'A divisão entre os numeros {num1} e {num2} é {divisao}')
else:
    print('Vc informou um operador errado.')

#5- Dado o comprimento das três retas a, b e c. Verifique se eles podem ser o comprimento dos lados de um triângulo. 
print('\nQuestão 5, Verificador de triangulos.')
a = int(input('Informe o Comprimento da reta A: '))
b = int(input('Informe o Comprimento da reta B: '))
c = int(input('Informe o Comprimento da reta C: '))

if a < b + c and b < c + a and c < a + b:
    if a != b and a != c and b != c:
        print('Seu triangulo é escaleno')
    elif a == b and b == c and c == a:
        print('seu triângulo é Equilatero')
    elif (a == b and a != c) or (b == c and b != a) or (c == a and c != b):
        print('Seu triangulo é isosceles')

else:
    print('As medidas não formam um triângulo.')