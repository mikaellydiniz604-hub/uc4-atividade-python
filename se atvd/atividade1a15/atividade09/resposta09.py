inscritos = int(input("Quantidade de inscitos: "))
cadeiras = int(input("Quantidade de cadeiras: "))

if inscritos > 80 and cadeiras < inscritos:
  cadeiras = cadeiras + 30 

print("quantidade final de caderias:", cadeiras)