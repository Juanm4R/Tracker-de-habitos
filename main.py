def mostrar_habitos():
    if not habitos:
        print("No hay hábitos cargados.")
        return False
    print("Lista de Hábitos")
    for i, (nombre, progreso) in enumerate(habitos, 1):
        cumplidos = sum(progreso)
        print(i, ".", nombre, "- Cumplidos:", cumplidos, "/", len(progreso))
    return True


#----- Nuevo codigo -------
def calcular_racha(progreso):
    racha_maxima = 0
    temp_max = 0
    for dia in progreso:
        if dia == 1:
            temp_max += 1
            if temp_max > racha_maxima:
                racha_maxima = temp_max
        else:
            temp_max = 0
    
    racha_actual = 0
    for dia in reversed(progreso):
        if dia == 1:
            racha_actual += 1
        else:
            break
            
    return racha_actual, racha_maxima

def mostrar_habitos(solo_nombres=False):
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
            total_semanal = len(progreso_semanal)
            
            print(i, ".", nombre, 
                  "- Cumplidos:", cumplidos, "/", len(progreso), 
                  "Racha Actual:", racha_actual, 
                  "Racha Máxima:", racha_maxima,
                  "Últimos 7 Días:", cumplidos_semanales, "/", total_semanal)
    return True