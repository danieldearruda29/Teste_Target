
#Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado
# um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

x1 = 0
x2 = 1


numero = int(input("Informe um número para o cálculo da sequência de Fibonacci: "))

if numero == 0:
    print(f'{x1}')
elif numero == 1:
    print(f'{x1}, {x2}')
else:
    print(f'{x1}, {x2}', end=", ")

    while x2 < numero:
        x3 = x1 + x2
        print(f'{x3}', end=", " if x3 < numero else "\n")
        x1 = x2
        x2 = x3

    if x2 == numero:
        print(f'O número {numero} pertence à sequência')
    else:
        print(f'O número {numero} não pertence à sequência')