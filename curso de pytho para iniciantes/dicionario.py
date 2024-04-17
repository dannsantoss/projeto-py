precos = [1500, 1000, 800, 2000]
produtos = ["celular", "camera", "fone de ouvido", "monitor"]

dic_preco = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}

#pegar um item

preco_celular = dic_preco["celular"]
print(preco_celular)

dic_preco["celular"] = 2000
print(dic_preco) 

dic_preco["iphone"] = 4500
print(dic_preco)

dic_preco.pop("iphone")
print(dic_preco)

#temanho do dicionario

print(len(dic_preco))

print(dic_preco.keys())
print(dic_preco.values())

#exercicio
#sistema de consulta de preco
dic_preco = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}

verificar_produto = input("Digite o produto:")
verificar_produto = verificar_produto.lower()

preco_celular = dic_preco["celular"]
print(preco_celular)
print(dic_preco.values())

if verificar_produto in dic_preco:

    
    preco = dic_preco[verificar_produto]
    
    print(f"Produto {verificar_produto}, Preço: {preco}")
else:
    print("produto não cadastrado, tente novamente")