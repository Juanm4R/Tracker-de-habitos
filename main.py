#marcar objetivo
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