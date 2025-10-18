# 🎨 Layout do Streamlit App

## Interface Visual

```
╔════════════════════════════════════════════════════════════════════════╗
║                    💰 Dividend Analyst                                 ║
║              Análise comparativa de dividendos com IA                  ║
╠════════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║  ┌─────────────────────┐  ┌──────────────────────────────────────┐   ║
║  │  ⚙️ Configurações   │  │  🎯 Ações Selecionadas               │   ║
║  │                     │  │                                       │   ║
║  │  📊 Ações para      │  │  ┌──────┐  ┌──────┐  ┌──────┐       │   ║
║  │     Analisar        │  │  │PETR4 │  │VALE3 │  │ITUB4 │       │   ║
║  │  ┌────────────────┐ │  │  └──────┘  └──────┘  └──────┘       │   ║
║  │  │ ☑️ PETR4       │ │  │                                       │   ║
║  │  │ ☑️ VALE3       │ │  │                                       │   ║
║  │  │ ☑️ ITUB4       │ │  │  ┌──────────────────────────────┐   │   ║
║  │  │ ☐ BBDC4       │ │  │  │  🚀 Executar                 │   │   ║
║  │  │ ☐ BBAS3       │ │  │  │                              │   │   ║
║  │  │ ☐ ...         │ │  │  │  ▶️  Analisar Dividendos     │   │   ║
║  │  └────────────────┘ │  │  │                              │   │   ║
║  │                     │  │  └──────────────────────────────┘   │   ║
║  │  📅 Período         │  │                                       │   ║
║  │  [ 1 ano ▼ ]       │  └──────────────────────────────────────┘   ║
║  │                     │                                             ║
║  │  🤖 Modelo de IA    │  ┌──────────────────────────────────────┐   ║
║  │  ⚪ OpenAI          │  │  ✅ Análise concluída!               │   ║
║  │  ⚪ Gemini          │  │                                       │   ║
║  │                     │  │  📄 Relatório Gerado:                │   ║
║  │                     │  │  /reports/ranking_dividendos_1y.pdf  │   ║
║  │  ℹ️ Informações     │  │                                       │   ║
║  │  [  APIs...  ▼  ]  │  │  📥 [Baixar Relatório PDF]           │   ║
║  └─────────────────────┘  └──────────────────────────────────────┘   ║
║                                                                        ║
║  ────────────────────────────────────────────────────────────────────  ║
║  💡 Dica: Dividend yield acima de 7% gera recomendação de COMPRA      ║
║  🤖 Powered by CrewAI + OpenAI/Gemini + Brapi.dev                     ║
╚════════════════════════════════════════════════════════════════════════╝
```

## Fluxo de Uso

```
┌─────────────────────────────────────────────────────────────────┐
│  1️⃣  Usuário seleciona ações                                    │
│      ↓                                                          │
│  2️⃣  Escolhe período de análise                                 │
│      ↓                                                          │
│  3️⃣  Seleciona modelo de IA (OpenAI/Gemini)                     │
│      ↓                                                          │
│  4️⃣  Clica em "Analisar Dividendos"                             │
│      ↓                                                          │
│  ⚙️  Sistema processa (CrewAI Multi-Agente)                     │
│      ├── Busca dados (Brapi.dev)                               │
│      ├── Calcula métricas de dividendos                        │
│      ├── Compara e rankeia ações                               │
│      └── Gera PDF profissional                                 │
│      ↓                                                          │
│  5️⃣  PDF é gerado e disponibilizado para download               │
│      ↓                                                          │
│  6️⃣  Usuário baixa o relatório completo                         │
└─────────────────────────────────────────────────────────────────┘
```

## Cores e Tema

- **Cor Principal:** Verde (#4CAF50) - Representa crescimento financeiro
- **Background:** Branco limpo (#FFFFFF)
- **Background Secundário:** Cinza claro (#F0F2F6)
- **Texto:** Cinza escuro (#262730)

## Componentes Principais

### Sidebar (Menu Lateral)
- ✅ Multiselect para escolher ações (2-6 ações)
- ✅ Dropdown para período
- ✅ Radio buttons para modelo de IA
- ✅ Expander com informações de ajuda

### Área Principal
- ✅ Cards com ações selecionadas
- ✅ Botão grande de execução
- ✅ Barra de progresso durante análise
- ✅ Card de resultado com link do PDF
- ✅ Botão de download do relatório

### Feedback Visual
- 🔵 Info boxes para orientação
- 🟡 Warnings para validações
- 🟢 Success messages após conclusão
- 🔴 Error messages em caso de falha
- ⏳ Progress bars durante processamento

## Experiência do Usuário

1. **Simplicidade:** Interface limpa e intuitiva
2. **Feedback:** Mensagens claras em cada etapa
3. **Validação:** Previne erros antes da execução
4. **Performance:** Feedback visual durante processamento
5. **Resultado:** Download direto do PDF gerado

---

**Objetivo:** Tornar a análise de dividendos acessível e profissional com apenas alguns cliques! 🚀


