from typing import Container
import streamlit as st
from multipage import save, MultiPage, start_app, clear_cache
import base64
import pandas as pd
import numpy as np
from datetime import datetime
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')



# Data Base
import sqlite3
conn = sqlite3.connect('data/posts.sqlite')
c = conn.cursor()

# Functions for anuncios
def create_anuncios_table():
    c.execute('CREATE TABLE IF NOT EXISTS anunciostable(Titulo TEXT, Anuncio TEXT, Fecha DATE)')

def add_anuncios_data(titulo, anuncio, fecha):
    c.execute('INSERT INTO anunciostable(Titulo, Anuncio, Fecha) VALUES (?,?,?)', (titulo, anuncio, fecha))
    conn.commit()

def view_all_anuncios():
    c.execute('SELECT * FROM anunciostable')
    data = c.fetchall()
    return data

def delete_anuncio(title):
    c.execute('DELETE FROM anunciostable WHERE Titulo="{}"'.format(title))
    conn.commit()

# Functions for pedidos
def create_pedidos_table():
    c.execute('CREATE TABLE IF NOT EXISTS pedidostable(Pedido TEXT, Fecha DATE)')

def add_pedidos_data(pedido, fecha):
    c.execute('INSERT INTO pedidostable(Pedido, Fecha) VALUES (?,?)', (pedido, fecha))
    conn.commit()

def view_all_pedidos():
    c.execute('SELECT * FROM pedidostable')
    data = c.fetchall()
    return data

def delete_pedido(title):
    c.execute('DELETE FROM pedidostable WHERE Pedido="{}"'.format(title))
    conn.commit()

# Functions for lesson comments
def create_comentarios_table():
    c.execute('CREATE TABLE IF NOT EXISTS comentariostable(Comentario TEXT, Fecha DATE)')

def add_comentarios_data(comentario, fecha):
    c.execute('INSERT INTO comentariostable(Comentario, Fecha) VALUES (?,?)', (comentario, fecha))
    conn.commit()

def view_all_comentarios():
    c.execute('SELECT * FROM comentariostable')
    data = c.fetchall()
    return data

def delete_comentario(title):
    c.execute('DELETE FROM comentariostable WHERE Titulo="{}"'.format(title))
    conn.commit()



# Layout Templates
anuncios_temp = """
<div style="background-color:#820A42;padding:10px;border-radius:10px;margin:10px;">
<h4 style="color:white;text-align:center;">{}</h1>
<img src="https://drive.google.com/uc?id=1AAy1qyWiktxXBDJmxjL0Qr37KhkEfA2v" alt="Avatar" style="vertical-align: middle;float:left;width:60px;border-radius:10%;" >
<h6 style="color:white;"> <br/> {}</h6>
<p style="color:white;text-align:right;">{}</p>
</div>
"""

pedidos_temp = '''
<div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
<img src="https://drive.google.com/uc?id=1c63h7YK6QbA5bwXI4tzwLy_LzC1nfJrw" alt="Avatar" style="vertical-align:bottom;float:right;width:50px;border-radius:10%;">
<br>
<h6 style="color:white;text-align:center">{}</h6>
<p style="color:white;text-align:right">{}</p>
</div>
'''

comentarios_temp = '''
<div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
<img src="https://drive.google.com/uc?id=1ZcojuObJQWizMzaI1DV0S04I12x_7RiN" alt="Avatar" style="vertical-align:bottom;float:right;width:50px;border-radius:10%;">
<br>
<h6 style="color:white;text-align:center">{}</h6>
<p style="color:white;text-align:right">{}</p>
</div>
'''

start_app() #Clears the cache when the app is started

app = MultiPage()

# Side Bar

sidebar_logo = """
<p style="text-align:center;"><img src="https://drive.google.com/uc?id=1-z7Qusop31zf-E-UzTHMndxYRhezUAqB" alt="SSPSDA" width="150"></p>
<p style="text-align:center;">
<br>
<a href="https://www.google.com/maps/place/140+6th+Ave+N,+South+St+Paul,+MN+55075/@44.8964291,-93.0577413,14.75z/data=!4m5!3m4!1s0x87f7d473b1b1f4fd:0x5ceaab1845d7cd9a!8m2!3d44.8917517!4d-93.0406702" target="_blank">140 6th Ave N, South St Paul, MN 55075</a><br>
<br>
<a href="https://www.facebook.com/sspsda" target="_blank">Siguenos en Facebook</a><img src="https://drive.google.com/uc?id=1Y4r-9fyMWAg2RBaoWkiVTSJY6ek0bVr6" alt="facebook" width="50">
<br>
<a href="https://www.youtube.com/c/SouthStPaulSDA" target="_blank">Miranos en Youtube</a><img src="https://drive.google.com/uc?id=1Jrjakn3WhICMrC_Xf_Qo32dH6WcFqxDB" alt="facebook" width="43">
</p>
"""
st.sidebar.markdown(sidebar_logo, unsafe_allow_html=True)
st.sidebar.write(' ')
app.navbar_name = "Paginas"

prev_vars = [1,0]


# Pages

def main(prev_vars): #First page

    page_title = '''
    <h1 style="font-family:Candara; color:#0000A5;text-align:center;">Iglesia Adventista de South St. Paul</h1>
    <br>
    <br>
    '''
    
    st.markdown(page_title, unsafe_allow_html=True)

    welcome_message = '''
    <div style="background-color:#1f90ff;padding:10px;border-radius:10px;margin:10px;">
    <h4 style="color:white;text-align:center;">Bienvenidos</h1>
    <img src="https://drive.google.com/uc?id=1-z7Qusop31zf-E-UzTHMndxYRhezUAqB" alt="Avatar" style="vertical-align:middle;float:left;width: 50px;border-radius: 10%;" >
    <h6> <br/>Esta es nuestra pagina de la Iglesia Adventista del Sur de San Pablo</h6>
    <p style="color:gray;text-align:right;"> </p>
    </div>'''
    st.markdown(welcome_message, unsafe_allow_html=True)
    
    st.markdown("""
    ---
    <h3 style="text-align:center;">Anuncios del Mes</h1>""", unsafe_allow_html=True)

    create_anuncios_table()
    anuncios = view_all_anuncios()
    for i in anuncios:
        a_title = i[0]
        a_post = i[1]
        a_date = i[2]
        st.markdown(anuncios_temp.format(a_title, a_post, a_date), unsafe_allow_html=True)

      



def lesson(prev_vars): #Second page
    st.title('Escuela Sabática')
    st.subheader('IV Trimestre - Lección de la Semana 6')

    # Opening file from file path
    with open("leccion.pdf", "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    # Embedding PDF in HTML
        pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
    # Displaying File
        st.markdown(pdf_display, unsafe_allow_html=True)

    # displayPDF("https://drive.google.com/uc?id=1GsjBovR4OrzPvtGBjxjX9hpvgG-j2MBq")

    st.markdown('''
    *** 
    #### Comentarios de la lección
    ''')

    create_comentarios_table()
    comentarios = view_all_comentarios()
    for i in comentarios:
        c_post = i[0]
        c_date = i[1]
        st.markdown(comentarios_temp.format(c_post, c_date), unsafe_allow_html=True)

    st.markdown('''
    ---

    ###### Abajo puede escribir su comentario u opinion acerca de la lección de esta semana y presione el boton de "Agregar"
    ''')
    date_today = datetime.today().strftime('%m/%d/%Y')
    comentario_post = st.text_area('')
    if st.button('Agregar'):
        add_comentarios_data(comentario_post, date_today)
        st.success("Comentario agregado {}".format(date_today))

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

def prayer(prev_vars): # Fourth Page
    st.subheader('Pedidos de Oración')
    create_pedidos_table()
    pedidos = view_all_pedidos()
    for i in pedidos:
        p_post = i[0]
        p_date = i[1]
        st.markdown(pedidos_temp.format(p_post, p_date), unsafe_allow_html=True)

    date_today = datetime.today().strftime('%m/%d/%Y')
    st.markdown('''
    ---

    ##### Escriba su pedido abajo y presione el boton para agregar a la lista
    ''')
    pedido_post = st.text_area('')
    if st.button('Agregar'):
        add_pedidos_data(pedido_post, date_today)
        st.success("Pedido agregado {}".format(date_today))

def admin(prev_vars): # Fifth Page

    inputs = st.empty()
    with inputs.container():
        st.subheader('Log In')
        st.write('Solo para administradores de la pagina')
        username = st.text_input("Please input your username:")
        passwd = st.text_input("Please input your password",type='password')

    if username == st.secrets["DB_USERNAME"] and passwd == st.secrets["DB_PASSWORD"]:
        inputs.empty()
        st.subheader('Admin Dashboard')
        st.success("Welcome back！")
        st.markdown('''
        ### Anuncios
        ##### Escriba su anuncio abajo y presione el boton para agregar a la lista
        ''')
        anuncio_title = st.text_input('Titulo del Anuncio')
        anuncio_post = st.text_area('Anuncio')
        anuncio_date = st.date_input('Fecha del Evento').strftime('%m/%d/%Y')
    
        if st.button('Agregar'):
            add_anuncios_data(anuncio_title, anuncio_post, anuncio_date)
            st.success("Anuncio Agregado {}".format(anuncio_date))

        # Manage Anuncios Table
        anucio_results = view_all_anuncios()
        clean_anuncios = pd.DataFrame(anucio_results,columns=["Titulo", "Anuncio", "Fecha"])
        st.dataframe(clean_anuncios)

        all_anuncios = [i[0] for i in view_all_anuncios()]
        select_anuncio = st.selectbox("Seleccionar Anuncio", all_anuncios)

        if st.button('Borrar Anuncio'):
            delete_anuncio(select_anuncio)
            st.warning("{} ha sido borrado de la pagina principal".format(select_anuncio))

        # Divider line for Lesson settings
        st.markdown("""
        ---
            
        #### Comentarios de la lección
        """)

        

        # Divider line for Requests settings
        st.markdown("""
        ---

        #### Pedidos
        """)

        # Manage Pedidos Table
        pedido_results = view_all_pedidos()
        clean_pedidos = pd.DataFrame(pedido_results,columns=["Pedido", "Fecha"])
        st.dataframe(clean_pedidos)

        all_pedidos = [i[0] for i in view_all_pedidos()]
        select_pedido = st.selectbox("Seleccionar Pedido", all_pedidos)

        if st.button('Borrar Pedido'):
            delete_pedido(select_pedido)
            st.warning("{} Borrado de la pagina principal".format(select_pedido))

        

    else:
        st.info("Username and/or password are incorrect")


# app.set_initial_page(app1)
app.add_app("Pagina Principal", main) #Adds first page (app1) to the framework
app.add_app("Escuela Sabatica", lesson) #Adds second page (app2) to the framework
app.add_app("Registro de Estudio", app3) #Adds third page (app3) to the framework
app.add_app("Pedidos de Oración", prayer)
app.add_app("Admin", admin)
app.run() #Runs the multipage app!
