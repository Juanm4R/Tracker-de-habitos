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
