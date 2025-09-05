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

if __name__ == "__main__":
    menu()