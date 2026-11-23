import math

print("číslo PI:", math.pi)
print("Sinus 90 stupňů:", math.sin(math.pi/2))

print("=========================================")

def bezpecne_deleni(a,b):
    try:
        vysledek = a / b
    except ZeroDivisionError as zde:
        print("Chyba:", zde)
        return None
    except Exception as e:
        zprava = f"Nelze dělit objekt {a} / {b}: {e}"
        raise Exception(zprava)
    finally:
        print("děleni bylo povedeno")
        print("Tento blok se provede vždy")
    return vysledek

print(bezpecne_deleni(10, 2))
print(bezpecne_deleni(10, 0))