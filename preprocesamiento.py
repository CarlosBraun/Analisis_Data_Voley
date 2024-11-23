import os
import pandas as pd

# Ruta de la carpeta donde están los PDFs
carpeta = "./FECHA1"

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
