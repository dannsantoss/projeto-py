import os

lista_arquivos = os.listdir("arquivos")
print(lista_arquivos)

for nome_arquivos in lista_arquivos:
    if "txt" in nome_arquivos:
        if"22" in nome_arquivos:
            os.rename(f"arquivos/{nome_arquivos}", f"arquivos/22/{nome_arquivos}")
        elif "23" in nome_arquivos:
            os.rename(f"arquivos/{nome_arquivos}", f"arquivos/22/{nome_arquivos}")


import requests

link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

resposta = requests.get(link)
dic_resposta = resposta.json()
cotacao_dolar = dic_resposta["USDBRL"]
print(cotacao_dolar["bid"])