import streamlit as st
from multipage import save, MultiPage, start_app, clear_cache
import base64
import pandas as pd
import numpy as np

start_app() #Clears the cache when the app is started

app = MultiPage()

app.navbar_name = "Paginas"

st.title('Escuela Sabatica So. St. Paul SDA')

def app1(prev_vars): #First page
    st.subheader('Anuncios de esta semana')

    st.markdown('''
    ***
    >**11/6/2021**

    >### Bienvenidos a la applicación para Escuela Sabatica del Sur de San Pablo
    ''')

    st.markdown('''
    ***
    >**11/7/2021**

    >### 12 de Diciembre Programa de Decimo Tercer Sabado, no faltes
    ''')

    
def app2(prev_vars): #Second page
    st.subheader('IV Trimestre - Lección de la Semana 6')

    # Opening file from file path
    with open("leccion 6.pdf", "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    # Embedding PDF in HTML
        pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
    # Displaying File
        st.markdown(pdf_display, unsafe_allow_html=True)

    # displayPDF("https://rebiblicos.s3.us-east-2.wasabisys.com/Escuela%20Sabatica/4to%202021/Adultos/_6.pdf")

    st.markdown('''
    *** 
    #### Commentarios de la lección
    ''')

    st.text_area('')

def app3(prev_vars): #Third page
    st.subheader('Registro de Estudio')
    st.write('Conteste las siguientes preguntas para llevar conteo de la leccion de esta semana.')
    st.write('Gracias.')
    st.subheader('Nombre')
    st.text_input('',type='default')

    st.subheader('Favor de marcar los dias que "SI" estudio')

    domingo = st.checkbox('Domingo', False)
    lunes = st.checkbox('Lunes', False)
    martes = st.checkbox('Martes', False)
    miercoles = st.checkbox('Miercoles', False)
    jueves = st.checkbox('Jueves', False)
    viernes = st.checkbox('Viernes', False)
    sabado = st.checkbox('Sabado', False)

    days = ['Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado']

    df = pd.DataFrame({'Si/No':np.random.choice(['Si','No'], len(days))})
    # df.index = df.index[:6].tolist() + days

    st.bar_chart(df)

    st.subheader('Llevando estudios biblicos?')
    st.checkbox('Si')
    st.checkbox('No')

def app4(prev_vars):
    st.subheader('Pedidos de Oración')

app.set_initial_page(app1)
app.add_app("Anuncios", app1) #Adds first page (app1) to the framework
app.add_app("Leccion", app2) #Adds second page (app2) to the framework
app.add_app("Registro de Estudio", app3) #Adds third page (app3) to the framework
app.add_app("Pedidos de Oracion", app4)
app.run() #Runs the multipage app!