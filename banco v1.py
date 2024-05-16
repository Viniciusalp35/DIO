import time
menu = f"""
------------- Bem vindo ao Banco X -------------

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair do menu

------------------------------------------------
"""

extrato = ""
saldoEmConta = 0
numeroSaques = 0
LIMITE_MAXIMO = 500


while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Qual o valor voce deseja depositar?\n"))
        if deposito < 0:
            print("Valor inválido")
            time.sleep(1)
        else:
            saldoEmConta += deposito
            extrato += f"""
        Depósito <------- R$ {deposito:.2f}            

"""
            print("Depósito realizado com sucesso!")
        time.sleep(1)

    elif opcao == "s":
        if numeroSaques < 3:
            saque = float(input("Qual o valor voce deseja sacar?\n"))
            if saque <= 0:
                print("Valor inválido")
                time.sleep(1)
            elif saque > 500:
                print("Valor excede limite máximo de saque")
                time.sleep(1)
            elif saque > saldoEmConta:
                print("Saldo insuficiente")
                time.sleep(1)
            else:
                saldoEmConta -= saque
                numeroSaques += 1
                print("Saque realizado com sucesso!")
                extrato += f"""
            Saque ------> R$ {saque:.2f}

    """
                time.sleep(1)
        else:
            print("Numero máximo de saques diários atingido")
            time.sleep(1)

    
    
    elif opcao == "e":
        fimExtrato = extrato + f"""
        Saldo em conta -------> R$ {saldoEmConta:.2f}

"""
        
        print(fimExtrato)
        input("Aperte Enter para retornar ao menu!")

    elif opcao == "q":
        break

