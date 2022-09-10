nome = 'Paulo Roberto'
idade = 37  #int
altura = 1.71   #float
e_maior = idade > 18    #bool
peso = 70
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de e seu imc é', imc)
print(f'{nome} tem {idade} anos de e seu imc é {imc:.2f}')
print('{} tem {} anos de , {} de altura, peso {} e seu imc é {:.2f}'.format(nome, idade, altura, peso, imc))
"""
podemos mudar as ordens das variaveis e repertir
"""
print('{0} tem {1} anos e seu imc é {2:.2f}'.format(nome, idade, imc))
print('eu tenho {i} anos me chamo {n} e meu imc é {im:.2f}, com {i} anos estou preparado pra ver o Mengão Campeão da LIbertadores 2022.'.format(n=nome, i=idade, im=imc))

