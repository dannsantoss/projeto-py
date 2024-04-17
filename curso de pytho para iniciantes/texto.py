faturamento = 1000
custo = 700
lucro = faturamento - custo

#print(f"Faturamento: {faturamento}, Custo: {custo}, Lucro: {lucro}")
#print("faturamento: " + str(faturamento) + ",Custo:" str(custo) ",lucro:" srt(lucro))


email = "DAnilo@gmail.com"

print(email.lower()) 
print(email.find("@")) #-1, se n encontrar o elemto. Se encontrar: a posição

posicao = email.find("@")
servidor = email[posicao+1:]
print(servidor)
nome_email = email[:posicao]
print(nome_email)

#TAMANHO E UM TEXTO
tamanho = len(email)
print(tamanho)

#trocar um pedaço do tetxo
email_trocado = email.replace("gmail.com", "hotmail.com")
print(email_trocado)

nome = "joao lira"
print(nome.capitalize()) #Joao lira
print(nome.title()) #Joao Lira

#especiais - formatacao numerica
margem = lucro / faturamento
print(f"Faturamento: R${faturamento:,.2f},\nCusto: {custo}, \n Lucro: {lucro}")
print(f"Margem: {margem:.1%}")

#exercicios
nome = "Danilo Santos Silva"
email = "danilofalso@gmail.com"

#descubrar o servidor do email
posicao = email.find("@")
servidor = email[posicao:]
print(servidor)

# pegar o primeiro nome do ususario
posicao = nome.find(" ")
primeiro_name = nome[:posicao]
print(primeiro_name)

#construa uma mensagem; usuario Danilo cadastrado com sucesso cadastrado com email tal
print(f" Usuario {primeiro_name} foi cadatrado com Sucesso, com email: {email}")

# contrua uma mensagem : enviamos um link de confirmaçao para o email j***@gmail.com
primeira_letra = email[0]

mensagem2 = f"enviamos um link de confimaçao para o email {primeira_letra}***{servidor}"
print(mensagem2)