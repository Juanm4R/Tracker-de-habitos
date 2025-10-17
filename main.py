import matplotlib.pyplot as plt

habitos = []

def grafico_barras():
    if not habitos:
        print("No hay hábitos cargados.")
        return

    nombres = []
    porcentajes = []
    for nombre, progreso in habitos:
        if len(progreso) > 0:
            porcentaje = (sum(progreso) / len(progreso)) * 100
        else:
            porcentaje = 0
        nombres.append(nombre)
        porcentajes.append(porcentaje)

    plt.bar(nombres, porcentajes, color="skyblue", edgecolor="black")
    plt.ylabel("Cumplimiento (%)")
    plt.title("Porcentaje de cumplimiento por hábito")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def grafico_torta():
    if not habitos:
        print("No hay hábitos cargados.")
        return

    cumplidos = sum(sum(cumplimiento) for nombre, cumplimiento in habitos)
    no_cumplidos = sum(len(cumplimiento) - sum(cumplimiento) for nombre, cumplimiento in habitos)

    if cumplidos + no_cumplidos == 0:
        print("Aún no hay registros para mostrar.")
        return

    plt.pie(
        [cumplidos, no_cumplidos],
        labels=["Cumplidos", "No cumplidos"],
        autopct="%1.1f%%",
        colors=["lightgreen", "lightcoral"]
    )
    plt.title("Proporción total de cumplimiento")
    plt.show()

def marcar_habito(cumplido=True):
    if not mostrar_habitos():
        return
    try:
        num = int(input("Ingrese el número del hábito a marcar: "))
        if 1 <= num <= len(habitos):
            habitos[num-1][1].append(1 if cumplido else 0)
            estado = "cumplido" if cumplido else "no cumplido"
            print(f"\nSe registró el hábito '{habitos[num-1][0]}' como {estado}.")
        else:
            print("\n Número inválido.")
    except ValueError:
        print("\n Debe ingresar un número.")

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



#_______PREMIO POR PROGRESO_______#
import random

def premio_por_progreso(habito, cumplido, total):
    if total == 0:
        return  
    
    porcentaje = round((cumplido / total) * 100)

    
    mensajes = {
        "bronce": [
            "¡Bien hecho! Vas dando tus primeros pasos.",
            "Estás comenzando a construir el hábito, seguí así.",
        ],
        "plata": [
            "¡Muy bien! Llevás más de la mitad del objetivo cumplido.",
            "Vas avanzando con constancia, no pares ahora.",
        ],
        "oro": [
            "¡Excelente! Ya casi llegás a tu meta.",
            "Gran esfuerzo, estás cerca de lograrlo.",
        ],
        "diamante": [
            "¡Felicitaciones! Cumpliste el 100% de tu hábito.",
            "Objetivo alcanzado, lograste tu meta con éxito.",
        ]
    }
    categoria = ""
    if porcentaje >= 100:
        categoria = "diamante"
    elif porcentaje >= 75:
        categoria = "oro"
    elif porcentaje >= 50:
        categoria = "plata"
    elif porcentaje >= 25:
        categoria = "bronce"
    else:
        categoria = "inicial"

    print("Progreso en", habito + ":", porcentaje, "%")

    if categoria in mensajes:
        print(random.choice(mensajes[categoria]))
    else:
        print("Todavía estás comenzando, cada pequeño paso cuenta.")
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
        print("7. Ver gráfico de barras")
        print("8. Ver gráfico de torta")
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
        elif opcion == "7":
            grafico_barras()
        elif opcion == "8":
            grafico_torta()
        elif opcion == "0":
            print("\n¡Hasta la próxima!")
            break
        else:
            print("\n Opción no válida.")

if __name__ == "__main__":
    menu()
