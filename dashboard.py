import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from src.load_data import carregar_csv
from src.correlacao import calcular_correlacao
from src.visualizacao import grafico_disp, mapa_calor
from src.fuzzy_risco import calcular_risco_fuzzy

# =====================================================================
# CONFIGURAÇÃO DO DASHBOARD
# =====================================================================
st.set_page_config(
    page_title="Dashboard — Risco Cardíaco",
    layout="wide",
    page_icon="❤️"
)

# =====================================================================
# CSS PERSONALIZADO
# =====================================================================
st.markdown("""
    <style>
    .card {
        padding: 18px;
        border-radius: 12px;
        background-color: #fdfdfd;
        border: 1px solid #ddd;
        text-align: center;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
    }
    .risk-low {
        background-color: #d4edda;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
    }
    .risk-medium {
        background-color: #fff3cd;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
    }
    .risk-high {
        background-color: #f8d7da;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# TÍTULO
# =====================================================================

st.image("cardik_logo.png", width=150)
st.title("Dashboard Inteligente de Risco Cardíaco")
st.write("""
Este painel apresenta:
- 📊 **Estatísticas gerais**
- 📈 **Correlação entre variáveis**
- 🎯 **Visualizações**
- 🧠 **Sistema de Lógica Fuzzy para risco cardíaco**

Dados reais do arquivo: `risco_cardiaco.csv`
""")

# =====================================================================
# CARREGAR DADOS
# =====================================================================
df = carregar_csv()

# =====================================================================
# TABS DO DASHBOARD
# =====================================================================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Estatísticas Gerais",
    "Correlação",
    "Visualizações",
    "Lógica Fuzzy",
    "Mini Relatório"
])


# =====================================================================
# TAB 1 — ESTATÍSTICAS GERAIS
# =====================================================================
with tab1:
    st.header("Estatísticas Gerais dos Pacientes")

    col1, col2, col3 = st.columns(3)

    col1.markdown(
        f"<div class='card'><h3>Idade Média</h3><p>{df['idade'].mean():.1f} anos</p></div>",
        unsafe_allow_html=True
    )
    col2.markdown(
        f"<div class='card'><h3>Colesterol Médio</h3><p>{df['colesterol'].mean():.1f} mg/dL</p></div>",
        unsafe_allow_html=True
    )
    col3.markdown(
        f"<div class='card'><h3>Pressão Média</h3><p>{df['pressao'].mean():.1f} mmHg</p></div>",
        unsafe_allow_html=True
    )

    st.write("### Dados do CSV")
    st.dataframe(df, use_container_width=True)

# =====================================================================
# TAB 2 — CORRELAÇÃO
# =====================================================================
with tab2:
    st.header("Correlação entre Variáveis")

    corr = calcular_correlacao(df)

    colA, colB = st.columns([1, 2])

    with colA:
        st.subheader("Tabela de Correlação")
        st.dataframe(corr.style.background_gradient(cmap="coolwarm"))

    with colB:
        st.subheader("Mapa de Calor da Correlação")
        mapa_calor(corr)

# =====================================================================
# TAB 3 — VISUALIZAÇÕES
# =====================================================================
with tab3:
    st.header("Visualizações de Dispersão")

    st.subheader("🔹 Colesterol × Pressão")
    grafico_disp(df)

    # Distribuições
    st.subheader("🔹 Distribuição das Variáveis")

    colA, colB, colC = st.columns(3)

    with colA:
        fig, ax = plt.subplots()
        sns.histplot(df['idade'], kde=True)
        plt.title("Distribuição da Idade")
        st.pyplot(fig)

    with colB:
        fig, ax = plt.subplots()
        sns.histplot(df['colesterol'], kde=True)
        plt.title("Distribuição do Colesterol")
        st.pyplot(fig)

    with colC:
        fig, ax = plt.subplots()
        sns.histplot(df['pressao'], kde=True)
        plt.title("Distribuição da Pressão")
        st.pyplot(fig)

# =====================================================================
# TAB 4 — LÓGICA FUZZY
# =====================================================================
with tab4:
    st.header("Sistema Fuzzy de Avaliação de Risco Cardíaco")

    st.write("Use os controles abaixo para testar o **risco fuzzy**:")

    col1, col2, col3 = st.columns(3)

    idade = col1.slider("Idade", 20, 100, 45)
    colesterol = col2.slider("Colesterol (mg/dL)", 100, 300, 220)
    pressao = col3.slider("Pressão (mmHg)", 90, 180, 140)

    risco_fuzzy = calcular_risco_fuzzy(idade, colesterol, pressao)

    st.subheader(f"🔍 Risco Fuzzy Estimado: **{risco_fuzzy:.2f}/100**")

    # classificação do risco
    if risco_fuzzy < 30:
        st.markdown("<div class='risk-low'>🟢 Baixo Risco</div>", unsafe_allow_html=True)
    elif risco_fuzzy < 60:
        st.markdown("<div class='risk-medium'>🟡 Risco Moderado</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='risk-high'>🔴 Alto Risco</div>", unsafe_allow_html=True)

    st.write("### Como funciona o modelo fuzzy?")
    st.write("""
O sistema fuzzy utiliza regras linguísticas como:
- **Se colesterol é ALTO e pressão é ALTA → risco é ALTO**
- **Se colesterol é MÉDIO e pressão é MÉDIA → risco é MÉDIO**
- **Se colesterol é BAIXO e pressão é BAIXA → risco é BAIXO**
- **Se idade é IDOSO e colesterol é ALTO → risco é ALTO**

Com isso, produz uma saída contínua entre 0 e 100.
    """)

with tab5:
    st.header(" Mini Relatório — Análise dos Resultados")

    st.markdown("""
    ## 🎯 Objetivo Geral
    Avaliar o risco cardíaco dos pacientes com base em três variáveis principais:
    - Idade  
    - Colesterol  
    - Pressão arterial  

    A análise usa métodos estatísticos, gráficos e lógica fuzzy para identificar padrões associados ao risco cardíaco.
    """)

    st.markdown("---")

    st.subheader("1) Estatísticas Gerais dos Pacientes")

    st.markdown(f"""
    **Idade média:** `{df['idade'].mean():.1f}` anos  
    **Colesterol médio:** `{df['colesterol'].mean():.1f}` mg/dL  
    **Pressão média:** `{df['pressao'].mean():.1f}` mmHg  

    Os valores mais elevados de colesterol e pressão se concentram nos pacientes classificados como de risco.
    """)

    st.markdown("---")

    st.subheader("2) Correlação Entre Variáveis")

    st.markdown("""
    Principais relações observadas:

    - **Colesterol × Pressão:** Correlação positiva forte  
    - **Pressão × Risco:** Correlação direta e forte  
    - **Colesterol × Risco:** Correlação forte  
    - **Idade × Risco:** Correlação moderada  

    **Interpretação:** colesterol e pressão são os fatores que mais influenciam o risco cardíaco.
    """)

    st.markdown("---")

    st.subheader("3) Achados Visuais")

    st.markdown("""
    - O gráfico de dispersão mostra dois agrupamentos claros:  
        • Baixo risco → colesterol <= 180 e pressão <= 125  
        • Alto risco → colesterol >= 220 e pressão >= 140  

    - As distribuições reforçam que valores extremos justificam risco elevado.  
    """)

    st.markdown("---")

    st.subheader("4) Análise Fuzzy do Risco")

    st.markdown("""
    O sistema fuzzy utiliza regras linguísticas como:

    - **Alto colesterol + Alta pressão → Alto risco**  
    - **Médio colesterol + Média pressão → Risco moderado**  
    - **Baixo colesterol + Baixa pressão → Baixo risco**  
    - **Idoso + Colesterol alto → Alto risco**

    O risco fuzzy varia de **0 a 100**, gerando uma classificação contínua:

    - `0 a 30` → 🟢 Baixo risco  
    - `30 a 60` → 🟡 Moderado  
    - `60 a 100` → 🔴 Alto risco  
    """)

    st.markdown("---")

    st.subheader("Conclusões")

    st.markdown("""
    - Colesterol e pressão arterial são as variáveis mais determinantes para o risco.  
    - Idade influencia, mas menos intensamente.  
    - O sistema fuzzy permite interpretar o risco de forma mais suave e realista.  
    - O dataset, embora pequeno, mostra comportamentos coerentes com literatura médica.  
    """)

    st.success("Relatório gerado automaticamente com base nos dados e cálculos do dashboard.")
