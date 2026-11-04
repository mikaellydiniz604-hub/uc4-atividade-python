temperatura = float(input("Digite a temperatura atual em °C: "))
if temperatura > 35:
    temperatura = temperatura + 5
print(f"temperatura final: {temperatura: .1f} °C")