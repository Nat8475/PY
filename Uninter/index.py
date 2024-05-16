nome = input("Qual seu Nome:")
media = float(input("Quanto é a média minima para Aprovação?"))
nota1 = float(input("Quanto foi sua Primeira nota?"))
nota2 = float(input("Quanto foi sua Segunda nota?"))
nota3 = float(input("Quanto foi sua Terceira nota"))

mdf = (nota1 + nota2 + nota3)/3

if(media <= mdf):
    print(f"Meus parabéns {nome}, você foi aprovado com média de {mdf: .1f}")
else:
    print(f"{nome}, infelizmente você Reprovou, sua média foi {mdf: .1f}")