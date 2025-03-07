def llegir_fitxer(nom_fitxer):
    try:
        with open(nom_fitxer, 'r') as fitxer:
            contingut = fitxer.read()
            return contingut
    except FileNotFoundError:
        return f"Error: El fitxer {nom_fitxer} no existeix."
    except Exception as e:
        return f"Error: S'ha produït un problema en obrir el fitxer. Detall: {e}"

# Exemple d'ús
resultat = llegir_fitxer('exemple.txt')
print(resultat)
