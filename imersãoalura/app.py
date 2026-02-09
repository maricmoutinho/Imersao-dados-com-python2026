import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- CONFIGURAÇÃO DA PÁGINA ----------------
st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="📊",
    layout="wide",
)

# ---------------- CARREGAMENTO DOS DADOS ----------------
@st.cache_data
def carregar_dados():
    return pd.read_csv(
        "https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv"
    )

df = carregar_dados()

# ---------------- SIDEBAR - FILTROS ----------------
st.sidebar.header("🔍 Filtros")

# Resetar filtros
if st.sidebar.button("🔄 Resetar filtros"):
    st.experimental_rerun()

# Ano
anos_disponiveis = sorted(df['ano'].unique())
anos_selecionados = st.sidebar.multiselect(
    "Ano", anos_disponiveis, default=anos_disponiveis
)

# Senioridade
senioridades_disponiveis = sorted(df['senioridade'].unique())
senioridades_selecionadas = st.sidebar.multiselect(
    "Senioridade", senioridades_disponiveis, default=senioridades_disponiveis
)

# Tipo de contrato
contratos_disponiveis = sorted(df['contrato'].unique())
contratos_selecionados = st.sidebar.multiselect(
    "Tipo de Contrato", contratos_disponiveis, default=contratos_disponiveis
)

# Tamanho da empresa
tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())
tamanhos_selecionados = st.sidebar.multiselect(
    "Tamanho da Empresa", tamanhos_disponiveis, default=tamanhos_disponiveis
)

# Cargo
cargos_disponiveis = sorted(df['cargo'].unique())
cargos_selecionados = st.sidebar.multiselect(
    "Cargo", cargos_disponiveis, default=cargos_disponiveis
)

# Remoção de outliers
remover_outliers = st.sidebar.checkbox("Remover outliers (99%)")

# ---------------- FILTRAGEM DO DATAFRAME ----------------
df_filtrado = df[
    (df['ano'].isin(anos_selecionados)) &
    (df['senioridade'].isin(senioridades_selecionadas)) &
    (df['contrato'].isin(contratos_selecionados)) &
    (df['tamanho_empresa'].isin(tamanhos_selecionados)) &
    (df['cargo'].isin(cargos_selecionados))
]

if remover_outliers and not df_filtrado.empty:
    limite = df_filtrado['usd'].quantile(0.99)
    df_filtrado = df_filtrado[df_filtrado['usd'] <= limite]

# ---------------- CONTEÚDO PRINCIPAL ----------------
st.title("🎲 Dashboard de Análise de Salários na Área de Dados")
st.markdown(
    "Explore os dados salariais na área de dados. "
    "Utilize os filtros à esquerda para refinar sua análise."
)

# ---------------- KPIs ----------------
st.subheader("Métricas gerais (Salário anual em USD)")

if not df_filtrado.empty:
    salario_medio = df_filtrado['usd'].mean()
    salario_mediano = df_filtrado['usd'].median()
    salario_maximo = df_filtrado['usd'].max()
    total_registros = df_filtrado.shape[0]
    cargo_mais_frequente = df_filtrado['cargo'].mode()[0]
else:
    salario_medio = salario_mediano = salario_maximo = 0
    total_registros = 0
    cargo_mais_frequente = ""

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Salário médio", f"${salario_medio:,.0f}")
col2.metric("Salário mediano", f"${salario_mediano:,.0f}")
col3.metric("Salário máximo", f"${salario_maximo:,.0f}")
col4.metric("Total de registros", f"{total_registros:,}")
col5.metric("Cargo mais frequente", cargo_mais_frequente)

st.caption(
    f"Análise baseada em {total_registros:,} registros "
    f"entre {min(anos_selecionados)} e {max(anos_selecionados)}."
)

st.markdown("---")

# ---------------- GRÁFICOS ----------------
st.subheader("Gráficos")

col_graf1, col_graf2 = st.columns(2)

# Top 10 cargos
with col_graf1:
    if not df_filtrado.empty:
        top_cargos = (
            df_filtrado.groupby('cargo')['usd']
            .mean()
            .nlargest(10)
            .sort_values()
            .reset_index()
        )

        fig = px.bar(
            top_cargos,
            x='usd',
            y='cargo',
            orientation='h',
            title="Top 10 cargos por salário médio",
            labels={'usd': 'Salário médio anual (USD)', 'cargo': ''}
        )
        fig.update_layout(title_x=0.1)
        st.plotly_chart(fig, use_container_width=True)

# Distribuição salarial
with col_graf2:
    if not df_filtrado.empty:
        fig = px.histogram(
            df_filtrado,
            x='usd',
            nbins=30,
            title="Distribuição de salários anuais",
            labels={'usd': 'Salário (USD)', 'count': ''}
        )
        fig.update_layout(title_x=0.1)
        st.plotly_chart(fig, use_container_width=True)

col_graf3, col_graf4 = st.columns(2)

# Tipo de trabalho
with col_graf3:
    if not df_filtrado.empty:
        remoto = df_filtrado['remoto'].value_counts().reset_index()
        remoto.columns = ['tipo_trabalho', 'quantidade']

        fig = px.pie(
            remoto,
            names='tipo_trabalho',
            values='quantidade',
            hole=0.5,
            title="Proporção dos tipos de trabalho"
        )
        fig.update_traces(textinfo='percent+label')
        fig.update_layout(title_x=0.1)
        st.plotly_chart(fig, use_container_width=True)

# Mapa Data Scientist
with col_graf4:
    df_ds = df_filtrado[df_filtrado['cargo'] == 'Data Scientist']
    if not df_ds.empty:
        media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()

        fig = px.choropleth(
            media_ds_pais,
            locations='residencia_iso3',
            color='usd',
            color_continuous_scale='rdylgn',
            title="Salário médio de Data Scientist por país",
            labels={'usd': 'Salário médio (USD)'}
        )
        fig.update_layout(title_x=0.1)
        st.plotly_chart(fig, use_container_width=True)

# ---------------- GRÁFICOS ANALÍTICOS ----------------
st.markdown("---")
st.subheader("Análises adicionais")

col_a1, col_a2 = st.columns(2)

# Evolução salarial
with col_a1:
    if not df_filtrado.empty:
        salario_ano = df_filtrado.groupby('ano')['usd'].mean().reset_index()
        fig = px.line(
            salario_ano,
            x='ano',
            y='usd',
            markers=True,
            title="Evolução do salário médio ao longo dos anos"
        )
        fig.update_layout(title_x=0.1)
        st.plotly_chart(fig, use_container_width=True)

# Boxplot por senioridade
with col_a2:
    if not df_filtrado.empty:
        fig = px.box(
            df_filtrado,
            x='senioridade',
            y='usd',
            title="Distribuição salarial por senioridade"
        )
        fig.update_layout(title_x=0.1)
        st.plotly_chart(fig, use_container_width=True)

# ---------------- TABELA ----------------
st.subheader("Dados Detalhados")
st.dataframe(df_filtrado)
