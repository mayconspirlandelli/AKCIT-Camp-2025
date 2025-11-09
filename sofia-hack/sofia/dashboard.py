import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def dashboard():

        # Configuração da página
        st.set_page_config(page_title="Dashboard de Evasão Escolar", layout="wide", page_icon="🎓")

        # Título
        st.title("🎓 Dashboard de Diagnóstico de Evasão Escolar")
        st.markdown("---")

        # Função para gerar dados de exemplo
        @st.cache_data
        def gerar_dados_exemplo():
            np.random.seed(42)
            n = 500
            
            data = {
                'ID_Aluno': range(1, n+1),
                'Idade': np.random.randint(14, 19, n),
                'Serie': np.random.choice(['1º Ano', '2º Ano', '3º Ano'], n),
                'Genero': np.random.choice(['Masculino', 'Feminino'], n),
                'Nota_Media': np.random.uniform(3, 10, n),
                'Faltas': np.random.poisson(15, n),
                'Renda_Familiar': np.random.choice(['Baixa', 'Média', 'Alta'], n, p=[0.4, 0.4, 0.2]),
                'Distancia_Escola_km': np.random.uniform(0.5, 15, n),
                'Participacao_Atividades': np.random.choice(['Baixa', 'Média', 'Alta'], n),
                'Apoio_Familiar': np.random.choice(['Baixo', 'Médio', 'Alto'], n),
                'Status': np.random.choice(['Ativo', 'Em Risco', 'Evadido'], n, p=[0.6, 0.25, 0.15])
            }
            
            df = pd.DataFrame(data)
            
            # Ajustar probabilidades baseadas em fatores
            for idx in df.index:
                if df.loc[idx, 'Faltas'] > 25 or df.loc[idx, 'Nota_Media'] < 5:
                    df.loc[idx, 'Status'] = np.random.choice(['Em Risco', 'Evadido'], p=[0.6, 0.4])
                elif df.loc[idx, 'Faltas'] < 10 and df.loc[idx, 'Nota_Media'] > 7:
                    df.loc[idx, 'Status'] = 'Ativo'
            
            return df

        df = gerar_dados_exemplo()

        # Sidebar com filtros
        st.sidebar.header("🔍 Filtros")
        serie_selecionada = st.sidebar.multiselect(
            "Série:",
            options=df['Serie'].unique(),
            default=df['Serie'].unique()
        )

        status_selecionado = st.sidebar.multiselect(
            "Status:",
            options=df['Status'].unique(),
            default=df['Status'].unique()
        )

        renda_selecionada = st.sidebar.multiselect(
            "Renda Familiar:",
            options=df['Renda_Familiar'].unique(),
            default=df['Renda_Familiar'].unique()
        )

        # Filtrar dados
        df_filtrado = df[
            (df['Serie'].isin(serie_selecionada)) &
            (df['Status'].isin(status_selecionado)) &
            (df['Renda_Familiar'].isin(renda_selecionada))
        ]

        # Métricas principais
        st.header("📊 Indicadores Principais")
        col1, col2, col3, col4 = st.columns(4)

        total_alunos = len(df_filtrado)
        alunos_ativos = len(df_filtrado[df_filtrado['Status'] == 'Ativo'])
        alunos_risco = len(df_filtrado[df_filtrado['Status'] == 'Em Risco'])
        alunos_evadidos = len(df_filtrado[df_filtrado['Status'] == 'Evadido'])

        col1.metric("Total de Alunos", total_alunos)
        col2.metric("Alunos Ativos", alunos_ativos, f"{(alunos_ativos/total_alunos*100):.1f}%")
        col3.metric("Alunos em Risco", alunos_risco, f"{(alunos_risco/total_alunos*100):.1f}%", delta_color="inverse")
        col4.metric("Alunos Evadidos", alunos_evadidos, f"{(alunos_evadidos/total_alunos*100):.1f}%", delta_color="inverse")

        st.markdown("---")

        # Gráficos principais
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📈 Distribuição por Status")
            status_counts = df_filtrado['Status'].value_counts()
            cores_status = {'Ativo': '#2ecc71', 'Em Risco': '#f39c12', 'Evadido': '#e74c3c'}
            
            fig1 = px.pie(
                values=status_counts.values,
                names=status_counts.index,
                color=status_counts.index,
                color_discrete_map=cores_status,
                hole=0.4
            )
            fig1.update_traces(textposition='inside', textinfo='percent+label')
            fig1.update_layout(showlegend=True, height=400)
            st.plotly_chart(fig1, use_container_width=True)

        with col2:
            st.subheader("📚 Status por Série")
            status_serie = df_filtrado.groupby(['Serie', 'Status']).size().reset_index(name='Quantidade')
            
            fig2 = px.bar(
                status_serie,
                x='Serie',
                y='Quantidade',
                color='Status',
                color_discrete_map=cores_status,
                barmode='group'
            )
            fig2.update_layout(height=400)
            st.plotly_chart(fig2, use_container_width=True)

        # Análise de fatores de risco
        st.markdown("---")
        st.header("🎯 Análise de Fatores de Risco")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📉 Notas Médias por Status")
            fig3 = px.box(
                df_filtrado,
                x='Status',
                y='Nota_Media',
                color='Status',
                color_discrete_map=cores_status
            )
            fig3.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig3, use_container_width=True)

        with col2:
            st.subheader("🚫 Faltas por Status")
            fig4 = px.box(
                df_filtrado,
                x='Status',
                y='Faltas',
                color='Status',
                color_discrete_map=cores_status
            )
            fig4.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig4, use_container_width=True)

        # Análise socioeconômica
        st.markdown("---")
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("💰 Status por Renda Familiar")
            renda_status = df_filtrado.groupby(['Renda_Familiar', 'Status']).size().reset_index(name='Quantidade')
            
            fig5 = px.bar(
                renda_status,
                x='Renda_Familiar',
                y='Quantidade',
                color='Status',
                color_discrete_map=cores_status,
                barmode='stack'
            )
            fig5.update_layout(height=400)
            st.plotly_chart(fig5, use_container_width=True)

        with col2:
            st.subheader("🏃 Participação em Atividades")
            part_status = df_filtrado.groupby(['Participacao_Atividades', 'Status']).size().reset_index(name='Quantidade')
            
            fig6 = px.bar(
                part_status,
                x='Participacao_Atividades',
                y='Quantidade',
                color='Status',
                color_discrete_map=cores_status,
                barmode='stack'
            )
            fig6.update_layout(height=400)
            st.plotly_chart(fig6, use_container_width=True)

        # Correlação entre fatores
        st.markdown("---")
        st.header("🔗 Análise de Correlação")

        fig7 = px.scatter(
            df_filtrado,
            x='Nota_Media',
            y='Faltas',
            color='Status',
            size='Distancia_Escola_km',
            hover_data=['Serie', 'Renda_Familiar'],
            color_discrete_map=cores_status,
            title="Relação entre Notas, Faltas e Status"
        )
        fig7.update_layout(height=500)
        st.plotly_chart(fig7, use_container_width=True)

        # Tabela de alunos em risco
        st.markdown("---")
        st.header("⚠️ Alunos em Situação de Risco")

        alunos_risco_df = df_filtrado[df_filtrado['Status'].isin(['Em Risco', 'Evadido'])].sort_values('Faltas', ascending=False)

        if len(alunos_risco_df) > 0:
            st.dataframe(
                alunos_risco_df[['ID_Aluno', 'Serie', 'Status', 'Nota_Media', 'Faltas', 'Renda_Familiar', 'Apoio_Familiar']].head(10),
                use_container_width=True
            )
            
            # Opção de download
            csv = alunos_risco_df.to_csv(index=False)
            st.download_button(
                label="📥 Baixar lista completa (CSV)",
                data=csv,
                file_name="alunos_em_risco.csv",
                mime="text/csv"
            )
        else:
            st.info("Nenhum aluno em situação de risco com os filtros selecionados.")

        # Recomendações
        st.markdown("---")
        st.header("💡 Recomendações e Insights")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.info("""
            **🎯 Intervenção Prioritária**
            
            Focar nos alunos com:
            - Mais de 20 faltas
            - Nota média abaixo de 5.0
            - Baixo apoio familiar
            """)

        with col2:
            st.success("""
            **✅ Estratégias Preventivas**
            
            - Programas de tutoria
            - Acompanhamento personalizado
            - Integração família-escola
            - Atividades extracurriculares
            """)

        with col3:
            st.warning("""
            **📊 Monitoramento Contínuo**
            
            - Frequência semanal
            - Desempenho acadêmico
            - Participação nas atividades
            - Contato com responsáveis
            """)

        # Footer
        st.markdown("---")
        st.markdown("*Dashboard desenvolvido para diagnóstico e prevenção da evasão escolar*")