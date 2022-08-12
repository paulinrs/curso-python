"""
iniciar com letra, pode conter numeros, separar _, letras minusculas
"""
nome = 'Paulo Roberto'
idade = 37
altura = 1.71
e_maior = idade > 18
peso = 71
imc = peso / (altura ** 2)

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)