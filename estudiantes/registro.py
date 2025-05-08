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
