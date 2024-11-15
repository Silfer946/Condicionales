
nota = float(input("\nIntroduce la nota: "))
edad = int(input("Introduce la edad: "))
sexo = input("Introduce el sexo (F/M): ") 

if nota >= 5 and edad >= 18 and sexo == 'f':
    print("\nACEPTADA")
elif nota >= 5 and edad >= 18 and sexo == 'm':
    print("\nPOSIBLE")
else:
    print("\nNO ACEPTADA") 