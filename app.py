import random

opciones = ('rock', 'paper', 'scissors')

while True:
    eleccion_usuario = input("Elige una opción: rock, paper, scissors: ").lower()
    if eleccion_usuario not in opciones:
        print("Opción no válida. Inténtalo de nuevo.")
        continue
    eleccion_oponente = random.choice(opciones)
    if eleccion_usuario == eleccion_oponente:
        print("Es un empate.")
    elif (eleccion_usuario == "rock" and eleccion_oponente == "scissors") or \
         (eleccion_usuario == "scissors" and eleccion_oponente == "paper") or \
         (eleccion_usuario == "paper" and eleccion_oponente == "rock"):
        print("Has ganado.")
    else:
        print("Has perdido.")
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if jugar_de_nuevo != "s":
        break