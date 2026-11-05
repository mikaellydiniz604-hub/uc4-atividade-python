alunos = int(input("Quantidade total de alunos: "))
presentes = int(input("Quantidade de presentes: "))
media = float(input("Média geral da turma: "))

if presentes == alunos and media >= 8:
  valor = alunos * 5 
  print("Compra autorizada!")
  print("Custo total: R$", valor)
else:
  print("A turma não cumpriu os requisitos.")