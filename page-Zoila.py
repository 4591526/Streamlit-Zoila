import streamlit as st  #Importamos Streamlit: esta biblioteca de Python facilita la creación y visualización de páginas web interactivas 
import pandas as pd  #Importamos Pandas: esta biblioteca sirve para el análisis de datos tabulados en Python
import csv  #Este comando sirve para leer y escribir archivos CSV 
import json  #Este comando proporciona funciones para trabajar con datos en formato JSON (formato fácil de leer y escribir para humanos, y fácil de analizar y generar para máquinas)
import os #Esta biblioteca proporciona una interfaz para interactuar con el sistema operativo (manipulación de rutas, la creación y eliminación de directorios, y la obtención de información sobre archivos)
from PIL import Image #Es una clase dentro de la biblioteca Pillow que proporciona funcionalidades para trabajar con imágenes

# Con formato de Markdown centramos y agrandamos la letra del título de la web en streamlit
st.markdown("<h1 style='text-align: center;'>Álbum personal de Zoila Aurora Cáceres</h1>", unsafe_allow_html=True)

# Nombramos al archivo de la imagen de Zoila y Team Zoila
imagen_zoila = "ZOILA.png"
imagen_team_zoila = "Team Zoila.JPG"

# Definimos la ruta de la carpeta donde se encuentran las imágenes de la base de datos de Zoila
folder_zoila = "ID-Item/"

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
    <div style="font-family: {tipografia}; font-size: 20px; text-align: justify;">
        {texto}
"""

# Mostramos el texto con la tipografía personalizada
st.markdown(estilo_personalizado, unsafe_allow_html=True)

# Mostramos la imagen de Zoila
st.image(imagen_zoila, caption="Zoila Cáceres", use_column_width=True)

# Mostramos la imagen de las chicas superpoderosas
# st.image(imagen_chicas, caption="Grupo Chicas Superpoderosas - HLAB", use_column_width=True)

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

st.subheader("🔎 Buscador de imágenes")
imagen = st.text_input("Ingrese el ID-Item que desea buscar:")
if imagen:
    if imagen == 'ZAC-002-estampilla':
        st.markdown("<a href='https://datos.pucp.edu.pe/file.xhtml?fileId=20676&version=1.0' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif imagen == 'ZAC-005/006-recorte1':
        st.markdown("<a href='https://datos.pucp.edu.pe/file.xhtml?fileId=20624&version=1.0' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    else:
        st.warning("No se encontraron resultados para la búsqueda.")

# Mostramos la imagen del Team del proyecto de Zoila
st.image(imagen_team_zoila, caption="Equipo del Proyecto de Zoila", use_column_width=True)
