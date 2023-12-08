import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title="Previsão de Renda - Análise exploratória",
     layout="wide",
)

st.write('# Análise exploratória da previsão de renda')

renda = pd.read_csv('./input/previsao_de_renda.csv')

#plots
fig, ax = plt.subplots(8,1,figsize=(10,70))
renda[['posse_de_imovel','renda']].plot(kind='hist', ax=ax[0])
st.write('## Gráficos ao longo do tempo')
sns.lineplot(x='data_ref',y='renda', hue='posse_de_imovel',data=renda, ax=ax[1]).set(title='Gráfico de renda ao longo do tempo por posse de imóvel')
ax[1].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='posse_de_veiculo',data=renda, ax=ax[2]).set(title='Gráfico de renda ao longo do tempo por posse de veículo')
ax[2].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='qtd_filhos',data=renda, ax=ax[3]).set(title='Gráfico de renda ao longo do tempo por quantidade de filho')
ax[3].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='tipo_renda',data=renda, ax=ax[4]).set(title='Gráfico de renda ao longo do tempo por tipo de renda')
ax[4].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='educacao',data=renda, ax=ax[5]).set(title='Gráfico de renda ao longo do tempo por escolaridade')
ax[5].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='estado_civil',data=renda, ax=ax[6]).set(title='Gráfico de renda ao longo do tempo por estado civil')
ax[6].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='tipo_residencia',data=renda, ax=ax[7]).set(title='Gráfico de renda ao longo do tempo por tipo de residencia')
ax[7].tick_params(axis='x', rotation=45)

plt.subplots_adjust(hspace=0.5)
sns.despine()
st.pyplot(plt)


st.write('## Gráficos bivariada')
fig, ax = plt.subplots(7,1,figsize=(10,50))
sns.barplot(x='posse_de_imovel',y='renda',data=renda, ax=ax[0]).set(title='Gráfico de posse de imóvel x renda')
ax[0].tick_params(axis='x', rotation=45)
sns.barplot(x='posse_de_veiculo',y='renda',data=renda, ax=ax[1]).set(title='Gráfico de posse de veículo x renda')
ax[1].tick_params(axis='x', rotation=45)
sns.barplot(x='qtd_filhos',y='renda',data=renda, ax=ax[2]).set(title='Gráfico de quantidade de filhos x renda')
ax[2].tick_params(axis='x', rotation=45)
sns.barplot(x='tipo_renda',y='renda',data=renda, ax=ax[3]).set(title='Gráfico de tipo de renda x renda')
ax[3].tick_params(axis='x', rotation=45)
sns.barplot(x='educacao',y='renda',data=renda, ax=ax[4]).set(title='Gráfico de escolaridade x renda')
ax[4].tick_params(axis='x', rotation=45)
sns.barplot(x='estado_civil',y='renda',data=renda, ax=ax[5]).set(title='Gráfico de estado civil x renda')
ax[5].tick_params(axis='x', rotation=45)
sns.barplot(x='tipo_residencia',y='renda',data=renda, ax=ax[6]).set(title='Gráfico de tipo de residencia x renda')
ax[6].tick_params(axis='x', rotation=45)
plt.subplots_adjust(hspace=0.7)
sns.despine()
st.pyplot(plt)





