import streamlit as st
import pandas as pd
import time

def upload():
    # Tema personalizado: fundo branco e texto/interface em preto
    # st.markdown("""
    #     <style>
    #     /* Cor de fundo geral */
    #     .stApp {
    #         background-color: white;
    #         color: black;
    #     }

    #     /* Cor de fundo dos cards e widgets */
    #     div[data-testid="stMetricValue"], 
    #     div[data-testid="stMetricLabel"], 
    #     .stButton>button, .stSelectbox, .stTextInput>div>div>input,
    #     .stDownloadButton>button {
    #         color: black !important;
    #     }

    #     /* Caixas, métricas e títulos */
    #     h1, h2, h3, h4, h5, h6, p, label, span {
    #         color: black !important;
    #     }

    #     /* Remover sombras e bordas escuras do modo noturno */
    #     .stMarkdown, .stDataFrame, .stPlotlyChart, .stFile_uploader {
    #         background-color: white !important;
    #         color: black !important;
    #     }

    #     /* Alterar cor de fundo de containers */
    #     .block-container {
    #         background-color: white;
    #     }


    #     </style>
    # """, unsafe_allow_html=True)

    # Configuração da página
    st.set_page_config(
        page_title="Upload de Arquivo",
        page_icon="📁",
        layout="centered"
    )

    # Título da aplicação
    st.title("📁 Upload de Arquivos")
    st.markdown("---")

    # Descrição
    st.markdown("""
    ### Instruções:
    - Faça upload de um arquivo **CSV** ou **Excel** (.xlsx, .xls)
    - O sistema processará automaticamente o arquivo
    - Você verá o progresso do carregamento em tempo real
    """)

    st.markdown("---")

    # Área de upload
    uploaded_file = st.file_uploader(
        "Escolha um arquivo",
        type=['csv', 'xlsx', 'xls'],
        help="Formatos aceitos: CSV, Excel (.xlsx, .xls)"
    )

    # Processar arquivo quando uploaded
    if uploaded_file is not None:
        
        # Informações do arquivo
        st.info(f"📄 **Arquivo selecionado:** {uploaded_file.name}")
        st.info(f"📊 **Tamanho:** {uploaded_file.size / 1024:.2f} KB")
        
        # Container para barra de progresso
        progress_container = st.container()
        
        with progress_container:
            st.markdown("### 🔄 Processando arquivo...")
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                # Simular etapas de carregamento
                status_text.text("⏳ Iniciando leitura do arquivo...")
                time.sleep(0.3)
                progress_bar.progress(20)
                
                # Determinar tipo de arquivo e ler
                file_extension = uploaded_file.name.split('.')[-1].lower()
                
                status_text.text("📖 Lendo dados do arquivo...")
                time.sleep(0.4)
                progress_bar.progress(40)
                
                if file_extension == 'csv':
                    df = pd.read_csv(uploaded_file)
                elif file_extension in ['xlsx', 'xls']:
                    df = pd.read_excel(uploaded_file)
                
                progress_bar.progress(60)
                status_text.text("🔍 Validando dados...")
                time.sleep(0.3)
                
                # Validações básicas
                if df.empty:
                    raise ValueError("O arquivo está vazio!")
                
                progress_bar.progress(80)
                status_text.text("✨ Finalizando processamento...")
                time.sleep(0.3)
                
                progress_bar.progress(100)
                time.sleep(0.2)
                
                # Limpar mensagens de progresso
                progress_bar.empty()
                status_text.empty()
                
                # Mensagem de sucesso
                st.success("✅ **Arquivo carregado com sucesso!**")

            
            except pd.errors.EmptyDataError:
                progress_bar.empty()
                status_text.empty()
                st.error("❌ **Erro:** O arquivo está vazio ou não contém dados válidos!")
                
            except pd.errors.ParserError:
                progress_bar.empty()
                status_text.empty()
                st.error("❌ **Erro:** Não foi possível interpretar o arquivo. Verifique se o formato está correto!")
                
            except ValueError as ve:
                progress_bar.empty()
                status_text.empty()
                st.error(f"❌ **Erro de Validação:** {str(ve)}")
                
            except Exception as e:
                progress_bar.empty()
                status_text.empty()
                st.error(f"❌ **Erro ao processar o arquivo:** {str(e)}")
                st.error("Por favor, verifique se o arquivo está no formato correto e tente novamente.")
                
                # Mostrar detalhes técnicos em expander
                with st.expander("🔧 Ver detalhes técnicos do erro"):
                    st.code(str(e))

    else:
        # Mensagem quando nenhum arquivo foi carregado
        st.info("👆 Por favor, selecione um arquivo para começar")
        
        # Exemplo de formato esperado
        with st.expander("📚 Ver exemplo de formato esperado"):
            st.markdown("""
            **Formato CSV:**
            ```
            Nome,Idade,Cidade
            João,25,São Paulo
            Maria,30,Rio de Janeiro
            ```
            
            **Formato Excel:**
            - Deve conter pelo menos uma planilha com dados
            - Primeira linha deve conter os cabeçalhos das colunas
            """)

    # Rodapé
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <small>💡 Dica: Arquivos muito grandes podem levar mais tempo para processar</small>
    </div>
    """, unsafe_allow_html=True)