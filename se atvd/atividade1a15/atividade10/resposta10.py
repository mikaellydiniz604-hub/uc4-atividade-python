livros = int(input("Quantidade de livros: "))
jogos = int(input("Quantidade de jogos: "))
valor = float(input("Valor total: R$ "))

if livros >= 2 or jogos >= 3:
  valor = valor - 25

print("valor final: R$", valor)