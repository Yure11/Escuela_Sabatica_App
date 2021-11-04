from typing import Container
import streamlit as st
from multipage import save, MultiPage, start_app, clear_cache
import base64
import pandas as pd
import numpy as np
from datetime import datetime
import streamlit.components.v1 as components


# Data Base
import sqlite3
conn = sqlite3.connect('data.bd')
c = conn.cursor()

#Functions
def create_pedidos_table():
    c.execute('CREATE TABLE IF NOT EXISTS pedidostable(date DATE, pedido TEXT)')

def create_anuncios_table():
    c.execute('CREATE TABLE IF NOT EXISTS anunciostable(title Text, anuncio TEXT, date DATE)')

def add_pedidos_data(date, pedido):
    c.execute('INSERT INTO pedidostable(date, pedido) VALUES (?,?)', (date, pedido))
    conn.commit()

def add_anuncios_data(title, anuncio, date):
    c.execute('INSERT INTO anunciostable(title, anuncio, date) VALUES (?,?,?)', (title, anuncio, date))
    conn.commit()

def view_all_pedidos():
    c.execute('SELECT * FROM pedidostable')
    data = c.fetchall()
    return data

def view_all_anuncios():
    c.execute('SELECT * FROM anunciostable')
    data = c.fetchall()
    return data

# Layout Templates
anuncios_temp = """
<div style="background-color:#1f90ff;padding:10px;border-radius:10px;margin:10px;">
<h4 style="color:white;text-align:center;">{}</h1>
<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;" >
<h6> <br/> {}</h6>
<p style="color:gray;text-align:right;">{}</p>
</div>
"""

pedido_temp = '''
<div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
<h4 style="color:white;text-align:left;>{}</h1>
<img src="https://drive.google.com/uc?id=1rWl-c1vVxyRZHx0mpOEloaV6kRdR9xBT.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;">
<h6 style="color:white;">{}</h6>
<p style="color:gray;text-align:right"></p>
</div>
'''

start_app() #Clears the cache when the app is started

app = MultiPage()

# Side Bar
# st.sidebar.image('SSP Logo.png', width=150)
sidebar_logo = """
<p style="text-align:center;"><img src="https://drive.google.com/uc?id=1-z7Qusop31zf-E-UzTHMndxYRhezUAqB" alt="Logo" width="150"></p>
<p style="text-align:center;">
<a href="https://www.google.com/maps/place/140+6th+Ave+N,+South+St+Paul,+MN+55075/@44.8964291,-93.0577413,14.75z/data=!4m5!3m4!1s0x87f7d473b1b1f4fd:0x5ceaab1845d7cd9a!8m2!3d44.8917517!4d-93.0406702" target="_blank">140 6th Ave N, South St Paul, MN 55075</a><br>
<a href="https://www.facebook.com/sspsda" target="_blank">Siguenos en Facebook</a><br>
<a href="https://www.youtube.com/c/SouthStPaulSDA" target="_blank">Miranos en Youtube</a>
</p>
"""
st.sidebar.markdown(sidebar_logo, unsafe_allow_html=True)
st.sidebar.write(' ')
app.navbar_name = "Paginas"

prev_vars = [1,0]


# Pages
def main(prev_vars): #First page

    page_title = '''
    <H1 style="font-family:Candara; color:#0000A5;">Iglesia Adventista de South St. Paul</h1>
    '''
    
    st.markdown(page_title, unsafe_allow_html=True)
    
    create_anuncios_table()
    anuncios = view_all_anuncios()
    for i in anuncios:
        a_title = i[0]
        a_post = i[1]
        a_date = i[2]
        st.markdown(anuncios_temp.format(a_title, a_post, a_date), unsafe_allow_html=True)

    date_today = datetime.today().strftime('%m/%d/%Y')

    welcome_message = '''
    <div style="background-color:#1f90ff;padding:10px;border-radius:10px;margin:10px;">
    <h4 style="color:white;text-align:center;">Bienvenidos</h1>
    <img src="https://drive.google.com/uc?id=1-z7Qusop31zf-E-UzTHMndxYRhezUAqB" alt="Avatar" style="vertical-align:middle;float:left;width: 50px;border-radius: 10%;" >
    <h6> <br/>Esta es nuestra pagina de la Iglesia Adventista del Sur de San Pablo</h6>
    <p style="color:gray;text-align:right;">11/3/2021</p>
    </div>'''
    st.markdown(welcome_message, unsafe_allow_html=True)
    st.subheader('Anuncios de esta semana')
    st.markdown('''

    ---
    ##### Escriba su anuncio abajo y presione el boton para agregar a la lista
    ''')
    anuncio_title = st.text_input('Titulo del Anuncio')
    anuncio_post = st.text_area('Anuncio')
    
    if st.button('Agregar'):
        add_anuncios_data(anuncio_title, anuncio_post, date_today)
        st.success("Anuncio:{} agregado".format(date_today))



def lesson(prev_vars): #Second page
    st.title('Escuela Sabática')
    st.subheader('IV Trimestre - Lección de la Semana 6')

    # Opening file from file path
    with open("leccion.pdf", "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    # Embedding PDF in HTML
        pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
    # Displaying File
        st.markdown(pdf_display, unsafe_allow_html=True)

    # displayPDF("https://drive.google.com/uc?id=1GsjBovR4OrzPvtGBjxjX9hpvgG-j2MBq")

    st.markdown('''
    *** 
    #### Comentarios de la lección
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

def prayer(prev_vars):
    st.subheader('Pedidos de Oración')
    create_pedidos_table()
    pedidos = view_all_pedidos()
    for i in pedidos:
        p_post = i[1]
        p_date = i[0]
        st.markdown(pedido_temp.format(p_post, p_date), unsafe_allow_html=True)

    date_today = datetime.today().strftime('%m/%d/%Y')
    st.markdown('''
    ---

    ##### Escriba su pedido abajo y presione el boton para agregar a la lista
    ''')
    pedido_post = st.text_area('')
    if st.button('Agregar'):
        add_pedidos_data(date_today, pedido_post)
        st.success("Pedido:{} agregado".format(date_today))

def admin(prev_vars):

    inputs = st.empty()
    with inputs.container():
        st.subheader('Log In')
        st.write('Solo para administradores de la pagina')
        username = st.text_input("Please input your username:")
        passwd = st.text_input("Please input your password",type='password')

    if username == st.secrets["DB_USERNAME"] and passwd == st.secrets["DB_PASSWORD"]:
            inputs.empty()
            st.subheader('Admin Settings')
            st.success("Welcome back！")
            st.markdown("""
            ---

            #### Anuncios
            """)
            st.markdown("""
            ---
            
            #### Comentarios de la lección
            """)
            st.markdown("""
            ---

            #### Pedidos
            """)
    else:
        st.info("Username and/or password are incorrect")


# app.set_initial_page(app1)
app.add_app("Pagina Principal", main) #Adds first page (app1) to the framework
app.add_app("Escuela Sabatica", lesson) #Adds second page (app2) to the framework
app.add_app("Registro de Estudio", app3) #Adds third page (app3) to the framework
app.add_app("Pedidos de Oración", prayer)
app.add_app("Admin", admin)
app.run() #Runs the multipage app!
