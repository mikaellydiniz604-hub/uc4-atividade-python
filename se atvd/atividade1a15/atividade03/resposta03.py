jogos = int(input("Quantidade de jogos: "))
valor = float(input("Valor da compra: R$ "))
pontos = int(input("Pontos iniciais: "))

if jogos >= 3 and valor > 500:
  pontos = pontos + 200

print("Prontuação final:", pontos)