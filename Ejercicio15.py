jugador1 = input("Jugador 1, elige Piedra, Papel o Tijera: ").lower()
jugador2 = input("Jugador 2, elige Piedra, Papel o Tijera: ").lower()


if jugador1 not in ['piedra', 'papel', 'tijera'] or jugador2 not in ['piedra', 'papel', 'tijera']:
    print("Opción incorrecta.")
else:

    if jugador1 == jugador2:
        print("Empate.")
    elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijera" and jugador2 == "papel"):
        print("Gana Jugador 1.")
    else:
        print("Gana Jugador 2.")