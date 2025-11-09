import streamlit as st
import plotly.graph_objects as go
import pandas as pd


def dash2():

    # # Configuração da página
    # st.set_page_config(
    #     page_title="Dashboard Sofia",
    #     layout="wide"
    # )

    # # ======== ESTILO PERSONALIZADO ========
    # st.markdown("""
    # <style>
    #     /* Fundo branco e texto preto */
    #     .stApp {
    #         background-color: #ffffff;
    #         color: #000000;
    #     }

    #     /* Cabeçalho */
    #     h1 {
    #         font-size: 2.2rem !important;
    #         font-weight: 800 !important;
    #         margin-bottom: 0rem;
    #     }

    #     h2 {
    #         font-size: 1.5rem !important;
    #         font-weight: 600 !important;
    #         color: #333333;
    #         margin-top: 1rem;
    #         margin-bottom: 1.2rem;
    #     }

    #     /* Cards */
    #     .card {
    #         background-color: #ffffff;
    #         border-radius: 12px;
    #         padding: 25px 30px;
    #         box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    #         border: 1px solid #f0f0f0;
    #         text-align: left;
    #     }

    #     .metric-value {
    #         font-size: 2.2rem;
    #         font-weight: 700;
    #     }

    #     .subtext {
    #         font-size: 0.9rem;
    #         color: #555555;
    #     }

    #     .critical {
    #         color: #d72638;
    #         font-weight: 600;
    #     }

    #     .high {
    #         color: #ff7b00;
    #         font-weight: 600;
    #     }

    #     .good {
    #         color: #2ca02c;
    #         font-weight: 700;
    #     }

    #     /* Botão no canto superior direito */
    #     .css-1cpxqw2 {
    #         position: absolute;
    #         right: 2rem;
    #         top: 1.5rem;
    #     }
    # </style>
    # """, unsafe_allow_html=True)

    # # ======== CABEÇALHO ========
    # col1, col2 = st.columns([6, 1])
    # with col1:
    #     st.markdown("### Dashboard Sofia")
    #     st.write("Visão Executiva – Coordenador/Diretor")
    # with col2:
    #     st.button("Visão dos Pais")

    # st.markdown("---")

    # # ======== SEÇÃO: AGENTE COMANDANTE ========
    # st.subheader("📊 Agente Comandante – Visão Geral")

    # # ======== MÉTRICAS (CARDS) ========
    # col1, col2, col3, col4 = st.columns(4)

    # with col1:
    #     st.markdown("""
    #     <div class="card">
    #         <div>Total de Alunos</div>
    #         <div class="metric-value">800</div>
    #         <div class="subtext">Ensino Médio</div>
    #     </div>
    #     """, unsafe_allow_html=True)

    # with col2:
    #     st.markdown("""
    #     <div class="card">
    #         <div>Alunos em Risco</div>
    #         <div class="metric-value" style="color:#d72638;">70</div>
    #         <div>
    #             <span class="critical">23 Crítico</span> &nbsp;&nbsp;
    #             <span class="high">47 Alto</span>
    #         </div>
    #     </div>
    #     """, unsafe_allow_html=True)

    # with col3:
    #     st.markdown("""
    #     <div class="card">
    #         <div>Em Intervenção</div>
    #         <div class="metric-value" style="color:#7e6bc4;">18</div>
    #         <div class="subtext">65% taxa de recuperação</div>
    #         <div style="background-color:#e6e0f8; height:6px; border-radius:3px; margin-top:5px;">
    #             <div style="width:65%; background-color:#7e6bc4; height:6px; border-radius:3px;"></div>
    #         </div>
    #     </div>
    #     """, unsafe_allow_html=True)

    # with col4:
    #     st.markdown("""
    #     <div class="card">
    #         <div>Evasão Projetada</div>
    #         <div class="metric-value good">2.1%</div>
    #         <div class="subtext">✓ Abaixo da meta (2,5%)</div>
    #     </div>
    #     """, unsafe_allow_html=True)




    #     # import streamlit as st
        # import plotly.graph_objects as go
        # import pandas as pd

        # ===================== CONFIGURAÇÃO DA PÁGINA =====================
        st.set_page_config(
            page_title="Dashboard Sofia",
            layout="wide"
        )

        # ===================== ESTILO PERSONALIZADO =====================
        st.markdown("""
        <style>
            .stApp {
                background-color: #ffffff;
                color: #000000;
            }

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

            .critical { color: #d72638; font-weight: 600; }
            .high { color: #ff7b00; font-weight: 600; }
            .good { color: #2ca02c; font-weight: 700; }

            .css-1cpxqw2 {
                position: absolute;
                right: 2rem;
                top: 1.5rem;
            }
        </style>
        """, unsafe_allow_html=True)

        # ===================== CABEÇALHO =====================
        col1, col2 = st.columns([6, 1])
        with col1:
            st.markdown("### Dashboard Sofia")
            st.write("Visão Executiva – Coordenador/Diretor")
        with col2:
            st.button("Visão dos Pais")

        st.markdown("---")

        # ===================== SEÇÃO: AGENTE COMANDANTE =====================
        st.subheader("📊 Agente Comandante – Visão Geral")

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

        # ===================== GRÁFICO 1: EVOLUÇÃO SEMANAL =====================
        st.markdown("### 📈 Evolução Semanal")
        st.write("Acompanhamento de alunos em risco e recuperação")

        # Dados de exemplo
        semanas = ["Sem 1", "Sem 2", "Sem 3", "Sem 4"]
        alunos_risco = [28, 26, 24, 23]
        em_intervencao = [10, 13, 15, 16]
        recuperados = [0, 5, 9, 14]

        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=semanas, y=alunos_risco, mode='lines+markers',
                                name="Alunos em Risco", line=dict(color="#d72638", width=2)))
        fig1.add_trace(go.Scatter(x=semanas, y=em_intervencao, mode='lines+markers',
                                name="Em Intervenção", line=dict(color="#9b8bc2", width=2)))
        fig1.add_trace(go.Scatter(x=semanas, y=recuperados, mode='lines+markers',
                                name="Recuperados", line=dict(color="#2ca02c", width=2)))

        fig1.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            margin=dict(l=20, r=20, t=20, b=20),
            legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5),
            xaxis=dict(showgrid=True, gridcolor="#f0f0f0"),
            yaxis=dict(showgrid=True, gridcolor="#f0f0f0"),
        )
        st.plotly_chart(fig1, use_container_width=True)

        # ===================== GRÁFICO 2: DISTRIBUIÇÃO DE RISCO =====================
        st.markdown("### 📊 Distribuição de Risco por Série")
        st.write("Identificação de séries com maior concentração de risco")

        # Dados de exemplo
        series = ["9º Ano", "1º EM", "2º EM", "3º EM"]
        critico = [5, 10, 4, 3]
        alto = [8, 20, 9, 7]
        medio = [15, 35, 20, 15]

        fig2 = go.Figure(data=[
            go.Bar(name='Crítico', x=series, y=critico, marker_color='#d72638'),
            go.Bar(name='Alto', x=series, y=alto, marker_color='#ff7b00'),
            go.Bar(name='Médio', x=series, y=medio, marker_color='#f5c242')
        ])

        fig2.update_layout(
            barmode='group',
            plot_bgcolor='white',
            paper_bgcolor='white',
            margin=dict(l=20, r=20, t=20, b=20),
            legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5),
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor="#f0f0f0"),
        )
        st.plotly_chart(fig2, use_container_width=True)
