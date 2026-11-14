a = int(input("Zadejte první číslo:"))
b = int(input("Zadejte druhé číslo:"))

pocetni_operace = input("Chcete sčítat nebo odčítat?")

if pocetni_operace == "sčítat":
    print(a + b)
elif pocetni_operace == "odčítat":
    print(a - b)
else:
    print("Error!")