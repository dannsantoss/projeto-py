for i in range(1):
    print("Se increva no canal")


# for item in lista:
    # o que eu quero que seja repetir

lista_preco = [1500, 1000, 800, 2000]

for preco in lista_preco:
    imposto = preco * 0.1
    print(f"Preço {preco}, Imposto: {imposto}")

# regra do imposto
# preco ate 1000 -> imposto é de 10%
# preco maoir do uqe 1000 -> imppsto é de 15%

for preco in lista_preco:
    if preco > 1000:
        imposto = preco * 0.15
    else:
        imposto = preco * 0.1
    print(f"Preço {preco}, Imposto: {imposto}")

# Total de imposto

total_imposto = 0  # acumulado

for preco in lista_preco:  # 1500
    if preco > 1000:
        imposto = preco * 0.15  # 250
    else:
        imposto = preco * 0.1
    print(f"Preço {preco}, Imposto: {imposto}")
    total_imposto = total_imposto + imposto  # 0 + 225


print(total_imposto)


# exercio dasafio

venda_22 = {"jan": 15000, "fev": 15500, "mar": 14000,
            "abr": 16000, "mai": 16300, "jun": 17000}

venda_23 = {"jan": 17000, "fev": 15000, "mar": 17500,
            "abr": 16900, "mai": 16000, "jun": 18500}

# saber quanto variou poecentuamente cada mes de 2023em coparacao com 2022

for mes in venda_23:
    valor_22 = venda_22[mes]
    valor_23 = venda_23[mes]
    var_percentual = valor_23 / valor_22 -1
    print(f"Variação {mes} : {var_percentual:.1%}")

# simulem: se a empresa tivesse pelo meonos empatado com 2022 nos memse que ela vendeu menos, qual teria sido o faturamento
faturamento_total_simulado = 0
for mes in venda_23:
    valor_22 = venda_22[mes]
    valor_23 = venda_23[mes]
    var_percentual = valor_23 / valor_22 -1
    if var_percentual < 0:
        faturamento_total_simulado = faturamento_total_simulado + valor_22
    else:
        faturamento_total_simulado = faturamento_total_simulado + valor_23
    print(f"Variação do {mes}: {var_percentual:.1%}")
print(faturamento_total_simulado)