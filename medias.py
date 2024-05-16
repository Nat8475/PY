print("\tCalculadora de Notas")

qtd_notas = int(input("Quantidade de Notas?"))

media = 0
cont_notas = 1

while(cont_notas <= qtd_notas):
    x = float(input(f"Digite a {cont_notas} nota: "))
    media = media + x
    cont_notas = cont_notas + 1

media = media / qtd_notas
print(f"A média das notas é: {media}")