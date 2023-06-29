pasajeros = [("Manuel Juárez", 19823451, "Armenia"),
             ("Gloria Galvis", 45789234, "Cali"),
             ("Rosa Ortiz", 45456234, "Medellín"),
             ("Eduardo Carrasquilla", 79844677, "Cali")]
ciudades = [("Armenia", "Quindío"),
            ("Cali", "Valle"),
            ("Medellín", "Antioquia")]
def agregar_pasajero(pasajeros):
    nombre = input("Ingrese el nombre del pasajero: ")
    identificacion = int(input("Ingrese la identificación del pasajero: "))
    destino = input("Ingrese el destino del pasajero: ")
    pasajeros.append((nombre, identificacion, destino))
    return pasajeros
def agregar_ciudad(ciudades):
    ciudad = input("Ingrese el nombre de la ciudad: ")
    departamento = input("Ingrese el nombre del departamento: ")
    ciudades.append((ciudad, departamento))
    return ciudades
def buscar_destino_por_identificacion(pasajeros):
    identificacion = int(input("Ingrese la identificación del pasajero: "))
    for pasajero in pasajeros:
        if pasajero[1] == identificacion:
            for ciudad in ciudades:
                if ciudad[0] == pasajero[2]:
                    return ciudad[0]
            break
    return "No se encontró la ciudad destino para la identificación proporcionada."
def contar_pasajeros_por_ciudad(pasajeros):
    ciudad_destino = input("Ingrese el nombre de la ciudad destino: ")
    count = 0
    for pasajero in pasajeros:
        if pasajero[2] == ciudad_destino:
            count += 1
    return count
def buscar_pais_por_identificacion(pasajeros):
    identificacion = int(input("Ingrese la identificación del pasajero: "))
    for pasajero in pasajeros:
        if pasajero[1] == identificacion:
            for ciudad in ciudades:
                if ciudad[0] == pasajero[2]:
                    return ciudad[1]
            break
    return "No se encontró el país destino para la identificación proporcionada."
def contar_pasajeros_por_pais(pasajeros):
    pais_destino = input("Ingrese el nombre del país destino: ")
    count = 0
    for pasajero in pasajeros:
        for ciudad in ciudades:
            if ciudad[0] == pasajero[2] and ciudad[1] == pais_destino:
                count += 1
                break
    return count
while True:
    print("1. Agregar pasajeros")
    print("2. Agregar ciudades")
    print("3. Buscar ciudad destino por la identificación")
    print("4. Cantidad de pasajeros que viajan a una ciudad")
    print("5. Buscar país destino mediante la identificación")
    print("6. Cantidad de pasajeros que viajan a un país")
    print("7. Salir del programa")
    opcion = int(input("Acción a ejecutar: "))
    if opcion == 1:
        print("Agregar pasajeros")
        pasajeros = agregar_pasajero(pasajeros)
    elif opcion == 2:
        print("Agregar ciudades")
        ciudades = agregar_ciudad(ciudades)
    elif opcion == 3:
        print("Buscar ciudad destino por la identificación")
        ciudad_destino = buscar_destino_por_identificacion(pasajeros)
        print("Ciudad destino:", ciudad_destino)
    elif opcion == 4:
        print("Cantidad de pasajeros que viajan a una ciudad")
        cantidad_pasajeros = contar_pasajeros_por_ciudad(pasajeros)
        print("Cantidad de pasajeros:", cantidad_pasajeros)
    elif opcion == 5:
        print("Buscar país destino mediante la identificación")
        pais_destino = buscar_pais_por_identificacion(pasajeros)
        print("País destino:", pais_destino)
    elif opcion == 6:
        print("Cantidad de pasajeros que viajan a un país")
        cantidad_pasajeros = contar_pasajeros_por_pais(pasajeros)
        print("Cantidad de pasajeros:", cantidad_pasajeros)
    elif opcion == 7:
        break
    else:
        print("Opción inválida")

