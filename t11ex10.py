def dividir():
    a = float(input("Introdueix el primer nombre: "))
    b = float(input("Introdueix el segon nombre: "))
    if b == 0:
        return "No es pot dividir per zero."
    return a / b

resultat = dividir()
print(resultat)
