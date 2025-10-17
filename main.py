import matplotlib.pyplot as plt

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
