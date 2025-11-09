import streamlit as st

# Configurações da página
st.set_page_config(page_title="Diagnóstico Escolar", layout="wide")

# === MENU LATERAL ===
menu = st.sidebar.radio(
    "Navegação",
    ["📂 Upload de Arquivo", "🤖 Agente de IA"]
)

# === TELA 1: UPLOAD ===
if menu == "📂 Upload de Arquivo":
    st.title("📂 Upload de Arquivo")
    uploaded_file = st.file_uploader("Envie seu arquivo CSV para análise", type=["csv"])
    
    if uploaded_file is not None:
        st.success("Arquivo carregado com sucesso!")
        st.write("Nome do arquivo:", uploaded_file.name)

# === TELA 2: AGENTE DE IA ===
elif menu == "🤖 Agente de IA":
    st.title("🤖 Agente de IA")
    st.write("Esta área será usada para interagir com o agente de IA.")
    
    user_input = st.text_area("Digite sua pergunta:")
    if st.button("Enviar"):
        if user_input.strip():
            st.info(f"Agente de IA: (resposta simulada para '{user_input}')")
        else:
            st.warning("Por favor, digite uma pergunta antes de enviar.")
