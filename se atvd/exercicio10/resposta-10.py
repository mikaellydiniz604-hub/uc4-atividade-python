mensalidade = float(input("Digite o valor de mensalidade: R$"))
if mensalidade >= 500:
  mensalidade = mensalidade - 50
print(f"Mensalidade atualizada: R$ {mensalidade:.2f}")