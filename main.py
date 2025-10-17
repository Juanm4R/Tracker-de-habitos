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

plan_semanal = []  
DIAS = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

def agregar_actividad():
    print("\n--- Agregar Actividad ---")
    print("Días disponibles: ")
    for d in DIAS:
        print("-", d)

    dia = input("Ingrese el día: ").capitalize()
    if dia not in DIAS:
        print(" Día INVALIDO.")
        return

    hora = input("Ingrese la hora (HH:MM): ")
    actividad = input("Ingrese la actividad: ")

    plan_semanal.append([dia, hora, actividad])
    print(f"✅ Actividad '{actividad}' agregada para {dia} a las {hora}.")

def mostrar_plan_organizado():
    if not plan_semanal:
        print("No hay actividades cargadas.")
        return

    actividades_ordenadas = plan_semanal[:]
    n = len(actividades_ordenadas)

    for i in range(n):
        for j in range(0, n - i - 1):
            d1, h1, _ = actividades_ordenadas[j]
            d2, h2, _ = actividades_ordenadas[j+1]

            if DIAS.index(d1) > DIAS.index(d2):
                actividades_ordenadas[j], actividades_ordenadas[j+1] = actividades_ordenadas[j+1], actividades_ordenadas[j]
            elif d1 == d2 and h1 > h2:
                actividades_ordenadas[j], actividades_ordenadas[j+1] = actividades_ordenadas[j+1], actividades_ordenadas[j]

    print("\n--- PLAN SEMANAL ORGANIZADO ---")
    for dia, hora, act in actividades_ordenadas:
        print(f"{dia} {hora} → {act}")