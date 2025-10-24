###EDITAR HÁBITO####

def editar_habito():
    if not habitos:
        print("No hay hábitos para editar.")
        return
    for i, (nombre, progreso) in enumerate(habitos, start=1):
        print(i, "-", nombre)
    try:
        indice = int(input("Ingrese el número del hábito a editar: ")) - 1
        if indice < 0 or indice >= len(habitos):
            print("Número inválido.")
            return
        nuevo_nombre = input("Ingrese el nuevo nombre del hábito: ").strip()
        if nuevo_nombre == "":
            print("El nombre no puede estar vacío.")
            return
        anterior = habitos[indice][0]
        habitos[indice][0] = nuevo_nombre
        print("Hábito editado:", anterior, "→", nuevo_nombre)
    except ValueError:
        print("Debe ingresar un número válido.")
