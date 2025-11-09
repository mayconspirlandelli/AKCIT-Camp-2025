import streamlit as st

def dash2():

    # Configuração da página
    st.set_page_config(
        page_title="Dashboard Sofia",
        layout="wide"
    )

    # ======== ESTILO PERSONALIZADO ========
    st.markdown("""
    <style>
        /* Fundo branco e texto preto */
        .stApp {
            background-color: #ffffff;
            color: #000000;
        }

        /* Cabeçalho */
        h1 {
            font-size: 2.2rem !important;
            font-weight: 800 !important;
            margin-bottom: 0rem;
        }

        h2 {
            font-size: 1.5rem !important;
            font-weight: 600 !important;
            color: #333333;
            margin-top: 1rem;
            margin-bottom: 1.2rem;
        }

        /* Cards */
        .card {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 25px 30px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.08);
            border: 1px solid #f0f0f0;
            text-align: left;
        }

        .metric-value {
            font-size: 2.2rem;
            font-weight: 700;
        }

        .subtext {
            font-size: 0.9rem;
            color: #555555;
        }

        .critical {
            color: #d72638;
            font-weight: 600;
        }

        .high {
            color: #ff7b00;
            font-weight: 600;
        }

        .good {
            color: #2ca02c;
            font-weight: 700;
        }

        /* Botão no canto superior direito */
        .css-1cpxqw2 {
            position: absolute;
            right: 2rem;
            top: 1.5rem;
        }
    </style>
    """, unsafe_allow_html=True)

    # ======== CABEÇALHO ========
    col1, col2 = st.columns([6, 1])
    with col1:
        st.markdown("### Dashboard Sofia")
        st.write("Visão Executiva – Coordenador/Diretor")
    with col2:
        st.button("Visão dos Pais")

    st.markdown("---")

    # ======== SEÇÃO: AGENTE COMANDANTE ========
    st.subheader("📊 Agente Comandante – Visão Geral")

    # ======== MÉTRICAS (CARDS) ========
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="card">
            <div>Total de Alunos</div>
            <div class="metric-value">800</div>
            <div class="subtext">Ensino Médio</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div>Alunos em Risco</div>
            <div class="metric-value" style="color:#d72638;">70</div>
            <div>
                <span class="critical">23 Crítico</span> &nbsp;&nbsp;
                <span class="high">47 Alto</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <div>Em Intervenção</div>
            <div class="metric-value" style="color:#7e6bc4;">18</div>
            <div class="subtext">65% taxa de recuperação</div>
            <div style="background-color:#e6e0f8; height:6px; border-radius:3px; margin-top:5px;">
                <div style="width:65%; background-color:#7e6bc4; height:6px; border-radius:3px;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="card">
            <div>Evasão Projetada</div>
            <div class="metric-value good">2.1%</div>
            <div class="subtext">✓ Abaixo da meta (2,5%)</div>
        </div>
        """, unsafe_allow_html=True)
