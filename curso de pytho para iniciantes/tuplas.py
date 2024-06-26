def calcular_imposto2(preco, ir=0.225, csll=0.035, iss=0.05):
    imposto_ir = preco * ir
    imposto_csll = preco * csll
    imposto_iss = preco * iss
    return imposto_ir, imposto_csll, imposto_iss


def calcular_imposto2(preco, ir=0.225, csll=0.035, iss=0.05):
    imposto_ir = preco * ir
    imposto_csll = preco * csll
    imposto_iss = preco * iss
    return imposto_ir, imposto_csll, imposto_iss


ir, csll, iss = calcular_imposto2(1000)
print(ir, csll, iss, sep="\n")

tamanho_tela = (1920, 1080)


#

vendas = {
    "André": [1000, 500, 300, 5000, 1500, 80, 3000],
    "Andresa": [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500],
    "Alan": [800, 100],
    "Ana": [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 50, 65, 60, 70, 70, 70, 20, 180]
}

# cada venda o vendedo ganha 2 reias e 1% do valor de vendas
# calcular o valor total de bonus  pago e o bonus de cadas vendedor

def calcular_bonus(lista_vendas):
    qtde = len(lista_vendas)
    bonus1 = qtde * 2
    valor_total = sum(lista_vendas)
    bonus2 = 0.01 * valor_total
    bonus = bonus1 + bonus2
    return bonus

for vendedor in vendas:
    lista_venda_vendedor = vendas[vendedor]
    bonus = calcular_bonus(lista_venda_vendedor)
    print(f"Vendedor: {vendedor}, Bonus: {bonus}")
    bonus_total = bonus_total + bonus
print(bonus_total)

