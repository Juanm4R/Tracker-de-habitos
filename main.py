habitos = []

def agregar_habito(nombre):
    habitos.append([nombre, []])
    print(f"\nHábito '{nombre}' agregado.")

def eliminar_habito():
    if not mostrar_habitos():
        return
    try:
        num = int(input("Ingrese el número del hábito a eliminar: "))
        if 1 <= num <= len(habitos):
            nombre = habitos[num-1][0]
            habitos.pop(num-1)
            print(f"\n Hábito '{nombre}' eliminado.")
        else:
            print("\n Número inválido.")
    except ValueError:
        print("\n Debe ingresar un número.")

def mostrar_habitos():
    if not habitos:
        print("No hay hábitos cargados.")
        return False
    print("Lista de Hábitos")
    for i, (nombre, progreso) in enumerate(habitos, 1):
        cumplidos = sum(progreso)
        print(i, ".", nombre, "- Cumplidos:", cumplidos, "/", len(progreso))
    return True

def ver_estadisticas():
    if not habitos:
        print("No hay hábitos para mostrar estadísticas.")
        return

    estadisticas = []
    for nombre, progreso in habitos:
        total = 0
        for valor in progreso:
            total += valor

        if len(progreso) > 0:
            porcentaje = (total / len(progreso)) * 100
            estadisticas.append([nombre, porcentaje, total, len(progreso)])
        else:
            estadisticas.append([nombre, 0, 0, 0])

    n = len(estadisticas)
    for i in range(n):
        for j in range(0, n - i - 1):
            if estadisticas[j][1] < estadisticas[j + 1][1]:
                estadisticas[j], estadisticas[j + 1] = estadisticas[j + 1], estadisticas[j]

    for nombre, porcentaje, total, cantidad in estadisticas:
        print(f"Hábito: {nombre} - {porcentaje:.2f}% ({total}/{cantidad})")

def menu():
    while True:
        print("\n=== Tracker de Hábitos ===")
        print("1. Ver hábitos")
        print("2. Agregar hábito")
        print("3. Eliminar hábito")
        print("4. Marcar hábito como cumplido")
        print("5. Marcar hábito como no cumplido")
        print("6. Ver estadísticas (ranking)")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_habitos()
        elif opcion == "2":
            nombre = input("Ingrese el nombre del hábito: ")
            agregar_habito(nombre)
        elif opcion == "3":
            eliminar_habito()
        elif opcion == "4":
            marcar_habito(True)
        elif opcion == "5":
            marcar_habito(False)
        elif opcion == "6":
            ver_estadisticas()
        elif opcion == "0":
            print("\n¡Hasta la próxima!")
            break
        else:
            print("\n Opción no válida.")

if __name__ == "__main__":
    menu()