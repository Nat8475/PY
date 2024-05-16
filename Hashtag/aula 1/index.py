"""
Passo a Passo

1. Abrir o Sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login
2. Fazer login
3.abrir/importar base de dados
4.cadastrar produto
5.repetir processo
"""

import pyautogui
import time
pyautogui.PAUSE = 0.5

#pyautogui.alert("O código vai começar, não mexa em nada!")

# Abrir o Navegador

pyautogui.press("win")

pyautogui.write("brave")

pyautogui.press("enter")

#Entrar no Sistema

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.press("enter")

time.sleep(2)

#Fazer Login

pyautogui.click(x=-939, y=641)

pyautogui.write("datandarosa@gmail.com")

pyautogui.press("tab")

pyautogui.write("admin")

pyautogui.press("tab")

pyautogui.press("enter")

#pyautogui.click(x=-946, y=806)

time.sleep(1)

#Importar Base de Dados

import pandas as pd

tabela_produtos  = pd.read_csv("produtos.csv")

#Cadastrar Produtos
"""
codigo = "MOLO000251"

pyautogui.click(x=-1064, y=528)

pyautogui.write(codigo)

        pyautogui.press("tab")"""

for linha in tabela_produtos.index:
    """codigo = tabela_produtos.loc[linha, "codigo"]
    marca = tabela_produtos.loc[linha, "marca"]
    tipo = tabela_produtos.loc[linha, "tipo"]
    categoria = tabela_produtos.loc[linha, "categoria"]
    preco = tabela_produtos.loc[linha, "preco_unitario"]
    custo = tabela_produtos.loc[linha, "custo"]
    obs = tabela_produtos.loc[linha, "obs"]"""

    pyautogui.click(x=-1064, y=528)

    pyautogui.write(str(tabela_produtos.loc[linha, "codigo"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela_produtos.loc[linha, "marca"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela_produtos.loc[linha, "tipo"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela_produtos.loc[linha, "categoria"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela_produtos.loc[linha, "preco_unitario"]))

    pyautogui.press("tab")

    pyautogui.write(str(tabela_produtos.loc[linha, "custo"]))

    pyautogui.press("tab")
    obs = tabela_produtos.loc[linha, "obs"]

    if not pd.isna(obs):
        pyautogui.write(str(tabela_produtos.loc[linha, "obs"]))

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)





