import random

def obtener_jugada_usuario():
    jugada = input("Ingrese su jugada (piedra, papel o tijera): ")
    jugada = jugada.lower()
    while jugada not in ["piedra", "papel", "tijera"]:
        print("Jugada inválida. Intente nuevamente.")
        jugada = input("Ingrese su jugada (piedra, papel o tijera): ")
        jugada = jugada.lower()
    return jugada
def obtener_jugada_computadora():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)
def determinar_ganador(jugada_usuario, jugada_computadora):
    if jugada_usuario == jugada_computadora:
        return "Empate"
    elif jugada_usuario == "piedra":
        if jugada_computadora == "papel":
            return "Gana la PC"
        else:
            return "Gana el usuario"
    elif jugada_usuario == "papel":
        if jugada_computadora == "tijera":
            return "Gana la PC"
        else:
            return "Gana el usuario"
    elif jugada_usuario == "tijera":
        if jugada_computadora == "piedra":
            return "Gana la PC"
        else:
            return "Gana el usuario"
while True:
    print("Juego de Piedra, Papel o Tijera")
    print("1. Jugar")
    print("2. Salir")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        jugada_usuario = obtener_jugada_usuario()
        jugada_computadora = obtener_jugada_computadora()
        resultado = determinar_ganador(jugada_usuario, jugada_computadora)
        print("Jugada de la PC:", jugada_computadora)
        print("Resultado:", resultado)
    elif opcion == 2:
        break
    else:
        print("Opción inválida")
