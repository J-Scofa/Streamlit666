import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv('dataset/State_of_data_2023.csv')

st.title("Tecnologias mais utilizadas")

#Encontrar colunas
def find_columns(df, pattern):
    """Colunas em padrão"""
    return [col for col in df.columns if pattern in col]

tab1, tab2, tab3, tab4 = st.tabs(["Linguagens", "Bancos de Dados", "Ferramentas de BI", "Cloud"])

with tab1:
    st.subheader("Linguagens de Programação Mais Utilizadas")
    
    lang_mapping = {
        'SQL': find_columns(df, "P4_d_1 "),
        'R': find_columns(df, "P4_d_2 "),
        'Python': find_columns(df, "P4_d_3 "),
        'Java': find_columns(df, "P4_d_6 "),
        'JavaScript': find_columns(df, "P4_d_14 "),
    }
    
    lang_data = []
    for tech_name, cols in lang_mapping.items():
        if cols:
            col = cols[0]
            count = (df[col] == 1).sum()
            if count > 0:
                lang_data.append({'Tecnologia': tech_name, 'Uso': count})
    
    if lang_data:
        lang_df = pd.DataFrame(lang_data).sort_values('Uso', ascending=False)
        fig = px.pie(lang_df, values='Uso', names='Tecnologia', 
                    title='Linguagens Mais Utilizadas',
                    color_discrete_sequence=px.colors.qualitative.Set3)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(lang_df, use_container_width=True)
    else:
        st.warning("Nenhum dado disponível")

with tab2:
    st.subheader("Bancos de Dados Mais Utilizados")
    
    db_mapping = {
        'MySQL': find_columns(df, "P4_g_1 "),
        'PostgreSQL': find_columns(df, "P4_g_12 "),
        'Google BigQuery': find_columns(df, "P4_g_22 "),
        'Snowflake': find_columns(df, "P4_g_26 "),
        'MongoDB': find_columns(df, "P4_g_8 "),
        'SQL SERVER': find_columns(df, "P4_g_3 "),
    }
    
    db_data = []
    for tech_name, cols in db_mapping.items():
        if cols:
            col = cols[0]
            count = (df[col] == 1).sum()
            if count > 0:
                db_data.append({'Tecnologia': tech_name, 'Uso': count})
    
    if db_data:
        db_df = pd.DataFrame(db_data).sort_values('Uso', ascending=False)
        fig = px.pie(db_df, values='Uso', names='Tecnologia',
                    title='Bancos de Dados Mais Utilizados',
                    color_discrete_sequence=px.colors.qualitative.Set2)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(db_df, use_container_width=True)
    else:
        st.warning("Nenhum dado disponível")

with tab3:
    st.subheader("Ferramentas de BI Mais Utilizadas")
    
    bi_mapping = {
        'Microsoft PowerBI': find_columns(df, "P4_j_1 "),
        'Qlik': find_columns(df, "P4_j_2 "),
        'Tableau': find_columns(df, "P4_j_3 "),
        'Looker': find_columns(df, "P4_j_7 "),
        'Looker Studio': find_columns(df, "P4_j_8 "),
    }
    
    bi_data = []
    for tech_name, cols in bi_mapping.items():
        if cols:
            col = cols[0]
            count = (df[col] == 1).sum()
            if count > 0:
                bi_data.append({'Tecnologia': tech_name, 'Uso': count})
    
    if bi_data:
        bi_df = pd.DataFrame(bi_data).sort_values('Uso', ascending=False)
        fig = px.pie(bi_df, values='Uso', names='Tecnologia',
                    title='Ferramentas de BI Mais Utilizadas',
                    color_discrete_sequence=px.colors.qualitative.Pastel)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(bi_df, use_container_width=True)
    else:
        st.warning("Nenhum dado disponível")

with tab4:
    st.subheader("Provedores de Cloud Mais Utilizados")
    
    cloud_mapping = {
        'Azure (Microsoft)': find_columns(df, "P4_h_1 "),
        'AWS': find_columns(df, "P4_h_2 "),
        'Google Cloud (GCP)': find_columns(df, "P4_h_3 "),
    }
    
    cloud_data = []
    for tech_name, cols in cloud_mapping.items():
        if cols:
            col = cols[0]
            count = (df[col] == 1).sum()
            if count > 0:
                cloud_data.append({'Tecnologia': tech_name, 'Uso': count})
    
    if cloud_data:
        cloud_df = pd.DataFrame(cloud_data).sort_values('Uso', ascending=False)
        fig = px.pie(cloud_df, values='Uso', names='Tecnologia',
                    title='Provedores de Cloud Mais Utilizados',
                    color_discrete_sequence=px.colors.qualitative.Dark24)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(cloud_df, use_container_width=True)
    else:
        st.warning("Nenhum dado disponível")