# MENSAGEM DE BOAS-VINDAS
print("Olá, Seja Bem-Vindo a Copiadora do Natã")

#FUNÇÕES

#Função para o tipo de serviço Adicional

def servico_extra():

    while True:
        print("\tServiço Adicionais\n1 - Encadernação Simples\n2 - Encadernação Capa Dura\n0 - Nenhum Adicional")
        servico_extra = int(input(">> Escolha o serviço adicional: "))

        if -1 < servico_extra > 2:
            print("Valor Inválido")
            continue

        if servico_extra == 1:
            valor_servico_extra = 15
        elif servico_extra == 2:
            valor_servico_extra = 40
        else:
            valor_servico_extra = 0
    
        return valor_servico_extra

#Função para a quantidade de Páginas

def num_pag():
    desconto_total = 0

    while True:
        try:
            num_pag = int(input("Insira o Número de Páginas desejadas: "))

            if num_pag <= 0:
                print("Número de Páginas inválido.")
                continue

            if num_pag > 20000:
                print("Não aceitamos um Pedido desse Tamanho!")
                continue
            
            #Verificação de erro
        except ValueError:
            print("O Valor inserido não é válido")
            continue
        #Calcula o desconto de Acordo com o Número de Páginas

        if num_pag < 20:
            desconto_total = 0

        if (num_pag >= 20) and (num_pag < 200):
            desconto_total = 0.15

        if( num_pag >= 200) and ( num_pag < 2000):
            desconto_total = 0.20

        if (num_pag >= 2000) and ( num_pag < 2000):
            desconto_total = 0.25
                
        return (num_pag, desconto_total)


#Função para o tipo de serviço

def escolha_servico():

    servicos = ["DIG", "ICO", "IPB", "FOT"]

    while True:
            print("\tServiços Disponíveis\nDIG - Digitalização\nICO - Impressão Colorida\nIPB - Impressão Preto e Branco\nFOT - Fotocópia")
            servico = str(input(">>>")).upper()

            if servico not in servicos:
                print("O serviço inserido não está disponível")
                continue
  
            if servico == "DIG":
                valor_servico = 1.10
            elif servico == "ICO":
                valor_servico = 1
            elif servico == "IPB":
                valor_servico = 0.40
            elif servico == "FOT":
                valor_servico = 0.20

            return valor_servico
    


# Chama as Funções

valor_servico = escolha_servico()

num_pag, desconto = num_pag()

valor_servico_extra = servico_extra()

# Calcula o Valor total

total = (valor_servico * num_pag) + valor_servico_extra
# Calcula o Desconto
total2 = total - (total * desconto) 

# Imprime o resultado

print(f"Valor sem Desconto: R$ {total: .2f} (Serviço: {valor_servico}, Páginas: {num_pag}, Adicional: {valor_servico_extra})\nValor com Desconto: R$ {total2: .2f}")
