import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('dataset/State_of_data_2023.csv')

st.title("Salário por Nível de Experiência")

nivel_col = [col for col in df.columns if 'Nivel' in col and 'Ensino' not in col][0]
salario_col = [col for col in df.columns if 'Faixa salarial' in col][0]

nivel_mapping = {
    'Júnior': 1,
    'Pleno': 2,
    'Sênior': 3,
    'Gerente/Head': 4
}

salario_mapping = {
    'de R$ 1.001/mês a R$ 2.000/mês': 1500,
    'de R$ 2.001/mês a R$ 3.000/mês': 2500,
    'de R$ 3.001/mês a R$ 4.000/mês': 3500,
    'de R$ 4.001/mês a R$ 6.000/mês': 5000,
    'de R$ 6.001/mês a R$ 8.000/mês': 7000,
    'de R$ 8.001/mês a R$ 12.000/mês': 10000,
    'de R$ 12.001/mês a R$ 16.000/mês': 14000,
    'de R$ 16.001/mês a R$ 20.000/mês': 18000,
    'de R$ 20.001/mês a R$ 25.000/mês': 22500,
    'de R$ 25.001/mês a R$ 30.000/mês': 27500,
    'Acima de R$ 40.001/mês': 45000
}

df['Nivel_num'] = df[nivel_col].map(nivel_mapping)
df['Salario_num'] = df[salario_col].map(salario_mapping)

df_clean = df[['Nivel_num', 'Salario_num', nivel_col]].dropna()

np.random.seed(42)
jitter_strength = 0.1
df_clean['Nivel_jitter'] = df_clean['Nivel_num'] + np.random.normal(0, jitter_strength, len(df_clean))
df_clean['Salario_jitter'] = df_clean['Salario_num'] + np.random.normal(0, 500, len(df_clean))

# graf
fig, ax = plt.subplots(figsize=(10, 6))

scatter = ax.scatter(df_clean['Nivel_jitter'], df_clean['Salario_jitter'], 
                     alpha=0.5, s=100, c=df_clean['Nivel_num'], 
                     cmap='viridis', edgecolors='black', linewidth=0.5)

ax.set_xlabel('Nível de Experiência', fontsize=12, fontweight='bold')
ax.set_ylabel('Salário (R$)', fontsize=12, fontweight='bold')
ax.set_title('Distribuição de Salários por Nível de Experiência', fontsize=14, fontweight='bold')
ax.set_xticks([1, 2, 3, 4])
ax.set_xticklabels(['Júnior', 'Pleno', 'Sênior', 'Gerente/Head'])
ax.grid(True, alpha=0.3)


ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R$ {x:,.0f}'))

plt.tight_layout()
st.pyplot(fig)


st.subheader("Estatísticas por Nível")

for nivel, num in sorted(nivel_mapping.items(), key=lambda x: x[1]):
    dados_nivel = df_clean[df_clean['Nivel_num'] == num]['Salario_num']
    
    if len(dados_nivel) > 0:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Nível", nivel)
        with col2:
            st.metric("Média", f"R$ {dados_nivel.mean():,.0f}")
        with col3:
            st.metric("Mínima", f"R$ {dados_nivel.min():,.0f}")
        with col4:
            st.metric("Máxima", f"R$ {dados_nivel.max():,.0f}")
        
        st.divider()

