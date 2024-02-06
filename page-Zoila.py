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
imagen_chicas = "superpoderosas.png"
imagen_team_zoila = "Team Zoila.JPG"

# Definimos la ruta de la carpeta donde se encuentran las imágenes de la base de datos de Zoila
folder_zoila = "proyecto\\ID-Item"

texto = """
Zoila Aurora Cáceres fue una destacada escritora, política y activista del feminismo en Perú. 
Como fundadora del Centro Social de Mujeres, dedicó su vida a luchar incansablemente por mejorar 
las condiciones laborales de las mujeres y por el sufragio femenino. Durante los años 1890 a 1920, 
Zoila recolectó una gran variedad de materiales, como cartas, recortes periodísticos, 
fotografías y artículos, que compiló en su álbum personal. Este tesoro documental, 
reflejo de su compromiso y lucha, fue digitalizado por la Biblioteca Central de la PUCP, 
lo que ha permitido su preservación y acceso.

Desde el Laboratorio de Humanidades Digitales (H-LAB), se lanzó la iniciativa de crear una base 
de datos a partir del álbum personal de Zoila Cáceres. Esta base de datos no solo preserva su legado, 
sino que también se convierte en una rica fuente de información utilizada en diversos campos, 
incluyendo la programación. Este proyecto representa un puente entre la historia y la tecnología, 
ofreciendo una nueva perspectiva sobre la vida y obra de una de las figuras más influyentes en la lucha feminista en Perú.
"""

# Definimos la tipografía deseada ('Courier New')
tipografia = "Arial, sans-serif"

# Definimos el tamaño de la fuente, justificación y color
estilo_personalizado = f"""
    <div style="font-family: {tipografia}; font-size: 20px; text-align: justify; color: purple;">
        {texto}
"""

# Mostramos el texto con la tipografía personalizada
st.markdown(estilo_personalizado, unsafe_allow_html=True)

# Mostramos la imagen de Zoila
st.image(imagen_zoila, caption="Zoila Cáceres", use_column_width=True)

# Mostramos la imagen de las chicas superpoderosas
st.image(imagen_chicas, caption="Grupo Chicas Superpoderosas - HLAB", use_column_width=True)

# Obtenemos el nombre del archivo subido
file_name = "C:\\Users\\aml\\Desktop\\proyecto\\Dataset_ZAC.csv"

# Leemos el DataFrame de la base de datos de Zoila
df_zoila = pd.read_csv("Dataset_ZAC.csv")  
 

def buscar_item(keyword, dataframe):
    resultado = dataframe[dataframe.apply(lambda row: keyword.lower() in ' '.join(row.astype(str)).lower(), axis=1)]
    #imagen = dataframe.loc[image_df, 'ID-Item']
    return resultado if not resultado.empty else None

palabra_clave = st.text_input("Ingrese la palabra que desea buscar:")

if palabra_clave:
    resultados = buscar_item(palabra_clave, df_zoila)
    if resultados is not None:
        st.write(resultados)
    else:
        st.write(f"No se encontraron resultados para la palabra: {palabra_clave}")

def load_images_and_rgb(folder_path):
    images_data = []
    rgb_data = []

    for filename in os.listdir(folder_path):
        if filename.endswith(('.JPG', '.jpeg', '.PNG')):
            file_path = os.path.join(folder_path, filename)
            img = Image.open(file_path)

            id_item = os.path.splitext(filename)[0]

            images_data.append({'ID-Item': id_item, 'image': img})
            rgb_values = list(img.getdata())
            rgb_data.append({'ID-Item': id_item, 'RGB': rgb_values})

    images_df = pd.DataFrame(images_data)
    rgb_df = pd.DataFrame(rgb_data)

    images_df.set_index('ID-Item', inplace=True)
    rgb_df.set_index('ID-Item', inplace=True)

    return images_df, rgb_df

def open_image(images_df, id_item):
    if id_item in images_df.index:
        img = images_df.loc[id_item, 'image']
        st.image(img, caption=f"ID-Item: {id_item}", use_column_width=True)
    else:
        st.warning(f"No se encontró la imagen para el ID-Item: {id_item}")

# Llamar a la función para cargar imágenes y rasgos RGB
images_df, rgb_df = load_images_and_rgb(folder_zoila)

# Añadir un widget de búsqueda en Streamlit
search_query = st.text_input("Buscar la imagen que deseas según el ID-Item:")

# Verificar si se ha ingresado una consulta de búsqueda
if search_query:
    # Filtrar el DataFrame por ID-Item
    filtered_images_df = images_df[images_df.index.str.contains(search_query, case=False, na=False)]

    # Mostrar los resultados
    if not filtered_images_df.empty:
        # Mostrar imágenes correspondientes al resultado de la búsqueda
        for index, row in filtered_images_df.iterrows():
            open_image(images_df, index)
    else:
        st.warning("No se encontraron resultados para la búsqueda.")

# Mostramos la imagen del Team del proyecto de Zoila
st.image(imagen_team_zoila, caption="Equipo del Proyecto de Zoila", use_column_width=True)
