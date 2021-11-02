import streamlit as st
from multipage import save, MultiPage, start_app, clear_cache
import base64
import pandas as pd
import numpy as np
from datetime import datetime

start_app() #Clears the cache when the app is started

app = MultiPage()

# Side Bar
st.sidebar.image('logo.png')
st.sidebar.write('140 6th Ave N, South St Paul, MN 55075')
st.sidebar.write(' ')
app.navbar_name = "Paginas"

prev_vars = [1,0]


# Pages
def app1(prev_vars): #First page
    st.title('Iglesia Adventista de South St. Paul')
    st.subheader('Anuncios de esta semana')

    st.markdown('''
    ***
    >**11/6/2021**

    >#### Bienvenidos a la pagina de la iglesia Adventista de South St Paul.

    >###### Estamos contentos de que nos visites, en esta sencilla pagina encontraras información y recursos.
    ''')

    st.markdown('''
    ***
    >**11/7/2021**

    >#### 12 de Diciembre Programa de Decimo Tercer Sabado, no faltes
    ''')

    st.markdown('''
    ***
    >**11/7/2021**

    >#### Favor de tener paciencia mientras mejoramos nuestra pagina.

    >###### Estamos trabajando en hacer cada vez mejor nuestra pagina web y estaremos añadiendo mas funcionalidad poco a poco.
    ''')

def app2(prev_vars): #Second page
    st.title('Escuela Sabática')
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
    add_comment = st.button('Agregar')

def app3(prev_vars): #Third page
    st.subheader('Registro de Estudio')
    st.markdown(''' ##### Conteste las siguientes preguntas para llevar conteo de la lección de esta semana, gracias.

    ---

    ''')
    
    st.write(' ')
    st.text_input('Nombre',type='default')

    st.write('Favor de marcar los dias que "SI" estudio')

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

    st.write('Esta llevando estudios biblicos?')
    st.checkbox('Si')
    st.checkbox('No')

def app4(prev_vars):
    st.subheader('Pedidos de Oración')

    date_today = datetime.today().strftime('%m-%d-%Y')
    pedido_date = st.write('Fecha:', date_today)
    pedido_post = st.text_area('Escriba su pedido abajo')
    add_pedido = st.button('Agregar')
    

# app.set_initial_page(app1)
app.add_app("Pagina Principal", app1) #Adds first page (app1) to the framework
app.add_app("Escuela Sabatica", app2) #Adds second page (app2) to the framework
app.add_app("Registro de Estudio", app3) #Adds third page (app3) to the framework
app.add_app("Pedidos de Oración", app4)
app.run() #Runs the multipage app!