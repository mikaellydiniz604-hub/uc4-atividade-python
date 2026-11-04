transferência = float(input("Digite o valor da trasferência"))
if transferência > 1000:
    trasnferência = transferência + 15
print(f"Valor total a pagar: R$ {transferência: .2f}")