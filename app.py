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
    st.write("🔗 [LinkedIn: in/sammya-ferreira](https://linkedin.com/in/sammya-ferreira)")
    st.write("📫 sammyacaroline90@gmail.com")
    st.write("📞 [(98) 98451-1565](https://wa.me/5598984511565)")
    st.write("📍 Paço do Lumiar, Maranhão")

# --- RESUMO PROFISSIONAL ---
st.header("Resumo Profissional")

# Usamos o markdown para formatar o texto em negrito
st.markdown(
    """
    Profissional formada em **Análise e Desenvolvimento de Sistemas**  com sólida experiência em otimizar processos 
    no varejo. Minha paixão é entender necessidades para desenhar e implementar soluções tecnológicas. 
    Ao longo da minha carreira, transformei números em estratégias , liderei equipes focadas em resultados e evoluí da criação de relatórios em Excel para o desenvolvimento de dashboards interativos em **Power BI**. 
    Busco uma oportunidade onde eu possa unir minha visão de negócio com minha capacidade de analista e 
    desenvolvedora para criar ou sugerir ferramentas que realmente impulsionam pessoas e empresas.
    """
)

# --- EXPERIÊNCIA PROFISSIONAL ---
st.write("---") # Linha divisória
st.header("Experiência Profissional")

# --- BLOCO 1: CONSULTORA AUTÔNOMA ---
with st.expander("**Consultora de Vendas e Empreendedora** - (2024 - Atualmente)"):
    st.markdown(
        """
        - **Gestão Comercial e Vendas Multicanal:** Realizo a prospecção ativa e consultoria de vendas 
        personalizada para produtos de maquiagem e confecções, utilizando canais presenciais, 
        redes sociais para marketing e engajamento, e uma rede de indicações para expansão da base de clientes.
        """
    )
    st.success(
        """
        **Diferencial:** Analisei a necessidade do negócio e desenvolvi uma solução customizada para gestão 
        de inventário e controle financeiro. O sistema permite o monitoramento do fluxo de caixa, 
        análise de margem de lucro por produto e otimização do controle de estoque, resultando em 
        melhor tomada de decisão e saúde financeira da atividade.
        """
    )

# --- BLOCO 2: ALGOR CERTIFICAÇÃO DIGITAL ---
with st.expander("**Agente de Registro / Assistente Comercial** - Algor Certificação Digital (2019)"):
    st.markdown(
        """
        Nesta posição, avancei da análise em planilhas para a estruturação de dashboards em Excel, 
        monitorando a performance regional para apoiar decisões estratégicas, com foco no 
        relacionamento com parceiros e na expansão da carteira de clientes.
        """
    )
    data_clientes = {
        'Período': ['Início 2019', 'Final 2019'], 'Número de Clientes Ativos': [121, 177]
    }
    df_clientes = pd.DataFrame(data_clientes)
    fig_clientes = px.bar(
        df_clientes, x='Período', y='Número de Clientes Ativos',
        title='Crescimento da Base de Clientes Ativos em 2019', text_auto=True
    )
    
    # Linha abaixo foi alterada
    st.plotly_chart(fig_clientes, use_container_width=True, config={'staticPlot': True})

    st.success(
        """
        **Resultado:** O estabelecimento e fortalecimento do relacionamento com escritórios contábeis 
        resultou em uma significativa expansão da base de clientes ativos.
        """
    )

# --- BLOCO 3: LEITURA SLZ ---
with st.expander("**Coordenadora de Loja / Encarregada de Setor** - Leitura SLZ (2014-2017)"):
    st.markdown(
        """
        - **Gestão de Processos e Equipe:** Liderei equipes e otimizei processos de vendas e estoque. Uma das minhas principais contribuições foi a reestruturação do controle de inventário para reduzir perdas.
        - **Otimização do Processo de Checkout:** Para resolver a lentidão causada pela digitação manual de produtos sem código de barras, desenvolvi um sistema de códigos de barras avulsos. A iniciativa agilizou o atendimento no caixa e melhorou significativamente a experiência do cliente.
        """
    )
    data_ruptura = {
        'Ano': ['2015', '2016', '2017'], 'Índice de Ruptura (%)': [12.5, 8.2, 5.1]
    }
    df_ruptura = pd.DataFrame(data_ruptura)

    # ... (código que cria o df_ruptura) ...
    fig_ruptura = px.line(
        df_ruptura, x='Ano', y='Índice de Ruptura (%)',
        title='Redução Progressiva nas Rupturas de Estoque', markers=True, text='Índice de Ruptura (%)'
    )
    fig_ruptura.update_traces(textposition="top center")
    
    # Linha abaixo foi alterada
    st.plotly_chart(fig_ruptura, use_container_width=True, config={'staticPlot': True})

    st.success(
        """
        **Resultado:** A reestruturação de controles e processos proporcionou uma 
        redução significativa nas rupturas de produtos, garantindo maior disponibilidade de 
        itens-chave e agilidade no atendimento ao cliente.
        """
    )

# --- BLOCOS RESTANTES ---
with st.expander("**Líder de Crédito e Crediário** - Esplanada Brasil LTDA (2012 - 2013)"):
    st.markdown(
        """
        - Coordenei o setor de crédito, acompanhando relatórios de inadimplência e promovendo estratégias de negociação.
        - Elaborei metas mensais e campanhas promocionais que contribuíram para o crescimento do faturamento da unidade.
        - Desenvolvi relatórios analíticos para acompanhar o desempenho da equipe e auxiliar os gestores na tomada de decisão.
        """
    )

with st.expander("**Assistente Administrativo** - Padrão de Vida Corretora de Seguros (2011)"):
    st.markdown(
        """
        - Fui responsável pela organização de propostas comerciais e pela formalização documental, garantindo maior agilidade nos processos.
        - Atuei no suporte direto à equipe comercial, realizando atualização de cadastros e acompanhamento de contratos de clientes.
        """
    )

with st.expander("**Menor Aprendiz Administrativo** - Losango Promoções de Venda (2009 - 2011)"):
    st.markdown(
        """
        - Apoiei o setor administrativo com elaboração de relatórios e planilhas, desenvolvendo desde cedo práticas de organização e análise de dados.
        - Prestei suporte no atendimento ao cliente e lojistas, auxiliando em processos de cobrança e controle de transações financeiras.
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
        'Google Workspace', 'Power BI (Modelagem, Relatórios)',  # Avançado
        'Pacote Office', 'Excel (Dashboards, KPIs)',  # Intermediário
        'SQL (Básico)', 'Python',   # Em aprendizado
    ],
    'Nível': [
        'Avançado', 'Avançado',
        'Intermediário', 'Intermediário',
        'Em Aprendizado', 'Em Aprendizado'
    ],
    'Valor': [80, 80, 65, 50, 40, 30] # Valores numéricos para ordenar o gráfico
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
    textposition='outside',
    marker_color='#1f77b4'
)

# Linha abaixo foi alterada
st.plotly_chart(fig_habilidades, use_container_width=True, config={'staticPlot': True})

# --- CERTIFICAÇÕES ---
st.write("---")
st.header("Certificações")

# Usando colunas para organizar as certificações
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("🏅 **Software Architect / Mobile Developer - Gran Centro Universitário (357h)**")
    st.markdown("🏅 **Full Stack, Back-End e Front-End Developer - Gran Centro Universitário (340h)**")
    st.markdown("🏅 **Back-End Developer/ Process Mapping Analyst - Gran Centro Universitário (320h)**")
    st.markdown("🏅 **Data Administrator/ Project Manager - Gran Centro Universitário (380h)**")
    st.markdown("🏅 **Hands-on Professional/ Front-end Developer - Gran Centro Universitário (340h)**")

with col2:
    st.markdown("🏅 **Power BI - Fundação CECIERJ (180h)**")
    st.markdown("🏅 **Microsoft Office - Delta Informática**")
    st.markdown("🏅 **Liderança e Vendas - Losango**")
    st.markdown("🏅 **Marketing e Secretariado - CIEE**")

# --- RODAPÉ ---
st.write("---") # Linha divisória
st.markdown("© 2025 SCOF. Todos os direitos reservados.")
