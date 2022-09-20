import streamlit as st
import pandas as pd
import sqlite3
import numpy as np

conn = sqlite3.connect('data/orb.db')

st.title('Réferentiel ORB : ')
lst_orb_occupations = pd.read_sql("select DISTINCT(orb_occupation) from orb_experience_salary", conn)
lst_orb_occupations = list(np.unique(lst_orb_occupations))

metier = st.sidebar.selectbox("Métier : ", options=lst_orb_occupations)
xp = pd.read_sql("select distinct(experience) from "
                 f"orb_experience_salary where orb_occupation='{metier}' "
                 "and mean is not NULL", conn)

annee = st.sidebar.selectbox('Année d xp en mois :', options=list(np.unique(xp['experience'])))

df_tempo = pd.read_sql("select * from "
                       f"orb_experience_salary where orb_occupation='{metier}'", conn)

st.subheader(f'Métier : {metier} avec : {annee} xp')
st.write(f"- Salaire moyen : {df_tempo['mean'].values[0]} €")
st.write(f"- Salire median : {df_tempo['median'].values[0]} €")
st.write(f"- Salaire minimum : {df_tempo['min'].values[0]} €")
st.write(f"- Salaire maximum : {df_tempo['max'].values[0]} €")
st.write(f"- Salaire écart type : {df_tempo['ecart_type'].values[0]} €")

st.write(f"- Nombre d'offres : {df_tempo['offre_salaire'].values[0]}")
st.write(f"- Nombre d'offres sans salaire précisé : {df_tempo['offre_sans_salaire'].values[0]}")


st.subheader(f'Liste des observations pour le metier : {metier} ')
st.dataframe(df_tempo[[ "orb_occupation", "experience", "offre_salaire", "mean", "median", "min", "max",
                              "offre_sans_salaire", "ecart_type"]])
df_tempo=df_tempo.sort_values(by='experience')
st.subheader(f"la moyenne des salaires :  ")
st.bar_chart(df_tempo,x="experience",y="mean")
st.subheader(f"la median des salaires :  ")
st.bar_chart(df_tempo,x="experience",y="median")
st.subheader(f"le min des salaires  :  ")
st.bar_chart(df_tempo,x="experience",y="min")
st.subheader(f"le max des salaires :  ")
st.bar_chart(df_tempo,x="experience",y="max")
st.subheader(f"le nombre d offres  :  ")
st.bar_chart(df_tempo,x="experience",y="offre_salaire")
st.bar_chart(df_tempo,x="experience",y=["offre_salaire","offre_sans_salaire"])
