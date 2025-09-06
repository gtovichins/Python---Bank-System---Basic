from datetime import datetime


saldo = 0.0
extrato = []
limite = 500.0           
SAQUES_MAX = 3            
numero_saques = 0         


def formatar_valor(valor):
    return f"R${valor:.2f}"

def registrar_movimento(tipo, valor):
    hora = datetime.now().strftime("%d/%m/%Y %H:%M")
    extrato.append(f"{hora} | {tipo:<8} | {formatar_valor(valor)}")


def depositar():
    global saldo
    valor = float(input("Digite o valor do depósito: R$ "))
    if valor > 0:
        saldo += valor
        registrar_movimento("Depósito", valor)
        print(f"Depósito de {formatar_valor(valor)} realizado com sucesso!\n")
    else:
        print("Valor inválido! O depósito deve ser maior que 0.\n")

def sacar():
    global saldo, numero_saques
    if numero_saques >= SAQUES_MAX:
        print("Limite diário de saques atingido!\n")
        return
    
    if saldo <= 0:
        print("Saldo insuficiente! Não é possível realizar o saque.\n")
        return

    valor = float(input("Digite o valor do saque: R$ "))
    
    if valor <= 0:
        print("Valor inválido!\n")
    elif valor > saldo:
        print(f"Saldo insuficiente! Você possui apenas {formatar_valor(saldo)}.\n")
    elif valor > limite:
        print(f"Saque excede o limite de {formatar_valor(limite)} por operação!\n")
    else:
        saldo -= valor
        numero_saques += 1
        registrar_movimento("Saque", valor)
        print(f"Saque de {formatar_valor(valor)} realizado com sucesso!\n")

def consultar_extrato():
    print("\n" + "="*50)
    print("               EXTRATO BANCÁRIO")
    print("="*50)
    
    if not extrato:
        print("Nenhuma movimentação registrada.")
    else:
        print(f"{'Data/Hora':<16} | {'Operação':<8} | {'Valor':>10}")
        print("-"*50)
        for movimento in extrato:
            data_hora, resto = movimento.split(" | ", 1)
            tipo, valor = resto.split(" | ")
            print(f"{data_hora:<16} | {tipo:<8} | {valor:>10}")
    
    print("-"*50)
    print(f"Saldo atual: {formatar_valor(saldo)}")
    print(f"Saques realizados hoje: {numero_saques}/{SAQUES_MAX}")
    print("="*50 + "\n")


def menu():
    while True:
        print("---- Sistema Bancário ----")
        print("[d] Depositar")
        print("[s] Sacar")
        print("[e] Extrato")
        print("[q] Sair")
        opcao = input("Escolha uma opção: ").lower()
        
        if opcao == "d":
            depositar()
        elif opcao == "s":
            sacar()
        elif opcao == "e":
            consultar_extrato()
        elif opcao == "q":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Escolha novamente.\n")

menu()
