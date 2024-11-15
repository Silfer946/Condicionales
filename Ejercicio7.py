
base = int(input("\nIntroduce la base: "))
exponente = int(input("Introduce el exponente: "))

if exponente > 0:
    resultado = base ** exponente
    print("\nLa potencia es:",resultado)
elif exponente == 0:
    print("\nEl resultado es: 1")
else:  
    resultado = 1 / (base ** abs(exponente))
    print("\nLa potencia es:",resultado)