# Data Voley Information Processing System

Este proyecto procesa datos de partidos de voleibol a partir de archivos de entrada y genera un archivo Excel con la información procesada.
El procesamiento fue diseñado para PDFs salidos de Data Voley en español y portugués dado un archivo tipo.

## Instalación

### 1. Instalación de Python (Si ya lo tienes instalado puedes ir al paso 2)

Si aún no tienes Python instalado, descárgalo e instálalo desde la página oficial:

- [Descargar Python](https://www.python.org/downloads/)

Asegúrate de agregar Python al PATH durante la instalación.

### 2. Creación y activación del entorno virtual

Es recomendable utilizar un entorno virtual para gestionar las dependencias.  
Ejecuta los siguientes comandos:

#### **Windows**

```powershell
python -m venv venv
venv\Scripts\activate
```

#### **Mac/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalación de Dependencias

Ejecuta el siguiente comando para instalar los paquetes necesarios:

```bash
pip install -r requirements.txt
```

## Uso

### 1. Preparar los archivos de entrada

Asegúrate de tener un input.txt con la ruta de los archivos PDF que se procesarán.

### 2. Preprocesamiento

Ejecuta el siguiente comando para correr el script del preprocesamiento.

#### **Windows**

```powershell
python preprocesamiento.py
```

#### **Mac/Linux**

```bash
python3 preprocesamiento.py
```

Esto creará un archivo CSV con las rutas de los PDFs encontrados, en donde se deberá asignar manualmente el nombre tal y como se presenta en el PDF de los equipos.
Por ejemplo:
| Ruta | EQUIPO1 | EQUIPO2 |
|----------|----------|----------|
| pdf\archivos/AA ESPINHO 1 X 3 SL BENFICA.pdf | AA Espinho | SL Benfica |
| pdf\archivos/AJ FONTE BASTARDO 3 X 0 KAIROS.pdf | AJ Fonte Bastardo | Clube Kairós |
| pdf\archivos/ESMORIZ GC 3 X 2 LEIXOES SC.pdf | Esmoriz GC | Leixões SC |

Con esta información el script del procesamiento podrá definir los límites de la información de los equipos.
Una vez llenada la tabla se puede seguir con el paso 3.

### 3. Procesamiento

Ejecuta el siguiente comando para correr el script del procesamiento.

#### **Windows**

```powershell
python procesamiento.py
```

#### **Mac/Linux**

```bash
python3 procesamiento.py
```

Con esto se generó el archivo Datos.xlsx con toda la información para su posterior análisis.

## Feedback y/o Consultas

Contacto: cibraun@miuandes.cl
