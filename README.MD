# Visualizador de Datos CSV

Esta aplicación web permite a los usuarios cargar archivos CSV y visualizar los datos mediante gráficos interactivos generados con Chart.js. La aplicación está construida con Flask para el backend y utiliza tecnologías web modernas para el frontend.

## Características

- Carga de archivos CSV mediante arrastrar y soltar o selección de archivo
- Visualización de estadísticas descriptivas básicas de los datos
- Generación de gráficos interactivos (barras, líneas, circular, dispersión)
- Personalización de ejes X e Y para los gráficos
- Vista previa de los datos en formato de tabla
- Interfaz de usuario intuitiva y responsive

## Requisitos

- Python 3.7+
- Flask
- Pandas
- Bootstrap 5 (incluido vía CDN)
- Chart.js (incluido vía CDN)
- PapaParse (incluido vía CDN)

## Instalación

1. Clona este repositorio o descarga los archivos

2. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   ```

3. Activa el entorno virtual:
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Instala los paquetes requeridos:
   ```bash
   pip install flask pandas
   ```

5. Estructura de directorios:
   ```
   visualizador-csv/
   ├── app.py
   ├── uploads/  (se crea automáticamente)
   └── templates/
       └── index.html
   ```

## Uso

1. Ejecuta la aplicación:
   ```bash
   python app.py
   ```

2. Abre tu navegador y visita `http://127.0.0.1:5000/`

3. Carga un archivo CSV arrastrándolo al área designada o haciendo clic para seleccionarlo

4. Explora tus datos a través de las estadísticas, gráficos y tablas proporcionados

## Funcionamiento

### Backend (Flask)

La aplicación Flask maneja la carga de archivos CSV, los procesa utilizando Pandas y devuelve la información estructurada al frontend. Funciones principales:

- Ruta principal (`/`): Renderiza la plantilla HTML
- Ruta de carga (`/upload`): Procesa el archivo CSV y devuelve estadísticas y datos procesados

### Frontend

El frontend utiliza JavaScript para manejar la interacción del usuario, la carga de archivos y la visualización de datos:

- Interfaz de carga de archivos con funcionalidad de arrastrar y soltar
- Visualización de estadísticas descriptivas
- Gráficos interactivos con Chart.js
- Tabla de datos para vista previa

