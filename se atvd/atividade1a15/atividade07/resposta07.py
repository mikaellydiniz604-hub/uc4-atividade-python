reproduções = int(input("Quantidade de reproduções: "))
curtidas = int(input("Quantidade de curtidas: "))
valor = float(input("valor arrecadado: R$ ")) 

if reproduções > 1000 or curtidas > 200:
  valor = valor + 150

print("Valor final: R$", valor)