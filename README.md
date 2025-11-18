# 🏥 Dashboard Inteligente de Risco Cardíaco

Este projeto implementa um **dashboard interativo** para análise de risco cardíaco utilizando:

- 📊 Estatística descritiva  
- 📈 Visualizações exploratórias  
- 🔥 Correlação entre variáveis  
- 🧠 Sistema de **Lógica Fuzzy** para classificação de risco  
- 🖥️ Desenvolvimento em **Streamlit**

O objetivo é criar uma ferramenta simples, moderna e inteligente para interpretar fatores relacionados ao risco cardíaco.

---

## 📁 Estrutura do Projeto

```
risco_cardiaco/
│
├── data/
│ └── risco_cardiaco.csv
│
├── src/
│ ├── load_data.py # Funções de carregamento de dados
│ ├── correlacao.py # Cálculo de correlação
│ ├── visualizacao.py # Funções gráficas
│ ├── fuzzy_risco.py # Sistema fuzzy completo
│
└── dashboard.py # Dashboard principal
```


---

## 🧠 Lógica Fuzzy – Risco Cardíaco

O sistema fuzzy utiliza variáveis linguísticas e regras para estimar o risco cardíaco com base em:

### **Entradas**
- Idade  
- Colesterol  
- Pressão arterial  

### **Saída**
- Risco cardíaco (0 a 100)

### **Exemplos de Regras Fuzzy**
- Se **colesterol** é ALTO e **pressão** é ALTA → risco é ALTO  
- Se **colesterol** é MÉDIO e **pressão** é MÉDIA → risco é MODERADO  
- Se **colesterol** é BAIXO e **pressão** é BAIXA → risco é BAIXO  
- Se **idade** é IDOSO e **colesterol** é ALTO → risco é ALTO  

As funções de pertinência são triangulares (trimf) e implementadas com `scikit-fuzzy`.

---

## 📊 Funcionalidades do Dashboard

### **📊 1. Estatísticas Gerais**
- Cards com idade média, colesterol médio e pressão média  
- Tabela completa dos pacientes  

---

### **📈 2. Correlação**
- Matriz de correlação entre as variáveis  
- Mapa de calor (heatmap) com paleta “coolwarm”  

---

### **📉 3. Visualizações**
- Gráfico de dispersão (colesterol × pressão) segmentado por risco  
- Distribuição das variáveis:
  - Idade  
  - Colesterol  
  - Pressão  

---

### **🧠 4. Sistema Fuzzy**
- Sliders para alterar os valores  
- Cálculo fuzzy do risco em tempo real  
- Classificação visual:
  - 🟢 Baixo risco  
  - 🟡 Risco moderado  
  - 🔴 Alto risco  
- Explicação textual de como a lógica fuzzy funciona  

---

## 🚀 Como Executar o Projeto

### **1. Clone o repositório**

```bash
git clone https://github.com/seuusuario/risco_cardiaco.git
cd risco_cardiaco
```

2. Crie o ambiente virtual
```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Execute o dashboard
```bash
streamlit run dashboard.py
```

📦 Minimundo (risco_cardiaco.csv)

| paciente | idade | colesterol | pressao | risco |
| -------- | ----- | ---------- | ------- | ----- |
| 1        | 45    | 220        | 140     | 1     |
| 2        | 38    | 180        | 125     | 0     |
| 3        | 50    | 260        | 155     | 1     |
| 4        | 29    | 170        | 110     | 0     |



🛠️ Tecnologias Utilizadas

Python 3

Streamlit

Pandas

Matplotlib

Seaborn

SciPy

Scikit-Fuzzy

NetworkX

📌 Melhorias Futuras

 Adicionar Machine Learning supervisionado

 Criar API com FastAPI

 Exportar relatório em PDF

 Expandir o conjunto de variáveis médicas

 Conectar a um banco de dados

 ✨ Autor
Gabriel Raimundo