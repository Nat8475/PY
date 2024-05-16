#BOAS VINDAS

print("Seja Bem-Vindo a Distribuidora do Natã\n")

# INSERINDO VALOR DO PRODUTO E QUANTIDADE

valor = float(input("Insira o valor unitário do Produto:"))
quantidade = int(input("Insira a quantidade de Produtos que deseja:"))

# CALCULANDO O VALOR SEM DESCONTO

valor_sem_desconto = valor * quantidade

# DEFININDO OS DESCONTOS SE BASEANDO NO VALOR TOTAL DA COMPRA

if valor_sem_desconto < 2500:
    desconto = 0
elif 2500 <= valor_sem_desconto < 6000:
    desconto = 0.04
elif 6000 <= valor_sem_desconto < 10000:
    desconto = 0.07
else: 
    desconto = 0.11

# CALCULANDO O VALOR COM DESCONTO

valor_com_desconto = valor_sem_desconto - (valor_sem_desconto * desconto)

# IMPRIMINDO OS VALORES FINAL COM DESCONTO E SEM DESCONTO

print(f"Valor SEM Desconto: {valor_sem_desconto: .2f}")
print(f"Valor COM Desconto: {valor_com_desconto: .2f}")