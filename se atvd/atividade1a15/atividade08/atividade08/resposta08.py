execuções = int(input("Quantidade de execuções: "))
musicas = int(input("Músicas disponíveis: "))

if execuções >= 10:
  musicas = musicas + 5

print("Quantidade final de musicas:", musicas)