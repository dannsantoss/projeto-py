vendas = [100, 50 , 130 , 80, 120]

print(vendas[-1]) #-1 - o ultimo valor da listas,  -2 - penultimo valor da lista , assim em diante

total_vendas = sum(vendas)
print(total_vendas)
quantidade  = len(vendas)
print(quantidade)
valor_max = max(vendas)
print(valor_max)
valor_min = min(vendas)
print(valor_min)

posicao = vendas.index(130)
print(posicao)

print(vendas[:2])

produtos = ["iphone", "ipad", "airpod"]

print("iphone" in produtos)

#produtos_usuarios = input("Digite o nome de um produto:")


produtos = ["iphone", "ipad", "airpod"]
precos = [4000, 8000, 2000]

#edita um item
print("iphone" in produtos)
precos[0] = precos[0] * 1.1
print(precos)

#adiciona um item
produtos.append("macbook")
precos.append(100000)
print(produtos)
print(precos)

#remove o item
produtos.remove("macbook") #remove pelo valor
precos.pop(-1) #remove pelo indice
print(produtos)
print(precos)

#inserir um item
produtos.insert(1, "airpod") 
print(produtos)

#contar valores
print(produtos.count("airpod"))

#ordenar
precos.sort(reverse=True)
print(precos)
