import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def grafico_disp(df):
    fig, ax = plt.subplots()
    sns.scatterplot(df, x='colesterol', y='pressao', hue='risco', palette='coolwarm', s=100)
    plt.title("Colesterol × Pressão — Distribuição por Risco")
    plt.xlabel("Colesterol (mg/dL)")
    plt.ylabel("Pressão (mmHg)")
    st.pyplot(fig)


def mapa_calor(corr):
    fig, ax = plt.subplots(figsize=(6,4))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Mapa de Calor das Correlações")
    st.pyplot(fig)
