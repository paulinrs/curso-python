"""
Operadores Lógicos
and, or, no
in e not in
"""
nome = 'Paulo Roberto'

if 'l' in nome:
    print("Existe esssa letra no seu nome.")
else:
    print("Não existe essa letra no seu nome.")

if 'x' not in nome:
    print("Não existe essa letra no seu nome.")
else:
    print("Existe esssa letra no seu nome.")
print('_________________________________________________________')
usuario = input('Nome de usuario: ')
senha = input('Senha do usuário')

usuario_bd = 'arthur'
senha_bd = '0509'

if usuario_bd == usuario and senha_bd ==senha:
    print('Você está logado no sistema')
else:
    print('Usuário ou senha inválidos. ')

