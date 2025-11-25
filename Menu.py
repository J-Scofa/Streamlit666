import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Projeto Streamlit",
    page_icon=":📊:",
    layout="wide"
)

st.markdown(f"""
Aqui foram utilizados os mesmos dados do projeto de exemplo demonstrado pelo professor, porém ajustado para conter análises diferentes - ou seja dados da área de TI.

O objetivo deste projeto é demonstrar minhas habilidades em análise de dados e visualização utilizando a biblioteca Streamlit.
            
Nele haverá:
* **Composição por genero, raça e faixa etária** dos profissionais no Brasil;
* **Mapa por estado** com a distribuição dos profissionais;
* **Preferencia modelo de trabalho** (presencial, remoto, híbrido);
* **Análise de ferramentas e linguagens** mais utilizadas no mercado;
            
Para nevegar entre as seções, utilize o **menu lateral ⬅️**.
""")

df = pd.read_csv('dataset/State_of_data_2023.csv')

colunas_relevantes = [
    "('P1_b ', 'Genero')",
    "('P1_c ', 'Cor/raca/etnia')",
    "('P1_a_1 ', 'Faixa idade')",
    "('P1_i_1 ', 'uf onde mora')",
    "('P1_i_2 ', 'Regiao onde mora')",
    "('P2_r ', 'Atualmente qual a sua forma de trabalho?')",
    "('P2_s ', 'Qual a forma de trabalho ideal para você?')",
    "('P2_h ', 'Faixa salarial')",
    "('P2_i ', 'Quanto tempo de experiência na área de dados você tem?')",
    "('P4_d_1 ', 'SQL')",
    "('P4_d_3 ', 'Python')",
    "('P4_j_1 ', 'Microsoft PowerBI')",
    "('P4_j_3 ', 'Tableau')"
]

df = df[colunas_relevantes]

novos_nomes = {
    "('P1_b ', 'Genero')": 'Genero',
    "('P1_c ', 'Cor/raca/etnia')": 'Raca',
    "('P1_a_1 ', 'Faixa idade')": 'Faixa Etaria',
    "('P1_i_1 ', 'uf onde mora')": 'UF',
    "('P1_i_2 ', 'Regiao onde mora')": 'Regiao',
    "('P2_r ', 'Atualmente qual a sua forma de trabalho?')": 'Forma Trabalho Atual',
    "('P2_s ', 'Qual a forma de trabalho ideal para você?')": 'Forma Trabalho Ideal',
    "('P2_h ', 'Faixa salarial')": 'Faixa Salarial',
    "('P2_i ', 'Quanto tempo de experiência na área de dados você tem?')": 'Experiencia Dados',
    "('P4_d_1 ', 'SQL')": 'SQL',
    "('P4_d_3 ', 'Python')": 'Python',
    "('P4_j_1 ', 'Microsoft PowerBI')": 'PowerBI',
    "('P4_j_3 ', 'Tableau')": 'Tableau'
}

df.rename(columns=novos_nomes, inplace=True)
st.header("Informação trabalhada:")
st.dataframe(df.head())