nums = [1, 2, 3]
print(nums)

# Tipo list (lista)
print(type(nums))

# Tipo lista aceita elementos repetidos
# Para adicionar um elemento ao final de uma lista use o método append
nums.append(5)
print(nums)

# Para verificar quantos itens existem dentro da lista use a função len
print(len(nums))

# Sobreescrevendo um item da da lista
# O index 1 (segundo elemento da lista) vai receber o valor de 20
nums[1] = 20
print(nums)

# Adicionar um item a lista apartir de um index especifico
# No index 1, estou inserindo o valor 55, os demais itens serão deslocados
nums.insert(1, 55)
print(nums)

# Para obter o valor do ultimo item, basta usar o index -1
# -1 é o primeiro item de trás para frente
print(nums[-1])

# Usando o -2, obtemos o penultimo item e assim por diante
print(nums[-2])

