nombre_actividad = []
duracion_actividad = []
tipo_actividad = []

print("=== RESUMEN DE TU DÍA ===")
print("Escribe 'fin' como nombre para terminar.\n")

while True:
    nombre = input("Nombre de la actividad: ")
    if nombre.lower() == "fin":
        break
    
    while True:
        try:
            duracion = int(input("Duración de la actividad (en minutos): "))
            break
        except ValueError:
            print("Por favor, ingresa un número válido.")

    while True:
        print("Tipo de actividad: 1) Productiva  2) Descanso  3) Distracción")
        tipo_opcion = input("Elige la tipo de actividad (1, 2 o 3): ")
        if tipo_opcion == "1":
            tipo = "Productiva"
            break
        elif tipo_opcion == "2":
            tipo = "Descanso"
            break
        elif tipo_opcion == "3":
            tipo = "Distracción"
            break
        else:
            print("Tipo de actividad no válido, vuelve a intentarlo.")

    nombre_actividad.append(nombre)
    duracion_actividad.append(duracion)
    tipo_actividad.append(tipo)
    print("Actividad registrada.\n")

# Cálculos
total_actividades = len(nombre_actividad)
total_actividades_productivas = len([t for t in tipo_actividad if t == "Productiva"])
total_actividades_descansos = len([t for t in tipo_actividad if t == "Descanso"])
total_actividades_distracciones = len([t for t in tipo_actividad if t == "Distracción"])
        
# Suma los minutos de cada tipo
min_productiva = sum(duracion_actividad[i] for i in range(len(duracion_actividad)) if tipo_actividad[i] == "Productiva")
min_descanso = sum(duracion_actividad[i] for i in range(len(duracion_actividad)) if tipo_actividad[i] == "Descanso")
min_distraccion = sum(duracion_actividad[i] for i in range(len(duracion_actividad)) if tipo_actividad[i] == "Distracción")

total_minutos = sum(duracion_actividad)

def porcentaje(parte, total):
    return (parte / total * 100) if total > 0 else 0

print("\n======= RESUMEN DE ACTIVIDADES =======")
print(f"Total de actividades registradas: {total_actividades}")
print(f"\nTotal de minutos registrados: {total_minutos}")
print(f"Total de actividades de tipo 'Productiva': {total_actividades_productivas}")
print(f"Total de actividades de tipo 'Descanso': {total_actividades_descansos}")
print(f"Total de actividades de tipo 'Distracción': {total_actividades_distracciones}")
print(f"\n→ Productiva   : {min_productiva} min ({porcentaje(min_productiva, total_minutos):.1f}%)")
print(f"→ Descanso     : {min_descanso} min ({porcentaje(min_descanso, total_minutos):.1f}%)")
print(f"→ Distracción  : {min_distraccion} min ({porcentaje(min_distraccion, total_minutos):.1f}%)")

# Clasificación simple
if porcentaje(min_productiva, total_minutos) > 65 and porcentaje(min_distraccion, total_minutos) < 15:
    print("\nEvaluación general del día: Excelente")
    print("Sigue así, ¡muy buen trabajo!")
elif porcentaje(min_productiva, total_minutos) > 45 and porcentaje(min_distraccion, total_minutos) < 30:
    print("\nEvaluación general del día: Aceptable")
    print("Recomendación: Intenta reducir al menos 30 min de distracciones.")
else:
    print("\nEvaluación general del día: Mal gestionado")
    print("Recomendación: Intenta reducir más tu tiempo en distracciones.")