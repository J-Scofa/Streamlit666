import streamlit as st
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('dataset/State_of_data_2023.csv')

col_trabalho_ideal = "('P2_s ', 'Qual a forma de trabalho ideal para você?')"

st.header("Preferência de Tipo de Trabalho")

trabalho_ideal = df[col_trabalho_ideal].value_counts()

trabalho_ideal_limpo = {}
for idx, val in trabalho_ideal.items():
    if pd.notna(idx) and idx != '':
        idx_str = str(idx).lower()
        if 'presencial' in idx_str and 'híbrido' not in idx_str:
            chave = 'Presencial'
        elif '100% remoto' in idx_str or 'remoto' in idx_str and '100%' in str(idx):
            chave = 'Remoto'
        elif 'híbrido' in idx_str or 'hybrid' in idx_str:
            chave = 'Híbrido'
        else:
            continue
        
        if chave in trabalho_ideal_limpo:
            trabalho_ideal_limpo[chave] += val
        else:
            trabalho_ideal_limpo[chave] = val

# Criar gráfico de barras
fig = go.Figure(data=[
    go.Bar(
        x=list(trabalho_ideal_limpo.keys()),
        y=list(trabalho_ideal_limpo.values()),
        marker_color=['#636EFA', '#EF553B', '#00CC96'],
        text=list(trabalho_ideal_limpo.values()),
        textposition='auto',
    )
])

fig.update_layout(
    title='Preferência de Tipo de Trabalho',
    xaxis_title='Tipo de Trabalho',
    yaxis_title='Quantidade de Pessoas',
    height=500,
    hovermode='x unified'
)

st.plotly_chart(fig, use_container_width=True)