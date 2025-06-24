import math
import pandas as pd

# n1 = int(input('Entre com o primeiro numero:'))
# n2 = int(input('Entre com o segundo número:'))
# soma = n1 + n2

# print(n1)
# print(n2)

# print('A soma de', n1, 'com', n2, 'é:', soma)

# x = 5**3 #potencia
# print(x)

# y = float(input('Entre com o num:'))

# print(math.trunc(y)) #pega so o inteiro do num
# print(math.ceil(y)) #arredonda pra cima
# print(math.floor(y)) # arredonda pra baixo

r = 'hello-world'

print(r[6])
print(r[4])
print(r[:5])
print(r[6:11])
print(r[0:10:3])
print(len(r))
print(r.count('l'))
print(r.upper())

idade = int(input('idade:'))

if idade > 60:
    print('Você é idoso')
else:
    print('Você não é idoso')

