numero_dado = int(input("\nIntroduce el resultado del dado (1-6): "))


caras_opuestas = {1: "seis", 2: "cinco", 3: "cuatro", 4: "tres", 5: "dos", 6: "uno"}


if 1 <= numero_dado <= 6:
    print(f"La cara opuesta al {numero_dado} es {caras_opuestas[numero_dado]}.")
else:
    print("ERROR: número incorrecto.")