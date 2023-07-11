print('hi, variaveis')

a = 1
b = 3.3

print(a + b)

texto = "Sua idade é..."
idade = 24

# Erro pois não é possível concatenar strings e inteiros
# print(texto + idade) 

# Se precisar interpretar valores dentro de uma string use o "f string"
print(f'{texto} {idade}') # Isso funciona como um template string do JS

PI = 3.14
raio = float(input('Raio da circunferência: '))

print(type(raio))

area = PI * raio * raio 

print(f'O valor da area é {area}')