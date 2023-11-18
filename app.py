import random

opciones = ('piedra', 'papel', 'tijeras')
victorias = 0
derrotas = 0
empates = 0

while True:
    eleccion_usuario = input("Elige una opción: piedra, papel, tijeras: ").lower()
    if eleccion_usuario not in opciones:
        print("Opción no válida. Inténtalo de nuevo.")
        continue
    eleccion_oponente = random.choice(opciones)
    if eleccion_usuario == eleccion_oponente:
        print("Es un empate.")
        empates += 1
    elif (eleccion_usuario == "piedra" and eleccion_oponente == "tijeras") or \
         (eleccion_usuario == "tijeras" and eleccion_oponente == "papel") or \
         (eleccion_usuario == "papel" and eleccion_oponente == "piedra"):
        print("Has ganado.")
        victorias += 1
    else:
        print("Has perdido.")
        derrotas += 1
    print(f"Victorias: {victorias}, Derrotas: {derrotas}, Empates: {empates}")
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if jugar_de_nuevo != "s":
        break