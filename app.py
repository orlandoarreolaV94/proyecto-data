import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Análisis de anuncios de venta de coches')

build_histogram = st.checkbox('Construir un histograma')
if build_histogram:
    st.write('Histograma para la columna odometer')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Construir un gráfico de dispersión')
if build_scatter:
    st.write('Gráfico de dispersión: precio vs. odometer')
    fig2 = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig2, use_container_width=True)