import csv

def cargar_estudiantes(ruta_csv):
    estudiantes = []
    with open(ruta_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                nota = float(fila['nota'])
                if 0.0 <= nota <= 5.0:
                    estudiantes.append({'nombre': fila['nombre'], 'nota': nota})
            except ValueError:
                continue  # Ignorar filas con notas no numéricas
    return estudiantes

def mostrar_estudiantes(estudiantes):
    estudiantes_ordenados = sorted(estudiantes, key=lambda x: x['nombre'])
    print(f"{'Nombre':<20} {'Nota':<4}")
    print("-" * 26)
    for est in estudiantes_ordenados:
        print(f"{est['nombre']:<20} {est['nota']:<4.1f}")

def calcular_promedio(estudiantes):
    if not estudiantes:
        return 0.0
    total = sum(est['nota'] for est in estudiantes)
    promedio = total / len(estudiantes)
    return round(promedio, 2)
