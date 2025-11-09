import streamlit as st
from upload import upload
from dashboard import dashboard
from dash2 import dash2

# Configurações da página
st.set_page_config(page_title="Diagnóstico Escolar", layout="wide")

# === MENU LATERAL ===
menu = st.sidebar.radio(
    "Navegação",
    ["📂 Upload de Arquivo", "🤖 Dashborad"]
)

# === ROTAS ===
if menu == "📂 Upload de Arquivo":
    upload()
elif menu == "🤖 Dashborad":
    dash2()

