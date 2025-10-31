import matplotlib.pyplot as plt
import random
import json
import os
from datetime import datetime
from functools import reduce

ARCHIVO_DATOS = "datos_usuario.json"
DIAS = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")

def guardar_datos(habitos, plan_semanal, historial):
    datos = {
        "habitos": habitos,
        "plan_semanal": plan_semanal,
        "historial": historial
    }
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)


def cargar_datos():
    if os.path.exists(ARCHIVO_DATOS):
        try:
            with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
                datos = json.load(f)
                habitos = datos.get("habitos", [])
                plan_semanal = datos.get("plan_semanal", [])
                historial = datos.get("historial", {})

                for i in range(len(habitos)):
                    habitos[i][1] = [int(x) for x in habitos[i][1]]

                print("Datos cargados correctamente.")
                return habitos, plan_semanal, historial
        except Exception as e:
            print("Error al cargar los datos:", e)
    else:
        print("No se encontró un archivo de datos previo. Se creará uno nuevo al guardar.")
    return [], [], {}

def editar_habito(habitos):
    if not habitos:
        print("No hay hábitos para editar.")
        return habitos
    for i, (nombre, progreso) in enumerate(habitos, start=1):
        print(i, "-", nombre)
    try:
        indice = int(input("Ingrese el número del hábito a editar: ")) - 1
        if indice < 0 or indice >= len(habitos):
            print("Número inválido.")
            return habitos
        nuevo_nombre = input("Ingrese el nuevo nombre del hábito: ").strip()
        if nuevo_nombre == "":
            print("El nombre no puede estar vacío.")
            return habitos
        anterior = habitos[indice][0]
        habitos[indice][0] = nuevo_nombre
        print("Hábito editado:", anterior, "→", nuevo_nombre)
        cargar_datos()
    except ValueError:
        print("Debe ingresar un número válido.")
    return habitos


def grafico_barras(habitos):
    if not habitos:
        print("No hay hábitos cargados.")
        return

    nombres, porcentajes = [], []
    for nombre, progreso in habitos:
        porcentaje = (sum(progreso) / len(progreso)) * 100 if len(progreso) > 0 else 0
        nombres.append(nombre)
        porcentajes.append(porcentaje)

    plt.bar(nombres, porcentajes, color="skyblue", edgecolor="black")
    plt.ylabel("Cumplimiento (%)")
    plt.title("Porcentaje de cumplimiento por hábito")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def grafico_torta(habitos):
    if not habitos:
        print("No hay hábitos cargados.")
        return

    cumplidos = sum(sum(c) for _, c in habitos)
    no_cumplidos = sum(len(c) - sum(c) for _, c in habitos)

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


def registrar_historial(historial, nombre, cumplido):
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    if nombre not in historial:
        historial[nombre] = []
    historial[nombre].append({"fecha": fecha_actual, "cumplido": cumplido})
    return historial


def marcar_habito(habitos, historial, cumplido=True):
    if not mostrar_habitos(habitos):
        return habitos, historial
    try:
        num = int(input("Ingrese el número del hábito a marcar: "))
        if 1 <= num <= len(habitos):
            habitos[num-1][1].append(1 if cumplido else 0)
            estado = "cumplido" if cumplido else "no cumplido"
            print(f"\nSe registró el hábito '{habitos[num-1][0]}' como {estado}.")
            historial = registrar_historial(historial, habitos[num-1][0], 1 if cumplido else 0)
        else:
            print("\nNúmero inválido.")
    except ValueError:
        print("\nDebe ingresar un número.")
    return habitos, historial


def agregar_habito(habitos, nombre):
    habitos.append([nombre, []])
    print(f"\nHábito '{nombre}' agregado.")
    return habitos


def eliminar_habito(habitos, historial):
    if not mostrar_habitos(habitos):
        return habitos, historial
    try:
        num = int(input("Ingrese el número del hábito a eliminar: "))
        if 1 <= num <= len(habitos):
            nombre = habitos[num-1][0]
            habitos.pop(num-1)
            historial.pop(nombre, None)
            print(f"\nHábito '{nombre}' eliminado.")
        else:
            print("\nNúmero inválido.")
    except ValueError:
        print("\nDebe ingresar un número.")
    return habitos, historial


def premio_por_progreso(habito, cumplido, total):
    if total == 0:
        return
    porcentaje = round((cumplido / total) * 100)

    mensajes = {
        "bronce": ["¡Bien hecho! Vas dando tus primeros pasos.", "Estás comenzando a construir el hábito, seguí así."],
        "plata": ["¡Muy bien! Llevás más de la mitad del objetivo cumplido.", "Vas avanzando con constancia, no pares ahora."],
        "oro": ["¡Excelente! Ya casi llegás a tu meta.", "Gran esfuerzo, estás cerca de lograrlo."],
        "diamante": ["¡Felicitaciones! Cumpliste el 100% de tu hábito.", "Objetivo alcanzado, lograste tu meta con éxito."]
    }

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


def mostrar_habitos(habitos, solo_nombres=False):
    if not habitos:
        print("No hay hábitos cargados")
        return False
    print("Lista de Hábitos")
    for i, (nombre, progreso) in enumerate(habitos, 1):
        if solo_nombres:
            print(i, ".", nombre)
        else:
            racha_actual, racha_maxima = calcular_racha(progreso)
            cumplidos = sum(progreso)
            progreso_semanal = progreso[-7:]
            cumplidos_semanales = sum(progreso_semanal)
            print(i, ".", nombre, 
                  "- Cumplidos:", cumplidos, "/", len(progreso), 
                  "Racha Actual:", racha_actual, 
                  "Racha Máxima:", racha_maxima,
                  "Últimos 7 Días:", cumplidos_semanales, "/", len(progreso_semanal))
    return True


def calcular_racha(progreso):
    racha_maxima = temp = 0
    for dia in progreso:
        if dia == 1:
            temp += 1
            racha_maxima = max(racha_maxima, temp)
        else:
            temp = 0
    racha_actual = 0
    for dia in reversed(progreso):
        if dia == 1:
            racha_actual += 1
        else:
            break
    return racha_actual, racha_maxima


def ver_estadisticas(habitos):
    if not habitos:
        print("No hay hábitos para mostrar estadísticas.")
        return
    estadisticas = []
    for nombre, progreso in habitos:
        total = sum(progreso)
        porcentaje = (total / len(progreso)) * 100 if len(progreso) > 0 else 0
        estadisticas.append([nombre, porcentaje, total, len(progreso)])
    estadisticas.sort(key=lambda x: x[1], reverse=True)
    for nombre, porcentaje, total, cantidad in estadisticas:
        print(f"Hábito: {nombre} - {porcentaje:.2f}% ({total}/{cantidad})")


def agregar_actividad(plan_semanal):
    print("\n--- Agregar Actividad ---")
    print("Días disponibles:", ", ".join(DIAS))

    dia = input("Ingrese el día: ").capitalize()
    if dia not in DIAS:
        print("Día inválido.")
        return plan_semanal

    hora = input("Ingrese la hora (HH:MM): ")
    actividad = input("Ingrese la actividad: ")

    # conjunto para evitar duplicados
    actividades_existentes = {(d, h, a) for d, h, a in plan_semanal}
    if (dia, hora, actividad) in actividades_existentes:
        print("Esa actividad ya está registrada.")
        return plan_semanal

    plan_semanal.append((dia, hora, actividad))
    print(f"Actividad '{actividad}' agregada para {dia} a las {hora}.")
    return plan_semanal


def mostrar_plan_organizado(plan_semanal):
    if not plan_semanal:
        print("No hay actividades cargadas.")
        return
    actividades_ordenadas = sorted(plan_semanal, key=lambda x: (DIAS.index(x[0]), x[1]))
    print("\n--- PLAN SEMANAL ORGANIZADO ---")
    for dia, hora, act in actividades_ordenadas:
        print(f"{dia} {hora} → {act}")


def ver_historial(historial):
    if not historial:
        print("No hay registros de historial.")
        return
    print("\nHistorial de hábitos:")
    for nombre, registros in historial.items():
        print(f"\n- {nombre}:")
        for r in registros:
            estado = "Cumplido" if r["cumplido"] == 1 else "No cumplido"
            print(f"  {r['fecha']} → {estado}")


def calcular_porcentajes_lambda(habitos):
    if not habitos:
        print("No hay hábitos cargados.")
        return

    porcentajes = list(map(lambda h: (h[0], (sum(h[1]) / len(h[1]) * 100) if len(h[1]) > 0 else 0), habitos))
    cumplidos = list(filter(lambda x: x[1] >= 50, porcentajes))
    promedio = reduce(lambda acc, h: acc + h[1], porcentajes, 0) / len(porcentajes) if porcentajes else 0

    print("\n=== Estadísticas Avanzadas (Lambda / Map / Filter / Reduce) ===")
    print("Hábitos con más del 50% de cumplimiento:")
    for nombre, p in cumplidos:
        print(f"- {nombre}: {p:.2f}%")
    print(f"\nPromedio general de cumplimiento: {promedio:.2f}%")


def menu():
    habitos, plan_semanal, historial = cargar_datos()

    while True:
        print("\n=== TRACKER DE HÁBITOS ===")
        print("1. Ver hábitos")
        print("2. Agregar hábito")
        print("3. Eliminar hábito")
        print("4. Marcar hábito como cumplido")
        print("5. Marcar hábito como no cumplido")
        print("6. Ver estadísticas (ranking)")
        print("7. Ver gráfico de barras")
        print("8. Ver gráfico de torta")
        print("9. Ver premios por progreso")
        print("10. Ver plan semanal")
        print("11. Agregar actividad al plan semanal")
        print("12. Ver historial de hábitos")
        print("13. Editar hábito")
        print("14. Estadísticas avanzadas (lambda/map/filter/reduce)")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_habitos(habitos)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del hábito: ")
            habitos = agregar_habito(habitos, nombre)
        elif opcion == "3":
            habitos, historial = eliminar_habito(habitos, historial)
        elif opcion == "4":
            habitos, historial = marcar_habito(habitos, historial, True)
        elif opcion == "5":
            habitos, historial = marcar_habito(habitos, historial, False)
        elif opcion == "6":
            ver_estadisticas(habitos)
        elif opcion == "7":
            grafico_barras(habitos)
        elif opcion == "8":
            grafico_torta(habitos)
        elif opcion == "9":
            for nombre, progreso in habitos:
                premio_por_progreso(nombre, sum(progreso), len(progreso))
        elif opcion == "10":
            mostrar_plan_organizado(plan_semanal)
        elif opcion == "11":
            plan_semanal = agregar_actividad(plan_semanal)
        elif opcion == "12":
            ver_historial(historial)
        elif opcion == "13":
            habitos = editar_habito(habitos)
        elif opcion == "14":
            calcular_porcentajes_lambda(habitos)
        elif opcion == "0":
            print("\n¡Hasta la próxima!")
            guardar_datos(habitos, plan_semanal, historial)
            break
        else:
            print("\nOpción no válida.")

        guardar_datos(habitos, plan_semanal, historial)


if __name__ == "__main__":
    menu()
