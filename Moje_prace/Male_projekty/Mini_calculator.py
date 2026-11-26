a = int(input("Zadejte první číslo:"))
b = int(input("Zadejte druhé číslo:"))

pocetni_operace = input("Chcete sčítat nebo odčítat?")

while True:
    if pocetni_operace == "sčítat":
        print(a + b)
        break
    elif pocetni_operace == "odčítat":
        print(a - b)
        break
    else:
        while pocetni_operace != "sčítat" or pocetni_operace != "odčítat":
            pocetni_operace = input("Error! Zadejte platnou početní operaci:")
            break