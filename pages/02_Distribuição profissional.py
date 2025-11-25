import streamlit as st
import pandas as pd
import plotly.express as px
import re

df = pd.read_csv('dataset/State_of_data_2023.csv')

st.title('Distribuição profissional — contagem por estado')

def _norm(s: str) -> str:
	s = str(s).lower()
	s = re.sub(r"[^a-z0-9]+", ' ', s)
	return s.strip()

state_col = None
cols_norm = {c: _norm(c) for c in df.columns}
state_keywords = ['uf onde mora', 'estado onde mora', 'uf onde', 'uf', 'estado']

state_col = next((c for c, n in cols_norm.items() if any(k in n for k in state_keywords)), None)
if state_col is None:
	state_col = next((c for c, n in cols_norm.items() if 'uf' in n.split() or 'estado' in n.split()), None)

else:
	s = df[state_col].astype(str).str.strip()
	sig = s.str.extract(r"\(([A-Za-z]{2})\)", expand=False)
	is_two_letters = s.str.match(r'^[A-Za-z]{2}$')
	sig[is_two_letters] = s[is_two_letters].str.upper()
	last_token = s.str.split().str[-1]
	mask = sig.isna() & last_token.str.match(r'^[A-Za-z]{2}$')
	sig[mask] = last_token[mask].str.upper()

	sig = sig.fillna(s)
	df['__uf'] = sig.astype(str)

	counts = df.groupby('__uf').size().reset_index(name='count')
	counts = counts[counts['__uf'].notna() & (counts['__uf'] != '')]
	counts = counts.sort_values('count', ascending=False)

	st.subheader('Estados com maior número de profissionais (contagem)')
	st.dataframe(counts.reset_index(drop=True))

    # Finalmente o gráfico
	top_n = st.slider('Mostrar top N estados', min_value=5, max_value=27, value=15)
	plot_df = counts.head(top_n).copy()
	
    # Barrinha simples
	fig = px.bar(plot_df, x='__uf', y='count', labels={'__uf':'UF', 'count':'Contagem'},
				 title=f'Top {top_n} estados por número de profissionais')
	fig.update_layout(xaxis=dict(type='category'))
	st.plotly_chart(fig, use_container_width=True)