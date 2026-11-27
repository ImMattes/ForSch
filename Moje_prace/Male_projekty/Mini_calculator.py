a = int(input("Zadejte první číslo:"))
b = int(input("Zadejte druhé číslo:"))

pocetni_operace = input("Chcete sčítat nebo odčítat?").strip().lower()


while pocetni_operace not in ("sčítat", "odčítat"):
    pocetni_operace = input("Error! Zadejte platnou početní operaci:").strip().lower()

if pocetni_operace == "sčítat":
    print(a + b)
   
elif pocetni_operace == "odčítat":
    print(a - b)