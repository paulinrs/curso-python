"""
Tipos de dados
str - string - textos 'Assim' "assim"
int - inteiro - 123456 0 -10 -20-1500
float - real/ponto flutuante - 10.50 1.5 - 10.10
bool - booleano/lógico - True/False 10 == 10
"""
print('Paulo', type('Paulo'))
print(10, type(10))
print(25.23, type(25.23))
print(11 == 10, type('10 == 10'))

"""
Paulo <class 'str'>
10 <class 'int'>
25.23 <class 'float'>
True <class 'str'>
"""

print('Paulo', type('Paulo'), bool('Paulo'))
print('10', type('10'), type(int('10')))
print(10 + 10)

#string:nome
print('Paulo Roberto', type('Paulo Roberto'))
#Idade: int
print(37, type(37))
#Altura: float
print(1.71, type(1.71))
#e maior de idade 10 > 20
print(37 > 18, type(22 > 19))
