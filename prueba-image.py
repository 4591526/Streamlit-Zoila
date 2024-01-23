import streamlit as st  #Importamos Streamlit: esta biblioteca de Python facilita la creación y visualización de páginas web interactivas 
import pandas as pd  #Importamos Pandas: esta biblioteca sirve para el análisis de datos tabulados en Python
import csv  #Este comando sirve para leer y escribir archivos CSV 
import json  #Este comando proporciona funciones para trabajar con datos en formato JSON (formato fácil de leer y escribir para humanos, y fácil de analizar y generar para máquinas)
import os #Esta biblioteca proporciona una interfaz para interactuar con el sistema operativo (manipulación de rutas, la creación y eliminación de directorios, y la obtención de información sobre archivos)
from PIL import Image #Es una clase dentro de la biblioteca Pillow que proporciona funcionalidades para trabajar con imágenes

# Con formato de Markdown centramos y agrandamos la letra del título de la web en streamlit
st.markdown("<h1 style='text-align: center; color: purple;'>Álbum personal de Zoila Aurora Cáceres</h1>", unsafe_allow_html=True)

# Nombramos al archivo de la imagen de Zoila y Team Zoila
imagen_zoila = "ZOILA.png"
imagen_team_zoila = "Team Zoila.JPG"
# Definimos la ruta de la carpeta donde se encuentran las imágenes de la base de datos de Zoila
##folder_zoila = "C:\\Users\\u_humanidades\\Desktop\\proyecto\\ID-Item" (ruta lab)
folder_zoila = "C:\\Users\\aml\\Desktop\\proyecto\\ID-Item"


def load_images_and_rgb(folder_path):
    images_data = []  # Almacenará información sobre cada imagen
    rgb_data = []     # Almacenará los rasgos RGB de cada imagen

    for filename in os.listdir(folder_path):
        if filename.endswith(('.JPG', '.jpeg', '.PNG')):
            file_path = os.path.join(folder_path, filename)
            img = Image.open(file_path)

            # Obtener el ID-Item (nombre del archivo sin extensión)
            id_item = os.path.splitext(filename)[0]

            # Agregar información al DataFrame de imágenes
            images_data.append({'ID-Item': id_item, 'image': img})

            # Obtener los rasgos RGB de la imagen
            rgb_values = list(img.getdata())
            rgb_data.append({'ID-Item': id_item, 'RGB': rgb_values})

    # Crear DataFrames
    images_df = pd.DataFrame(images_data)
    rgb_df = pd.DataFrame(rgb_data)

    # Establecer el ID-Item como índice en el DataFrame de imágenes
    images_df.set_index('ID-Item', inplace=True)
    rgb_df.set_index('ID-Item', inplace=True)

    return images_df, rgb_df

def open_image(images_df, id_item):
    """
    Abre la imagen correspondiente al ID-Item especificado.
    """
    if id_item in images_df.index:
        img = images_df.loc[id_item, 'image']
        st.image(img, caption=f"ID-Item: {id_item}", use_column_width=True)
    else:
        st.warning(f"No se encontró la imagen para el ID-Item: {id_item}")

# Llamar a la función para cargar imágenes y rasgos RGB
images_df, rgb_df = load_images_and_rgb(folder_zoila)

# Añadir un widget de búsqueda en Streamlit
search_query = st.text_input("Buscar por ID-Item:")

# Filtrar el DataFrame por ID-Item
filtered_images_df = images_df[images_df.index.str.contains(search_query, case=False, na=False)]

# Mostrar los resultados
if not filtered_images_df.empty:
    # Mostrar imágenes correspondientes al resultado de la búsqueda
    for index, row in filtered_images_df.iterrows():
        st.image(row['image'], caption=f"ID-Item: {index}", use_column_width=True)
else:
    st.warning("No se encontraron resultados para la búsqueda.")