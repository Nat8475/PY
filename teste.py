from tqdm import tqdm
import os
import time

def clear():
    time.sleep(1)
    clear = lambda: os.system('clear')
    clear()

def carregamento_bar():
    for _ in tqdm(range(10), desc="Carregando o Sistema!", unit="iter"):
        time.sleep(1)
    print("Carregamento do SIstema foi concluído!")

#Boas Vindas


#name = str(input("Qual seu nome?"))

#carregamento_bar()

#clear()
def menu_principal():
    #print(f"Olá {name}, Seja Muito Bem-Vindo!\n")

    print("-"*50 + "\n|" + " "*16 + "Menu Principal" + " " *18 + "|\n" + "-"*50)
    print("|" + "1- Sorveteria" + " "*35 + "|" + "\n|2 - Livraria" + " "*36 + "|"  + "\n|3 - Banco"  + " "*39 + "|" +  "\n|4 - Alunos" + " "*38 + "|\n"  + "-"*50)

menu_principal()



