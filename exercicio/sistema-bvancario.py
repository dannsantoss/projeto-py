# sitema bancario com operacoes: sacar, depositar e vizualizar extrato.

menu = ''' 
  [d] Depositar
  [s] Sacar
  [e] extrato
  [q] sair

'''

saldo = 0
limite = 500
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print ("Depositar")

    elif opcao == "s":
        print ("Sacar")

    elif opcao == "e":
        print ("Extrato")

    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favoor selecione novamente a operaçao desejada")

# deposito - dever ser posivel depositar valores positivos, devem ser amarzenas e uma variavel e exibidos na operaçao de extrato

# saque- 3 saque diario de maximo 500
# caso nao tenha dinheiro na conta deve exibir nao sera possivel sacar o dinheiro por falta de saldo
# todos os saldos devem se armazenaos em uma variavel e exibidos na operaçao de extrato

# extrato - deve lista todos depositos e sauqe realizados na conta
# no fim deve ser exibido o salto atual da Conta
# os valore devem ser exibidos em formato r$ exemplo 1500.45 = R$ 1500.45


