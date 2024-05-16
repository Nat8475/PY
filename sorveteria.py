from tqdm import tqdm
import time
import os

sabores = [ "AC", "CH", "MR"]
tamanhos = [ "P", "M", "G"]

total_pedido = 0
total_unidades = 0

name = input("Qual é seu nome?")

def carregamento(tarefa,tarefa2, total):
    #print(f'{tarefa}...')
    for _ in tqdm(range(total), desc=tarefa2, unit="iter"):
        time.sleep(1)  # Simula o tempo de execução da tarefa
    print(f'{tarefa} concluído com sucesso!')

carregamento("Carregamento de Sistema","Carregando Sistema:", 10)

def limpar():
    time.sleep(1)
    clear = lambda: os.system('clear')
    clear()
limpar()


print(f"Seja muito Bem-vindo {name},\nPor Gentileza Utilize a Nomeação que está entre parênteses,\nLogo abaixo segue nosso Cardápio.")

def cardapio():
    print("|"+"-"*50 + "|" + "\n|"+ " "*20 + "Cardápio" + " "*22 + "|" + "\n|"+"-"*50 + "|")
    print("| Tamanhos:" + " "*20 + "Sabores:" + " "*12 + "|")
    print("|" + " "*14 + "Açaí(AC)" + " " + "Chococlate(CH)" + " " + "Morango(MR)" + " |")
    print("|Pequeno(P):" + " "*3 + "R$11.0 ", " R$10.0" + " "*9 +"R$10.0" + " "*6 + "|" + "\n|Médio(M):" + " "*5 + "R$13.0 ", " R$11.0" + " "*9 + "R$11.0" + " "*6 + "|" + "\n|Grande(G):" + " "*4 + "R$15.0 ", " R$13.0" + " "*9 + "R$13.0" + " "*6 + "|")
    print("|"+"-"*50 + "|")
cardapio()


while True:

    sabor = str(input("Qual o Sabor?"))
    saboru = sabor.upper()

    if saboru not in sabores:
        print("Sabor insirido não é válido, Utilize a Nomeação que está dentro do parênteses.")
        continue

    tamanho = input("Qual o tamanho?")

    tamanho_upper = tamanho.upper()
    if tamanho_upper not in tamanhos:
        print("Tamanho insirido não é válido, Utilize a Nomeação que está dentro do parênteses.")

    AC = {
    "P": 11,
    "M": 13,
    "G": 15
    }
    CH = {
    "P": 10,
    "M": 11,
    "G": 13
    }

    MR = {
    "P": 10,
    "M": 11,
    "G": 13
    }
    ac_p = AC["P"]
    ac_m = AC["M"]
    ac_g = AC["G"]

    ch_p = CH["P"]
    ch_m = CH["M"]
    ch_g = CH["G"]
    
    mr_p = MR["P"]
    mr_m = MR["M"]
    mr_g = MR["G"]

    if saboru == "AC":

        match tamanho_upper:
            case "P":
                total_pedido += ac_p
                total_unidades += 1

            case "M":
                total_pedido += ac_m
                total_unidades += 1

            case "G":
                total_pedido += ac_g
                total_unidades += 1

    if saboru == "CH":

        match tamanho_upper:
            case "P":
                total_pedido += ch_p
                total_unidades += 1

            case "M":
                total_pedido += ch_m
                total_unidades += 1

            case "G":
                total_pedido += ch_g
                total_unidades += 1

    if saboru == "MR":

        match tamanho_upper:
            case "P":
                total_pedido += mr_p
                total_unidades += 1

            case "M":
                total_pedido += mr_m
                total_unidades += 1

            case "G":
                total_pedido += mr_g
                total_unidades += 1


    print(f"{name}, seu pedido foi um {saboru}, {tamanho}, Valor total: {total_pedido}")

    other_pedido = str(input("Deseja Pedir mais alguma coisa?"))
    if other_pedido.lower() == "sim":
        
        limpar()
        print(cardapio())
    else:
        print(f"Você pediu {total_unidades}, Que deu um Valor Total de: {total_pedido: .2f}")
        break
