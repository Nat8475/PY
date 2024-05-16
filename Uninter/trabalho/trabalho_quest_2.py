#BOAS-VINDAS
print("Seja Bem-Vindo a loja de Sorvetes do Natã")

#CARDÁPIO
print("(Utilize a nomeação que está entre parênteses)\n-------------------------\n\tCardápio\n-------------------------")
print("Tamanho:\tSabores: Cupuaçu(CP)\tAçaí(AC)")
print("Pequeno(P)\t\t 9R$\t\t11R$\nMédio(M)\t\t 14R$\t\t16R$\nGrande(G)\t\t 18R$\t\t20R$\n-------------------------")

#Acumulador do valor do pedido
total_pedido = 0

# SELEÇÃO DE SABOR E TAMANHO

while True:
    sabor = input("Insira o Sabor desejado:").upper()

    # VERIFICAÇÃO SE O SABOR É VÁLIDO OU NÃO
    if sabor not in['CP', 'AC']:
        print("O Sabor inserido não se encontra em nosso Cardápio.\n")
        continue

    tamanho = input("Insira o tamanho desejado:").upper()

    # VERIFICAÇÃO SE O TAMANHO É VÁLIDO OU NÃO
    if tamanho not in ['P', 'M', 'G']:
        print("O tamanho inserido é Inválido.\n")
        continue


# CALCULAR VALOR DO PEDIDO COM BASE NO VALOR POR SABOR

    if(sabor == 'CP'):
        if(tamanho == 'P'):
            preço = 9
        elif(tamanho == 'M'):
            preço = 14
        else:
            preço = 18
    else:
        if(tamanho == 'P'):
            preço = 11
        elif(tamanho == 'M'):
            preço = 16
        else:
            preço = 20

    # PEDIDO FINAL
    print(f"Você pediu um {sabor}, tamanho {tamanho:} {preço}\n")

    # ADICIONAR VALOR DO PEDIDO
    total_pedido += preço

    #PEGUNTA SE DESEJA CONTINUAR PEDINDO OU NÃO
    continuar = input("Deseja pedir algo mais? (s/n)")
    if continuar.lower() != 's':
        print(f'O valor total do seu pedido é de R${total_pedido:.2f}')
        break
