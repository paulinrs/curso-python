"""
criar variáveis para o nome (str), idade (int),
altura (float) e peso (float) de uma pessoa
Criar variável com o ano atual (int)
Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
Exibir um texto com todos os valores na tela usando F-Strings(com chaves)
"""
nome = 'Paulinho'
idade = 37
peso = 70
altura = 1.71
ano_atual = 2022
nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'{nome} pesa {peso} e seu imc é {imc:.2f}.')
print(f'{nome} nasceu {nascimento}.')

