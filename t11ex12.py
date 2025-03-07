import os

# Crear el directori "Prova" dins /home/cicles/AO
directori = "/home/cicles/AO/Prova"
os.makedirs(directori, exist_ok=True)

# Canviar-nos a aquest directori
os.chdir(directori)

# Crear el fitxer Ex12.txt i posar els noms dels companys de classe
companys = ["Joan", "Maria", "Pau", "Anna"]  # Afegir els noms dels companys
with open("Ex12.txt", "w") as fitxer:
    fitxer.write("\n".join(companys))

# Obrir el fitxer per afegir els noms dels professors
professors = ["Sr. Pérez", "Sra. López"]  # Afegir els noms dels professors
with open("Ex12.txt", "a") as fitxer:
    fitxer.write("\n" + "\n".join(professors))

# Obrir el fitxer i posar el seu contingut dins una llista de noms
noms = []
with open("Ex12.txt", "r") as fitxer:
    noms = fitxer.readlines()

# Eliminar el salt de línia final de cada nom
noms = [nom.strip() for nom in noms]

print(noms)
