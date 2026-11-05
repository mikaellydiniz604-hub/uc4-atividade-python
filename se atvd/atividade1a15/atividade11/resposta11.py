curtidas = int(input("quantidade de curtidas: "))
comentarios = int(input("Quantidade de comentarios: "))
pontos = int(input("Pontos Inicial: "))

if curtidas >= 100 and comentarios >= 30:
  pontos - pontos + 50

print("Pontuação final:", pontos)