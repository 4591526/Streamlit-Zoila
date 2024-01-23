import streamlit as st  #Importamos Streamlit: esta biblioteca de Python facilita la creación y visualización de páginas web interactivas 
import pandas as pd  #Importamos Pandas: esta biblioteca sirve para el análisis de datos tabulados en Python
import csv  #Este comando sirve para leer y escribir archivos CSV 
import json  #Este comando proporciona funciones para trabajar con datos en formato JSON (formato fácil de leer y escribir para humanos, y fácil de analizar y generar para máquinas)

# Con formato de Markdown centramos y agrandamos la letra del título de la web en streamlit
st.markdown("<h1 style='text-align: center; color: purple;'>Álbum personal de Zoila Aurora Cáceres</h1>", unsafe_allow_html=True)

# Nombramos al archivo de la imagen de Zoila y Team Zoila
imagen_zoila = "ZOILA.png"
imagen_team_zoila = "Team Zoila.JPG"

texto = """
Zoila Aurora Cáceres fue una destacada escritora, política y activista 
del feminismo en Perú. Como fundadora del Centro Social de Mujeres, 
dedicó su vida a luchar incansablemente por mejorar las condiciones 
laborales de las mujeres y por el sufragio femenino. Durante los años 
1890 a 1920, Zoila recolectó una gran variedad de materiales como 
cartas, recortes periodísticos, fotografías y artículos, que compiló 
en su álbum personal. Este tesoro documental, que refleja su 
compromiso y su lucha, fue digitalizado por la Biblioteca Central 
de la PUCP, lo que ha permitido su preservación y acceso. Desde 
el Laboratorio de Humanidades Digitales, se lanzó la iniciativa de 
crear una base de datos a partir del álbum personal de Zoila Cáceres. 
Esta base de datos no solo preserva su legado, sino que también 
se convierte en una rica fuente de información que puede 
ser utilizada en diversos campos, incluyendo la programación. 
Este proyecto representa un puente entre la historia y la tecnología, 
ofreciendo una nueva perspectiva sobre la vida y obra de una de 
las figuras más influyentes en la lucha feminista de Perú.
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

# Utilizamos Markdown para aplicar la tipografía
#texto_con_tipografia = f'<span style="font-family: {tipografia};">{texto}</span>'
#st.markdown(texto_con_tipografia, unsafe_allow_html=True)

# Mostramos la imagen de Zoila
st.image(imagen_zoila, caption="Zoila Cáceres", use_column_width=True)

# Obtenemos el nombre del archivo subido
file_name = "C:\\Users\\aml\\Desktop\\proyecto\\Dataset_ZAC.csv"

# Leemos el DataFrame de la base de datos de Zoila
df_zoila = pd.read_csv("Dataset_ZAC.csv")  

def buscar_item(keyword, dataframe):
    resultado = dataframe[dataframe.apply(lambda row: keyword.lower() in ' '.join(row.astype(str)).lower(), axis=1)]
    return resultado if not resultado.empty else None

palabra_clave = st.text_input("Ingrese la palabra que desea buscar:")

if palabra_clave:
    resultados = buscar_item(palabra_clave, df_zoila)
    if resultados is not None:
        st.write(resultados)
    else:
        st.write(f"No se encontraron resultados para la palabra: {palabra_clave}")


# Mostramos la imagen del Team del proyecto de Zoila
st.image(imagen_team_zoila, caption="Equipo del Proyecto de Zoila - HLAB", use_column_width=True)