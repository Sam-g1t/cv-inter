# Importando as bibliotecas para o gráfico
import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Sammya Ferreira | Desenvolvedora & Analista de Dados",
    page_icon="👩‍💻",
    layout="wide" # Usa a largura total da página
)

# --- CABEÇALHO ---
# Usando colunas para organizar a foto e o texto
col1, col2 = st.columns([1, 2.5], gap="medium") # A segunda coluna é 2.5x maior que a primeira

with col1:
    st.image("perfil.jpg", width=230) # Carrega sua foto

with col2:
    st.title("Sammya Caroline de Oliveira Ferreira")
    st.write("**Arquiteta de Soluções: unindo Desenvolvimento de Sistemas e Análise de Dados**")
    
    # Frase de impacto com um pouco de estilo
    st.markdown(
        """
        <div style="background-color: #f0f2f6; padding: 15px; border-radius: 10px;">
        <em>
        "Minha carreira é sobre encontrar a ferramenta certa para cada desafio. 
        Do Controle de Estoque em Excel ao Desenvolvimento de Sistemas, meu objetivo é 
        construir e sugerir soluções que tornam o trabalho mais inteligente e os resultados mais claros."
        </em>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    st.write("---") # Linha divisória
    
    # Informações de Contato ATUALIZADAS
    st.write("📫 sammyacaroline90@gmail.com")
    st.write("📞 [(98) 98451-1565](https://wa.me/5598984511565)")
    st.write("📍 Paço do Lumiar, Maranhão")
    st.write("🔗 [LinkedIn: in/sammya-ferreira](https://linkedin.com/in/sammya-ferreira)")


# --- RESUMO PROFISSIONAL ---
st.header("Resumo Profissional")

# Usamos o markdown para formatar o texto em negrito
st.markdown(
    """
    Profissional formada em **Análise e Desenvolvimento de Sistemas**  com sólida experiência em otimizar processos 
    no varejo. Minha paixão é entender necessidades para desenhar e implementar soluções tecnológicas. 
    Ao longo da minha carreira, transformei números em estratégias , liderei equipes focadas em resultados e evoluí da criação de relatórios em Excel para o desenvolvimento de dashboards interativos em **Power BI**. 
    Busco uma oportunidade onde eu possa unir minha visão de negócio com minha capacidade de analista e 
    desenvolvedora para criar e sugerir sistemas que realmente impulsionam pessoas e empresas.
    """
)

# --- EXPERIÊNCIA PROFISSIONAL ---
st.write("---") # Linha divisória
st.header("Experiência Profissional")

# --- BLOCO 1: LEITURA SLZ ---
st.subheader("Coordenadora de Loja / Encarregada de Setor - Leitura SLZ (2014-2018)")
st.markdown(
    """
    Nesta função, liderei equipes e otimizei processos de vendas e estoque. 
    Uma das minhas principais contribuições foi a reestruturação do controle de inventário, 
    que teve um impacto direto na disponibilidade dos produtos para os clientes.
    """
)

# Criando dados simulados para o gráfico de rupturas
# O objetivo é mostrar uma tendência de queda, representando o resultado do seu trabalho
data = {
    'Ano': ['2015', '2016', '2017', '2018'],
    'Índice de Ruptura (%)': [12.5, 8.2, 5.1, 3.4] # Números simulados mostrando a queda
}
df_ruptura = pd.DataFrame(data)

# Criando o gráfico de linhas com Plotly Express
fig_ruptura = px.line(
    df_ruptura,
    x='Ano',
    y='Índice de Ruptura (%)',
    title='Redução Progressiva nas Rupturas de Estoque',
    markers=True, # Adiciona marcadores nos pontos de dados
    text='Índice de Ruptura (%)' # Mostra o valor no gráfico
)

# Configurando detalhes do gráfico para ficar mais claro
fig_ruptura.update_traces(textposition="top center")
fig_ruptura.update_layout(
    xaxis_title="Ano de Atuação",
    yaxis_title="Percentual de Ruptura"
)

# Mostrando o gráfico na página
st.plotly_chart(fig_ruptura, use_container_width=True)

st.success(
    """
    **Resultado:** A estruturação de um controle de estoque mais detalhado em Excel proporcionou uma 
    redução significativa nas rupturas de produtos, garantindo maior disponibilidade de 
    itens-chave para o cliente. 
    """
)

# --- BLOCO 2: ALGOR CERTIFICAÇÃO DIGITAL ---
st.subheader("Agente de Registro / Assistente Comercial - Algor Certificação Digital (2019 - 2021)")
st.markdown(
    """
    Nesta posição, avancei da análise em planilhas para a estruturação de dashboards em Excel, 
    monitorando a performance regional para apoiar decisões estratégicas. Meu foco principal era no 
    relacionamento com parceiros e na expansão da nossa carteira de clientes.
    """
)

# Criando dados simulados para o gráfico de expansão de clientes
data_clientes = {
    'Período': ['Início do Projeto (2019)', 'Final do Projeto (2021)'],
    'Número de Clientes Ativos': [85, 250] # Números simulados mostrando forte crescimento
}
df_clientes = pd.DataFrame(data_clientes)

# Criando o gráfico de barras com Plotly Express
fig_clientes = px.bar(
    df_clientes,
    x='Período',
    y='Número de Clientes Ativos',
    title='Crescimento da Base de Clientes Ativos',
    text_auto=True # Adiciona os valores diretamente nas barras
)

# Configurando detalhes do gráfico
fig_clientes.update_layout(
    xaxis_title="Período de Atuação",
    yaxis_title="Clientes Ativos"
)

# Mostrando o gráfico na página
st.plotly_chart(fig_clientes, use_container_width=True)

st.success(
    """
    **Resultado:** O estabelecimento e fortalecimento do relacionamento com escritórios contábeis 
    resultou em uma significativa expansão da base de clientes ativos em menos de dois anos.
    """
)

# --- BLOCO 3: EXPERIÊNCIAS ANTERIORES ---
st.subheader("Outras Experiências que Formaram Minha Base")

# Usando st.expander com títulos em negrito (Markdown)
with st.expander("**Líder de Crédito e Crediário** - Esplanada Brasil LTDA (2012 - 2013)"):
    st.markdown(
        """
        - Coordenei o setor de crédito, acompanhando relatórios de inadimplência e promovendo estratégias de negociação. 
        - Elaborei metas mensais e campanhas promocionais que contribuíram para o crescimento do faturamento da unidade. 
        - Desenvolvi relatórios analíticos para acompanhar o desempenho da equipe e auxiliar os gestores na tomada de decisão.
        """
    )

with st.expander("**Assistente Administrativo** - Padrão de Vida Corretora de Seguros (2011-2012)"):
    st.markdown(
        """
        - Fui responsável pela organização de propostas comerciais e pela formalização documental, garantindo maior agilidade nos processos.
        - Atuei no suporte direto à equipe comercial, realizando atualização de cadastros e acompanhamento de contratos de clientes.
        - Contribuí para a fidelização de clientes com um atendimento mais humanizado e próximo.
        """
    )

with st.expander("**Menor Aprendiz Administrativo** - Losango Promoções de Venda (2009 - 2011)"):
    st.markdown(
        """
        - Apoiei o setor administrativo com elaboração de relatórios e planilhas, desenvolvendo desde cedo práticas de organização e análise de dados.
        - Prestei suporte no atendimento ao cliente e lojistas, auxiliando em processos de cobrança e controle de transações financeiras.
        - Essa experiência foi fundamental para consolidar minha disciplina, adaptabilidade e interesse em rotinas administrativas e analíticas.
        """
    )

# --- FORMAÇÃO ACADÊMICA ---
st.write("---")
st.header("Formação Acadêmica")

# Usando colunas para organizar a formação
col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("Tecnólogo em Análise e Desenvolvimento de Sistemas")
    st.markdown("🎓 *Gran Centro Universitário*")
    st.write("Concluído em Agosto/2025") # 

with col2:
    st.subheader("Licenciatura em Matemática")
    st.markdown("🎓 *Universidade Federal do Maranhão*")
    st.write("Previsão de término: Janeiro/2028") # 


# --- HABILIDADES TÉCNICAS ---
st.write("---")
st.header("Habilidades Técnicas")

# Criando dados para o gráfico de habilidades
dados_habilidades = {
    'Habilidade': [
        'Power BI (Modelagem, Relatórios)', 'Google Workspace',  # Avançado
        'Pacote Office', 'Excel (Dashboards, KPIs)',  # Intermediário
        'Python', 'SQL (Básico)',  # Em aprendizado
    ],
    'Nível': [
        'Avançado', 'Avançado',
        'Intermediário', 'Intermediário', 'Intermediário',
        'Em Aprendizado'
    ],
    'Valor': [90, 90, 50, 65, 70, 30] # Valores numéricos para ordenar o gráfico
}
df_habilidades = pd.DataFrame(dados_habilidades)

# Criando o gráfico de barras horizontais
fig_habilidades = px.bar(
    df_habilidades.sort_values(by='Valor', ascending=True), # Ordena as barras
    x='Valor',
    y='Habilidade',
    orientation='h', # Gráfico horizontal
    text='Nível', # Texto que aparece na barra
    title='Nível de Proficiência'
)

# Configurando o layout do gráfico
fig_habilidades.update_layout(
    xaxis_title="", # Remove o título do eixo X
    yaxis_title="", # Remove o título do eixo Y
    showlegend=False, # Esconde a legenda
    xaxis=dict(showticklabels=False), # Esconde os números do eixo X
    height=400,
)
fig_habilidades.update_traces(
    textposition='outside', # Posição do texto
    marker_color='#1f77b4'  # Cor das barras
)

st.plotly_chart(fig_habilidades, use_container_width=True)

# --- CERTIFICAÇÕES ---
st.write("---")
st.header("Certificações")

# Usando colunas para organizar as certificações
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("🏅 **Software Architect / Mobile Developer - Gran Centro Universitário (357h)**")
    st.markdown("🏅 **Full Stack, Back-End e Front-End Developer - Gran Centro Universitário (340h)**")
    st.markdown("🏅 **Back-End Developer/ Process Mapping Analyst - Gran Centro Universitário (320h)**")
    st.markdown("🏅 **Data Administrator/ Project Manager - Gran Centro Universitário (30h)**")
    st.markdown("🏅 **Hands-on Professional/ Front-end Developer - Gran Centro Universitário (340h)**")

with col2:
    st.markdown("🏅 **Power BI - Fundação CECIERJ (180h)**")
    st.markdown("🏅 **Microsoft Office - Delta Informática**")
    st.markdown("🏅 **Liderança e Vendas - Losango**")
    st.markdown("🏅 **Marketing e Secretariado - CIEE**")

# --- RODAPÉ ---
st.write("---") # Linha divisória
st.markdown("© 2025 Sammya Caroline de Oliveira Ferreira. Todos os direitos reservados.")
 