# Develop a program that reads how much money a person has in their wallet and shows how many dollars they can buy

brlInput = float(input("Please insert how much R$ (BRL) do you want to convert (integer or float numbers are supported): "))
brlToUsd = brlInput / 4.91

print(f"Conversion results:\n R$ {brlInput}\n $ {brlToUsd:.2f}")
