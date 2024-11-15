num_alumnos = int(input("\nIntroduce el número de alumnos que asistirán al viaje: "))

if num_alumnos >= 100:
    costo_por_alumno = 65
    costo_total = num_alumnos * costo_por_alumno
elif 50 <= num_alumnos <= 99:
    costo_por_alumno = 70
    costo_total = num_alumnos * costo_por_alumno
elif 30 <= num_alumnos <= 49:
    costo_por_alumno = 95
    costo_total = num_alumnos * costo_por_alumno
else:
    costo_por_alumno = 4000 / num_alumnos
    costo_total = 4000

print("\nEl costo total a pagar a la compañía de autobuses es de:", costo_total, "euros")
print("Cada alumno debe pagar:", costo_por_alumno, "euros")