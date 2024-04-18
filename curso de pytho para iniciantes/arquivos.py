with open("./curso de pytho para iniciantes/vendas.txt", "r") as arquivo:
    #fazer o que quiser com o arquivo
    infos = arquivo.readlines()
venda_totais = 0
for item in infos:
    item = item.replace("\n", "")
    item = item.replace(" ", "")
    resultado =item.split(",")
    valor = resultado[1]
    valor = float(valor)
    venda_totais = venda_totais + valor

print(venda_totais)
