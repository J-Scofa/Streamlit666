import streamlit as st
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('dataset/State_of_data_2023.csv')

colunas_relevantes = [
    "('P1_b ', 'Genero')",
    "('P1_c ', 'Cor/raca/etnia')",
    "('P1_a_1 ', 'Faixa idade')"
]
df = df[colunas_relevantes]

novos_nomes = {
    "('P1_b ', 'Genero')": 'Genero',
    "('P1_c ', 'Cor/raca/etnia')": 'Raca',
    "('P1_a_1 ', 'Faixa idade')": 'Faixa Etaria'
}
df.rename(columns=novos_nomes, inplace=True)

st.header('Composição por Gênero, Raça e Faixa Etária')

coluna_principal = st.selectbox('Selecione a variável principal:', ['Genero', 'Raca', 'Faixa Etaria'])

outras_colunas = [col for col in ['Genero', 'Raca', 'Faixa Etaria'] if col != coluna_principal]

df_grafico = df.groupby([coluna_principal] + outras_colunas).size().reset_index(name='Contagem')

fig = go.Figure()

for coluna_secundaria in df_grafico[outras_colunas[0]].unique():
    dados_filtrados = df_grafico[df_grafico[outras_colunas[0]] == coluna_secundaria]
    fig.add_trace(go.Bar(
        x=dados_filtrados[coluna_principal],
        y=dados_filtrados['Contagem'],
        name=str(coluna_secundaria)
    ))

fig.update_layout(
    barmode='stack',
    title=f'Composição por {coluna_principal}',
    xaxis_title=coluna_principal,
    yaxis_title='Quantidade',
    height=500
)

st.plotly_chart(fig, use_container_width=True)