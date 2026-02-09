# Imersao-dados-com-python2026
📊 Dashboard interativo para análise de salários na área de dados usando Python, Streamlit e Plotly.
Este projeto foi desenvolvido durante uma Imersão em Python com Dados, com foco em análise, visualização e interpretação de dados reais da área de tecnologia, especialmente salários na área de dados.
Durante a imersão, foram trabalhados conceitos fundamentais como:
Manipulação de dados com Pandas
Criação de dashboards interativos com Streamlit
Visualizações avançadas com Plotly
Uso de filtros dinâmicos
Análise exploratória de dados (EDA)
Boas práticas de organização de código e apresentação de resultados
O objetivo final foi transformar um conjunto de dados brutos em um dashboard interativo, claro e informativo, permitindo análises profundas de forma intuitiva.

🎯 Objetivo do Projeto
Criar um dashboard interativo para analisar salários na área de dados, permitindo que o usuário explore informações como:
Evolução salarial ao longo dos anos
Diferenças salariais por cargo, senioridade e tipo de contrato
Distribuição dos salários
Comparação entre trabalho remoto, híbrido e presencial
Análise geográfica dos salários de Data Scientist por país
Tudo isso de forma visual, interativa e acessível.

🛠️ Tecnologias Utilizadas
Python
Streamlit – construção do dashboard
Pandas – manipulação e análise dos dados
Plotly Express – visualizações interativas
GitHub – versionamento e hospedagem dos dados

📂 Fonte dos Dados
Os dados utilizados estão disponíveis publicamente no GitHub e foram carregados diretamente via URL:
https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv
Eles contêm informações como:
Ano
Cargo
Senioridade
Tipo de contrato
Tipo de trabalho (remoto/presencial/híbrido)
Tamanho da empresa
País de residência
Salário anual em USD

⚙️ Explicação do Código
🔧 Configuração da Página
st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="📊",
    layout="wide",
)
Define o título, ícone e layout da aplicação, garantindo melhor experiência visual.

📥 Carregamento dos Dados
@st.cache_data
def carregar_dados():
    return pd.read_csv(URL)

Os dados são carregados via pandas.read_csv
O uso de @st.cache_data melhora a performance, evitando recarregamentos desnecessários

🔍 Filtros Interativos (Sidebar)
O dashboard possui filtros dinâmicos para:
Ano
Senioridade
Tipo de contrato
Tamanho da empres
Cargo
Remoção de outliers (percentil 99%)
Esses filtros permitem análises personalizadas e exploratórias.

🧹 Tratamento de Outliers
limite = df_filtrado['usd'].quantile(0.99)
df_filtrado = df_filtrado[df_filtrado['usd'] <= limite]
Essa opção remove salários extremamente altos que poderiam distorcer as análises.

📈 KPIs (Métricas Principais)
O dashboard exibe indicadores-chave como:
Salário médio
Salário mediano
Salário máximo
Total de registros analisados
Cargo mais frequente
Esses KPIs oferecem uma visão rápida e objetiva dos dados filtrados.

📊 Visualizações Criadas
Top 10 cargos por salário médio (gráfico de barras horizontal)
Distribuição salarial (histograma)
Proporção dos tipos de trabalho (gráfico de pizza/donut)
Mapa mundial com salário médio de Data Scientist por país
Evolução salarial ao longo dos anos (gráfico de linha)
Distribuição salarial por senioridade (boxplot)
Todas as visualizações são interativas, permitindo hover, zoom e melhor exploração dos dados.

📋 Tabela de Dados
Ao final, o dashboard exibe uma tabela com os dados filtrados, permitindo inspeção detalhada dos registros.

🚀 Como Executar o Projeto
Clone o repositório:
git clone https://github.com/seu-usuario/seu-repositorio.git

Instale as dependências:
pip install streamlit pandas plotly

Execute a aplicação:
streamlit run app.py

💡 Aprendizados

Este projeto consolidou conhecimentos importantes como:
Criação de dashboards profissionais
Análise exploratória aplicada a dados reais
Comunicação de dados através de visualizações
Uso de Python como ferramenta de tomada de decisão

✨ Considerações Finais

Este dashboard demonstra como Python e dados podem ser usados para gerar insights reais, apoiando análises estratégicas e decisões informadas na área de tecnologia.
Projeto desenvolvido como parte de uma Imersão em Python com Dados, com foco em aprendizado prático e aplicação real.
