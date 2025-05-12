#atv 1
def mens_num(mensagem, numero):
    print(f'sua mensagem: {mensagem}, e o numero: {numero}')

#atv 2
def calc_idade(ano_nascimento):
    return 2025 - ano_nascimento

#atv 3
def somar(x, y, z):
    valor_somado = x+y+z
    return valor_somado


#atv 4
def nota(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media



def main():
    print('Questão 1')
    mens = str(input('Digite uma mensagem: '))
    num = int(input('Digite um numero: '))
    mens_num(mens, num)

    print('\nQuestão 2')
    ano_nascimento = int(input('Digite seu ano de nascimento: '))
    idade = calc_idade(ano_nascimento)
    print(f'Voce tem {idade} anos de idade')

    print('\nQuestão 3')
    x = int(input('Digite um numero: '))
    y = int(input('Digite um numero: '))
    z = int(input('Digite um numero: '))
    soma = somar(x, y, z)
    print(f'A sua soma deu {soma}')

    print('\nQuestão 4')
    """Crie um programa que leia o nome de um aluno e três notas. Em seguida, uma função deve calcular a média das três notas e retornar esse valor.
     A função principal deve exibir o nome do aluno e a média calculada."""
    nome = str(input('Digite seu nome: '))
    nota1 = float(input('Digite sua nota 1: '))
    nota2 = float(input('Digite sua nota 2: '))
    nota3 = float(input('Digite sua nota 3: '))
    media = nota(nota1, nota2, nota3)
    print(f'O aluno {nome}, possui uma media de {media:.2f} nas três provas.')

if __name__ == '__main__':
    main()
