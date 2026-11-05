estado = int(input("Estao (1=ocupado, 0=livre): "))

ocupado = (estado == 1)

if not ocupado:
  print("Computador disponível!")
  print("Atualização autorizada.")
else:
  print("Computador ocupado.")
  print("Atualização não autorizda.")