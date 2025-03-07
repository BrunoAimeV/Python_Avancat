from abc import ABC, abstractmethod

# Clase abstracta Animal
class Animal(ABC):
    def __init__(self, especie, edat):
        self.especie = especie
        self.edat = edat

    @abstractmethod
    def xerrar(self):
        pass

    @abstractmethod
    def mourem(self):
        pass

    def quisoc(self):
        print(f"Sóc un {self.especie} de {self.edat} anys.")

# Subclase Cavall
class Cavall(Animal):
    def xerrar(self):
        print("El cavall fa: Íiiiiii!")

    def mourem(self):
        print("El cavall galopa.")

# Subclase Dofí
class Dofi(Animal):
    def xerrar(self):
        print("El dofí fa: Click click!")

    def mourem(self):
        print("El dofí neda.")

# Subclase Abella
class Abella(Animal):
    def xerrar(self):
        print("L'abella fa: Zzzzzz!")

    def mourem(self):
        print("L'abella vola.")

    def picar(self):
        print("L'abella ha picat!")

# Subclase Humà
class Huma(Animal):
    def __init__(self, especie, edat, nom):
        super().__init__(especie, edat)
        self.nom = nom

    def xerrar(self):
        print(f"{self.nom} diu: Hola!")

    def mourem(self):
        print(f"{self.nom} camina.")

# Subclase Fiet
class Fiet(Huma):
    def __init__(self, especie, edat, nom, pares):
        super().__init__(especie, edat, nom)
        self.pares = pares

    def nompares(self):
        print(f"Els pares de {self.nom} són: {', '.join(self.pares)}")

# Subclase Centaure
class Centaure(Cavall, Huma):
    def __init__(self, especie, edat, nom):
        super().__init__(especie, edat, nom)

    def xerrar(self):
        print("El centaure fa: Salutacions!")

    def mourem(self):
        print("El centaure corre i camina.")

# Clase Xou
class Xou:
    def __init__(self, especie, edat):
        self.especie = especie
        self.edat = edat

    def xerrar(self):
        print("El xou fa: Xou xou!")

    def mourem(self):
        print("El xou es mou estranyament.")

    def quisoc(self):
        print(f"Sóc un {self.especie} de {self.edat} anys.")

# Crear una llista d'elements de cada tipus
animals = [
    Cavall("Cavall", 5),
    Dofi("Dofí", 10),
    Abella("Abella", 1),
    Huma("Humà", 30, "Joan"),
    Fiet("Humà", 5, "Pepet", ["Joan", "Maria"]),
    Centaure("Centaure", 100, "Quiron"),
    Xou("Xou", 2)
]

# Bucle que crida als mètodes iguals
for animal in animals:
    animal.quisoc()
    animal.xerrar()
    animal.mourem()
    if isinstance(animal, Abella):
        animal.picar()
    if isinstance(animal, Fiet):
        animal.nompares()
    print("-" * 20)