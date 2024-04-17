nome = input("Digite aqui seu nome:")
email = input("Digite seu email:")

posicao = email.find("@")
servidor = email[posicao:]
print(servidor)

posicao = nome.find(" ")
primeiro_name = nome[:posicao]
print(primeiro_name)

#construa uma mensagem; usuario Danilo cadastrado com sucesso cadastrado com email tal
print(f" Usuario {primeiro_name} foi cadatrado com Sucesso, com email: {email}")

# contrua uma mensagem : enviamos um link de confirmaçao para o email j***@gmail.com
primeira_letra = email[0]
mensagem2 = f"enviamos um link de confimaçao para o email {primeira_letra}***{servidor}"
print(mensagem2)