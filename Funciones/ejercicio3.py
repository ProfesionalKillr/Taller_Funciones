def curso(notas):
    calificaciones = {}
    for asignatura, nota in notas.items():
        asignatura_mayusculas = asignatura.upper()
        if nota < 5:
            calificaciones[asignatura_mayusculas] = "Mal"
        elif nota < 7:
            calificaciones[asignatura_mayusculas] = "Regular"
        elif nota < 9:
            calificaciones[asignatura_mayusculas] = "Bueno"
        elif nota < 10:
            calificaciones[asignatura_mayusculas] = "Muy bien"
        else:
            calificaciones[asignatura_mayusculas] = "Excelente"
    return calificaciones
notas = {"Matemáticas": 7.5, "Historia": 6.8, "Ciencias": 9.2}
calificaciones = curso(notas)
print(calificaciones)
