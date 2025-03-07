import random

def imprimir_tauler(tauler):
    for fila in tauler:
        print(" | ".join(fila))
        print("-" * 9)

def verificar_guanyador(tauler, jugador):
    for fila in tauler:
        if all(c == jugador for c in fila):
            return True
    
    for col in range(3):
        if all(tauler[fila][col] == jugador for fila in range(3)):
            return True
    
    if all(tauler[i][i] == jugador for i in range(3)) or all(tauler[i][2 - i] == jugador for i in range(3)):
        return True
    
    return False

def moviments_disponibles(tauler):
    return [(r, c) for r in range(3) for c in range(3) if tauler[r][c] == " "]

def moviment_maquina(tauler):
    return random.choice(moviments_disponibles(tauler))

def tres_en_ratlla():
    tauler = [[" "] * 3 for _ in range(3)]
    mode = input("Vols jugar contra un altre jugador (2) o contra la màquina (1)? ")
    
    jugadors = {"X": "Jugador 1", "O": "Jugador 2" if mode == "2" else "Màquina"}
    jugador_actual = "X"
    
    while moviments_disponibles(tauler):
        imprimir_tauler(tauler)
        print(f"Torn de {jugadors[jugador_actual]} ({jugador_actual})")
        
        if mode == "1" and jugador_actual == "O":
            fila, col = moviment_maquina(tauler)
        else:
            while True:
                try:
                    fila, col = map(int, input("Introdueix fila i columna (0-2): ").split())
                    if (fila, col) in moviments_disponibles(tauler):
                        break
                    else:
                        print("Moviment no vàlid, torna a intentar-ho.")
                except ValueError:
                    print("Entrada no vàlida, introdueix dos números separats per espai.")
        
        tauler[fila][col] = jugador_actual
        
        if verificar_guanyador(tauler, jugador_actual):
            imprimir_tauler(tauler)
            print(f"{jugadors[jugador_actual]} ({jugador_actual}) ha guanyat!")
            return
        
        jugador_actual = "O" if jugador_actual == "X" else "X"
    
    imprimir_tauler(tauler)
    print("Empat!")

tres_en_ratlla()