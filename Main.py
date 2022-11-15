import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

@st.cache
def load_data():
    df = pd.read_csv("credit_score.csv")
    return df

# Hanya akan di run sekali
df = load_data()

df = load_data()

_, col2, _ = st.columns([1, 2, 1])

with col2:
    st.image('./pinjaman.jpg')
    st.header('Form Pengajuan Pinjaman')


with st.form(key='my_form'):
   Pendapatan = st.text_input('Pendapatan Setahun')
   KPR_aktif = st.text_input('KPR Aktif')
   Durasi = st.text_input('Durasi Pinjaman Bulan')
   tanggungan = st.text_input('Jumlah Tanggungan')
   overdue = st.text_input('Rata-rata Overdue')
   st.form_submit_button('Check Resiko')

st.write('\n')
st.write('\n')
st.write("Source Code : [https://github.com/fadetul-f/creditScore-app](https://github.com/fadetul-f/creditScore-app)")
   