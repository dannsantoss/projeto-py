faturamento = 1000
custo = 800

#lucro = faturamento - custo

#if lucro >= 0:
    #print("Lucro", lucro)
#else:
    #print("Prejuizo!!!!!")
    #print(lucro)

#produtos = ["iphone", "ipad", "airpod"]
#novo_produto = input("Digite aqui o produto:")
#novo_produto = novo_produto.lower

#if novo_produto in produtos:
    #print("produto já cadastrado")
#else:
   # print("produto cadastrado com sucesso")
   # produtos.append(novo_p#roduto)

#print(produtos)


#acima de 15000 > 500 de bonus
#acima de 1000 > 150 de bonus
#acima de 5000 > 50 de bonus

#vendas = int(input("Digite sua vendas"))

#if vendas > 15000:
#    bonus = 500
#elif vendas > 10000:
   # bonus = 150#
#elif vendas > 5000:
   # bonus = 50 
#else:
  #  bonus = 0

#print("Bonus", bonus)


#if vendas > 5000:
    #if vendas > 10000:
      #  if vendas > 15000:
      #      bonus = 500
       # else:
       #     bonus = 150
      #  bonus = 150
    #else:
      #  bonus = 50
#else:
    #bonus = 0

#print("Bonus", bonus)

#acima de 15000 > 500 de bonus
#acima de 1000 > 150 de bonus
#acima de 5000 > 50 de bonus
#vendas de empresa > 50000

#vendas = int(input("Digite sua vendas"))
#vendas_empresa = 60000
#meta_empresa = 50000

#if vendas > 15000 and vendas_empresa > meta_empresa:
   # bonus = 500
#elif vendas > 10000 and vendas_empresa > meta_empresa:
   # bonus = 150
#elif vendas > 5000 and vendas_empresa > meta_empresa:
   # bonus = 50 
#else:
   # bonus = 0

#print("Bonus", bonus)

#exercio desafios

#sistema de consulta de preco

precos = [1500, 1000, 800, 2000]
produtos = ["celular", "camera", "fone de ouvido", "monitor"]

verificar_produto = input("Digite o produto:")
verificar_produto = verificar_produto.lower()

if verificar_produto in produtos:
    posicao = produtos.index(verificar_produto)
    preco = precos[posicao]
    print(f"Produto encotrado {preco}")

else:
    print("produto não cadastrado, tente novamente")
