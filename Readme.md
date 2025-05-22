# 🧾 Proyecto Integrador Avanzado – Nivel 2
Nombre del proyecto: Gestor de Tiempo Personal Diario

🎯 Objetivo:
Crear un programa que permita al usuario registrar distintas actividades del día, clasificarlas por tipo (productiva, descanso o distracción), calcular cuánto tiempo dedicó a cada categoría y generar un resumen con análisis y recomendaciones personalizadas.

📚 Contexto del problema:
Una de las claves para el éxito en estudios, trabajo y vida personal es el uso consciente del tiempo. Este proyecto será una especie de "bitácora digital" que te ayude a identificar cuántas horas del día estás aprovechando... y cuántas estás perdiendo.

📂 Requisitos funcionales:
🧩 1. Entrada de datos dinámica:
El programa debe permitir ingresar n actividades del día, una por una:
- Nombre de la actividad
- Duración en minutos
- Tipo de actividad (el usuario selecciona entre):
* 1 → Productiva (estudio, trabajo, lectura)
* 2 → Descanso (comida, siesta breve, caminata)
* 3 → Distracción (redes sociales, TV, dormir sin control)

👉 Repite este proceso hasta que el usuario escriba "fin" como nombre de la actividad.

📊 2. Cálculos requeridos:
1. Total de minutos registrados
2. Tiempo y porcentaje por tipo de actividad
3. Tiempo no registrado (opcional si asumimos un día de 24 h o 1440 min)
4. Clasificación del día:
* 🟢 Excelente → Si el tiempo productivo es > 65% y distracción < 15%
* 🟡 Aceptable → Si prozuctivo > 45% y distracción < 30%
* 🔴 Mal gestionado → Si distracción > 30% o productivo < 45%

📋 3. Salida esperada:

======= RESUMEN DE TU DÍA =======
Total de actividades: 6
Tiempo total registrado: 600 min

→ Productivo   : 360 min (60.0%)
→ Descanso     : 90 min (15.0%)
→ Distracción  : 150 min (25.0%)

Evaluación general del día: ACEPTABLE
Recomendación: Intenta reducir al menos 30 min de distracciones.

🧰 Requisitos técnicos:
- Uso de listas para almacenar nombre, tipo y duración de actividades.
- Uso de condicionales para clasificación.
- Uso de conversión de tipos, input(), float/int(), validaciones simples.
- Uso de f-strings, sangría PEP8 y comentarios.
- Control de flujo con while.

🚀 Extras si te atreves (opcional):
1. Validación: si la duración ingresada no es numérica, muestra error y vuelve a pedirla.
2. Mostrar la actividad más larga registrada y a qué tipo pertenece.
3. Permitir guardar los datos del día en un archivo .txt.

