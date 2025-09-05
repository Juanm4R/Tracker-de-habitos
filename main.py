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

if __name__ == "__main__":
    menu()

