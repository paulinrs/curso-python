"""
Operadores Relacionais
==igualdade
>maior que
>=maior que ou igual
< menor que
<= menor que ou igual
!=diferente
"""

print ('crf' !='fla')

num_1 = 3
num_2 = 2

expressao = (num_1 < num_2)
print(expressao)


nome  =  input ('Qual o seu nome? ')
idade = input ('Qual a sua idade?')

idade = int(idade)

# Limite para pegar o empréstimo

idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo. ')
else:
    print(f'{nome} NÃO pode pegar o empréstimo')

time = input ("Qual seu time?")
nome  =  input ("Qual o seu nome?")
print()
print(f'{nome} torce para o {time}. ')