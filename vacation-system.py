print("""Bienvenido al portal para calcular los dias de
vacaciones disponibles para los trabajadores de Rappi\n""")

vacaciones = {
    "clave 1": (6, 14, 20),
    "clave 2": (7, 15, 22),
    "clave 3": (10, 20, 30)
}

while True:

    nombre = input("Ahora escribe tu nombre completo: ")
    clave = input("Escribe tu clave de departamento: ").lower().strip()

    if clave not in vacaciones:
        print("Esa clave no existe, intenta otra vez.\n")
        continue

    try:
        anti = int(input("¿Cuántos años tienes trabajando para Rappi? "))
    except ValueError:
        print("Eso no es un número válido.\n")
        continue

    
    if anti <= 1:
        dias = vacaciones[clave][0]
    elif anti <= 6:
        dias = vacaciones[clave][1]
    else:
        dias = vacaciones[clave][2]

    print(f"\n{nombre}, tienes {dias} días de vacaciones disponibles.\n")

    continuar = input(f"{nombre}, ¿deseas hacer otra consulta? (si/no): ")
    if continuar.lower() != "si":
        print("Bueno, ahí nos vemos 👋")
        break
