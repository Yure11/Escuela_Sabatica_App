from google.protobuf.symbol_database import Default
import streamlit as st
import pandas as pd
import numpy as np

st.title('Escuela Sabatica')
st.subheader('Repaso de la Leccion 1er Trimestre')

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
df.index = df.index[:6].tolist() + days

st.bar_chart(df)

st.subheader('Llevando estudios biblicos?')
st.checkbox('Si')
st.checkbox('No')