#BOAS VINDAS 

print("Olá, Seja Bem-Vindo a Livraria do Natã")

#VARIAVEIS

lista_livro = []
id_global = 0

def cadastrar_livros(id):

    livro = dict()

    #Inputs que fornece as informções de cadastro do Livro
    livro["id"] = id

    livro["nome"] = str(input("Nome do Livro:"))
    livro["autor"] = str(input("Autor do Livro: "))
    livro["editora"] = str(input("Editora do Livro: "))


    #Adiciona o livro na lista
    lista_livro.append(livro)


#FUNÇÃO PARA CONSULTA DOS LIVROS


def consultar_livro():

    while True:
        
        try:

            print("Opções de consulta disponíveis:\n1 - Consultar Todos\n2- Consultar por ID\n3 - Consultar por Autor\n4 - Retornar ao Menu")
            consulta = int(input(">>>"))

        #TRATAMENTO DE EXECEÇÃO

        except ValueError:
            print("O Valor inserido é inválido.")
            continue

        #Verifica de se o valor Inserido está entre as opções


        if (consulta > 4) or (consulta < 0):
            print("O valor inserido é Inválido, Tente Novamente.")
            continue
        
        #Faz o Print dos Cadastros com base na escolha

        match consulta:

            #Mostra todos os Livros Cadastrados
            case 1:
                for i in lista_livro:
                    print("-"*50 + f"\nID: {i['id']}\nNome: {i['nome']}\nAutor: {i['autor']}\nEditora: {i['editora']}\n" + "-"*50)


            #Mostra o livro com base no ID

            case 2:
                id_consulta = int(input("DIgite o ID: "))

                for i in lista_livro:
                    if i["id"] == id_consulta:
                        print("-"*50 + f"\nID: {i["id"]}\nNome: {i["nome"]}\nAutor: {i["autor"]}\nEditora: {i["editora"]}\n" + "-"*50)

            #Mostra os livros do mesmo Autor
            case 3:
                autor_consulta = str(input("Insira o Autor: "))

                for i in lista_livro:
                    if i["autor"] == autor_consulta:
                        print("-"*50 + f"\nID: {i["id"]}\nNome: {i["nome"]}\nAutor: {i["autor"]}\nEditora: {i["editora"]}\n" + "-"*50)

            #Encerra o menu
            case 4:
                break


#Função para Remover os Livros Cadastrado

def remover_livros():

    while True:
            
            id_remove = int(input("Digite o ID: "))

            for i in lista_livro:

            #Se o ID está Cadastrado apaga o cadastro
                if i["id"] == id_remove:
                
                    x = lista_livro.index(i)

                    lista_livro.pop(x)

                    print("O Livro foi removido com Sucesso!")

                    return
            print("O id Inserido é inválido")


# MENU PRINCIPAL
while True:

    try:
        print("\tMenu Principal:\n1 - Cadastrar Livro\n2 - Consultar Livro\n3 - Remover Livro\n4 -Encerrar Programa")
        indice = int(input(">>>"))

    #TRATAMENTO DE EXECEÇÃO

    except ValueError:
        print("O Valor inserido é Inválido, Tente Novamente")
        continue

    #Verifica de se o valor Inserido está entre as opções

    if(indice > 4) or (indice <0):
        print("O valor inserido é Inválido, Tente Novamente.")
        continue

    #Chama as Funções de acordo com a Escolha

    match indice:
        case 1:
            id_global += 1
            cadastrar_livros(id_global)
        case 2:
            consultar_livro()
        case 3:
            remover_livros()
        case 4:
            break
        