import os
import pandas as pd


nombre_archivo = "input.txt"

try:
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no fue encontrado en la carpeta del script.")
except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {e}")

carpeta = "./"+contenido

# Listar solo los archivos PDF y construir las rutas completas
pdfs = [carpeta.replace("./", "") + "/" + archivo for archivo in os.listdir(carpeta) if archivo.endswith(".pdf")]

# Crear un DataFrame con las columnas requeridas
data = {
    "RUTA": pdfs,
    "EQUIPO1": [""] * len(pdfs),  # Inicialmente vacío
    "EQUIPO2": [""] * len(pdfs)   # Inicialmente vacío
}

df = pd.DataFrame(data)
# Guardar el DataFrame en un archivo CSV separado por ';'
nombre_archivo = carpeta.replace("./","").lower()+"_pdfs.csv"
df.to_csv(nombre_archivo, sep=';', index=False, encoding='utf-8')

print(f"Archivo CSV '{nombre_archivo}' creado con éxito.")
nombre_txt = "ruta_csv.txt"
try:
    with open(nombre_txt, "w", encoding="utf-8") as archivo_txt:
        archivo_txt.write(nombre_archivo)
        print(f"Archivo TXT con la ruta del CSV creado: {nombre_txt}")
except Exception as e:
    print(f"Ocurrió un error al guardar la ruta en el archivo TXT: {e}")