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


# Ejecutar programa
if __name__ == "__main__":
    menu()