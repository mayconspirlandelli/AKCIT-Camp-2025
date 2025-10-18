# 🚀 Dividend Analyst - Streamlit App

Interface web interativa para análise comparativa de dividendos usando IA multi-agente.

## 📦 Como Executar

### 1. Ative o ambiente virtual

```bash
cd /home/leon/akcit/akcit-camp/repo/akcit-camp-2025/dia2
source .venv/bin/activate
```

### 2. Execute o Streamlit

```bash
streamlit run streamlit_app.py
```

O app abrirá automaticamente em seu navegador em `http://localhost:8501`

## 🎯 Como Usar

1. **Selecione as ações** no menu lateral (mínimo 2, máximo 6)
2. **Escolha o período** de análise (1 ano, 6 meses, etc.)
3. **Selecione o modelo de IA** (OpenAI ou Gemini)
4. **Clique em "Analisar Dividendos"**
5. **Baixe o PDF** gerado com o ranking completo

## 🔑 Configuração de APIs

Certifique-se de ter as chaves de API configuradas no arquivo `.env`:

```env
OPENAI_API_KEY=sua_chave_aqui
GEMINI_API_KEY=sua_chave_aqui
```

## ✨ Funcionalidades

- ✅ Interface intuitiva e responsiva
- ✅ Seleção múltipla de ações
- ✅ Suporte para OpenAI e Gemini
- ✅ Geração automática de PDF profissional
- ✅ Download direto do relatório
- ✅ Feedback visual em tempo real

## 📊 Ações Disponíveis

O app inclui as principais ações da B3:
- **Petróleo & Gás:** PETR4
- **Mineração:** VALE3
- **Bancos:** ITUB4, BBDC4, BBAS3
- **Utilities:** ELET3, ENBR3, CPLE6, TAEE11, CMIG4
- **E muito mais...**

## 🤖 Tecnologias

- **Streamlit** - Interface web
- **CrewAI** - Orquestração multi-agente
- **OpenAI/Gemini** - Modelos de linguagem
- **ReportLab** - Geração de PDF
- **Brapi.dev** - Dados financeiros

---

**Desenvolvido com ❤️ usando IA Multi-Agente**


