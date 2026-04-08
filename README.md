# 📊 Imersao-dados-com-python2026

Dashboard interativo para análise de dados na área de tecnologia, desenvolvido com **Python, Streamlit, Pandas e Plotly**.  

O projeto foi criado durante uma imersão prática em dados, com o objetivo de transformar dados brutos em **insights visuais, interativos e acessíveis**.

---

## 🎯 Objetivo

Construir um dashboard que permita ao usuário explorar informações relevantes sobre a área de dados, como:

- 📈 Evolução salarial ao longo dos anos  
- 💼 Diferenças salariais por cargo, senioridade e tipo de contrato  
- 🌍 Distribuição geográfica de profissionais da área de dados  
- 🏠 Comparação entre trabalho remoto, híbrido e presencial  
- 📊 Distribuições e padrões salariais  

Tudo isso de forma **visual, interativa e intuitiva**.

---

## 🛠️ Tecnologias Utilizadas

- **Python**  
- **Streamlit**  
- **Pandas**  
- **Plotly Express**  
- **GitHub**  

---

## 📂 Fonte dos Dados

Os dados utilizados são públicos e foram carregados diretamente via URL:


https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv


Contêm informações como:

- Ano  
- Cargo  
- Senioridade  
- Tipo de contrato  
- Modelo de trabalho (remoto, híbrido, presencial)  
- Tamanho da empresa  
- País  
- Salário anual em USD  

---

## ⚙️ Funcionalidades do Dashboard

### 🔍 Filtros Interativos

O usuário pode filtrar os dados por:

- Ano  
- Senioridade  
- Tipo de contrato  
- Tamanho da empresa  
- Cargo  

Além disso, há opção de **remoção de outliers (percentil 99%)**, evitando distorções nas análises.

---

### 📊 KPIs (Métricas principais)

- Média salarial  
- Mediana salarial  
- Salário máximo  
- Total de registros  
- Cargo mais frequente  

---

### 📈 Visualizações

- Top 10 cargos por salário médio  
- Histograma de distribuição salarial  
- Gráfico de proporção de tipos de trabalho  
- Mapa mundial com salários por país  
- Evolução salarial ao longo do tempo  
- Boxplot por senioridade  

Todas as visualizações são **interativas (zoom, hover, filtros)**.

---

## 🚀 Como Executar o Projeto

Siga o passo a passo abaixo para rodar o dashboard na sua máquina:

1. Clone o repositório:
Bash
2. git clone https://github.com/seu-usuario/seu-repositorio.git
3. Acesse a pasta do projeto
cd seu-repositorio
4. Abra no VS Code
code(ou abra manualmente pelo VS Code)
4. Instale as dependências
pip install streamlit pandas plotly
5. Execute o projeto
streamlit run app.py
6. Acesse o dashboard

Após executar o comando, o terminal irá mostrar algo como:

Local URL: http://localhost:8501

👉 Copie esse link e cole no navegador
ou clique diretamente nele

Pronto! Seu dashboard estará rodando localmente 🎉

💡 Aprendizados

Este projeto permitiu desenvolver habilidades importantes como:

Análise exploratória de dados (EDA)
Criação de dashboards interativos
Visualização de dados com foco em tomada de decisão
Organização e apresentação de projetos de dados
✨ Considerações Finais

Este dashboard demonstra como o uso de Python e análise de dados pode gerar insights relevantes e apoiar decisões estratégicas.

Projeto desenvolvido com foco em aprendizado prático e aplicação real na área de dados.


