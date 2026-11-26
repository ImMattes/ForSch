import math
# proměnné a řetězce

jmeno = "Petr"
vek = 25
print("Jmenuju se", jmeno, "a je mi", vek, "let")

print("======================")

numbers = [2, 4, 3, 18, 5, 6, 7, 8, 9, 10]

numbers.append(11)
numbers.sort()
print("Seřazeny seznam:", numbers)
print("První řádek seznamu:", numbers[0])
print("Poslední řádek seznamu:", numbers[-1])

print("======================")

student = {
    "jmeno": "Lojza",
    "vek": 20,
    "predmety": ["Matematika, Fyzika"]
}

student ["vek"] = 25
student ["jmeno"] = "Petr"
student ["predmety"] = ["Matematika", "Fyzika", "Informatika"]
print ("Student:", student)

print("======================")

data = [3, 3, 3, 4, 5, 6, 7, 8, 9, 9, 9, 10]
uniuque_data = set(data)
print("Unikátní hodnoty:", uniuque_data)

for i in range(1, 11):
    if i % 3 == 0:
        print("Je delitelne 3")
    elif i % 5 == 0:
        print("Je delitelne 5")
    else:
        print(i)

def vypocet_obvodu_obdelniku(delka, sirka):
    return 2 * (delka + sirka)

delka = 5
sirka = 3
print("Obvod obdélmíku s délkou", delka, "a šířkou", sirka, "je:", vypocet_obvodu_obdelniku(delka, sirka))