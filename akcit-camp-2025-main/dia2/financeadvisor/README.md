# 💰 Finance Advisor – Dividend Analyst

Um sistema multi-agente avançado para análise comparativa de dividendos de ações brasileiras. Ele combina dados em tempo real da B3, cálculo de métricas financeiras, orquestração com **CrewAI**, geração de insights com **LLMs** (OpenAI/Gemini) e **geração automática de relatórios PDF** profissionais.

### Por que este projeto?

- Demonstra uma arquitetura completa de **IA multi-agente** para análise financeira
- Integra **cache** (Redis), **LLMs** e **APIs financeiras**
- Oferece tanto uma **interface web moderna** (Streamlit) quanto **uso programático**
- Ideal para bootcamps, estudos de arquitetura de software e aplicações práticas de IA

---

## 🎯 Funcionalidades Principais

✅ Análise comparativa de múltiplas ações simultaneamente  
✅ Dados reais da B3 via API **brapi.dev**  
✅ Cálculo de métricas: retorno, volatilidade, dividend yield, P/L, etc.  
✅ Insights gerados por IA com base em dados e métricas  
✅ Ranking automático das melhores ações para dividendos  
✅ Geração de **relatórios PDF profissionais** com ReportLab  
✅ Interface web interativa com Streamlit  
✅ Sistema de cache inteligente (evita chamadas redundantes)  
✅ Suporte para **OpenAI** (GPT-4o-mini) e **Google Gemini**

---

## 📋 Pré-requisitos

- **Python 3.11+** (recomendado 3.12)
- **Docker** (para Redis)
- **Chave de API** do Google AI Studio (Gemini) **ou** OpenAI
- Token da **brapi.dev** (opcional, mas recomendado para evitar rate limits)
- Sistema operacional: Linux, macOS ou Windows (WSL2 recomendado)

---

## 🚀 Setup Rápido

### 1. Navegue até o diretório do projeto

```bash
cd /home/leon/akcit/akcit-camp/repo/akcit-camp-2025/dia2
```

### 2. Crie e ative o ambiente virtual

**Linux/macOS/WSL:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell):**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Instale as dependências

```bash
pip install -r financeadvisor/requirements.txt
```

**Pacotes principais instalados:**
- `crewai` – orquestração multi-agente
- `streamlit` – interface web
- `redis` – cache e rate limiting
- `google-generativeai` – LLM Gemini
- `reportlab` – geração de PDFs
- `pandas`, `numpy` – manipulação de dados
- `python-dotenv` – gerenciamento de variáveis de ambiente

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto (`dia2/.env`):

```bash
# APIs de LLM (escolha pelo menos uma)
GEMINI_API_KEY=sua_chave_gemini_aqui
OPENAI_API_KEY=sua_chave_openai_aqui

# API de dados financeiros (opcional)
BRAPI_TOKEN=seu_token_brapi_aqui

# Configurações Redis (usando Docker)
REDIS_HOST=localhost
REDIS_PORT=6379
```

**Como obter as chaves:**
- **Gemini:** https://aistudio.google.com/app/apikey
- **OpenAI:** https://platform.openai.com/api-keys
- **Brapi.dev:** https://brapi.dev/dashboard (plano gratuito disponível)

### 5. Inicie o Redis com Docker

```bash
docker-compose up -d
```

Isso iniciará o container Redis na porta 6379.

**Verificar se está rodando:**
```bash
docker ps
```

---

## 🎮 Como Rodar

### Opção 1: Interface Web com Streamlit (Recomendado)

```bash
streamlit run streamlit_app.py
```

O navegador abrirá automaticamente em `http://localhost:8501`

**Como usar:**
1. **Selecione de 2 a 6 ações** no menu lateral
2. **Escolha o período** de análise (1 ano, 6 meses, etc.)
3. **Selecione o modelo de IA** (OpenAI ou Gemini)
4. **Clique em "Analisar Dividendos"**
5. **Aguarde a geração** (pode levar 30-60s)
6. **Baixe o PDF** gerado com o ranking completo

### Opção 2: Uso Programático (Python)

#### Análise de um único ticker:

```python
from financeadvisor.core.orchestrator import analyze

resposta = analyze(
    ticker="PETR4",
    periodo="1y",
    user_question="Analise os dividendos da Petrobras",
    user_id="usuario123",
    llm_provider="gemini"  # ou "openai"
)

print(resposta)
```

#### Análise comparativa de múltiplos tickers:

```python
from financeadvisor.core.orchestrator import analyze_multi_tickers

pdf_path = analyze_multi_tickers(
    tickers=["PETR4", "VALE3", "ITUB4"],
    periodo="1y",
    user_question="Análise comparativa de dividendos",
    user_id="usuario123",
    llm_provider="gemini"
)

print(f"PDF gerado: {pdf_path}")
```

#### Executar análises em lote:

```bash
python financeadvisor/main.py
```

Este script executa análises pré-configuradas de diferentes carteiras (Blue Chips, Utilities, Top Dividendos).

---

## 🏗️ Arquitetura do Sistema

### Visão Geral

O sistema segue uma arquitetura multi-camadas com agentes especializados orquestrados pelo CrewAI:

```
┌─────────────────────────────────────────────────────────────┐
│                     USUÁRIO / INTERFACE                      │
│              (Streamlit UI ou Python Script)                 │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                    ORQUESTRADOR                              │
│         (financeadvisor/core/orchestrator.py)                │
│                                                              │
│  • Rate limiting por usuário (Redis)                         │
│  • Verificação de cache                                      │
│  • Coordenação do fluxo multi-agente                         │
└──────┬──────────────┬──────────────┬────────────────────────┘
       │              │              │
       ▼              ▼              ▼
┌──────────┐   ┌──────────┐   ┌──────────────┐
│  Data    │   │ Metrics  │   │ CrewAI       │
│  Loader  │   │Calculator│   │ Multi-Agent  │
└──────────┘   └──────────┘   └──────────────┘
       │              │              │
       ▼              ▼              ▼
┌──────────┐   ┌──────────┐   ┌──────────────┐
│ brapi.dev│   │  Redis   │   │ LLM          │
│   API    │   │  Cache   │   │              │
└──────────┘   └──────────┘   └──────────────┘
                                      │
                                      ▼
                              ┌──────────────┐
                              │ PDF Generator│
                              │ (ReportLab)  │
                              └──────────────┘
```

### Fluxo de Execução Detalhado

#### 1. **Recepção da Solicitação**
   - Usuário fornece: tickers, período, pergunta
   - Orquestrador aplica **rate limiting** via Redis

#### 2. **Carregamento de Dados (Data Loader)**
   - Verifica cache Redis (`rawdata:ticker:periodo`)
   - Se não existir, faz requisição à **brapi.dev**
   - Armazena dados brutos com TTL de 24h

#### 3. **Cálculo de Métricas (Metrics Calculator)**
   - Verifica cache Redis (`metrics:ticker:periodo`)
   - Calcula: retorno médio, volatilidade, dividend yield, P/L, etc.
   - Armazena métricas calculadas com TTL de 24h

#### 4. **Geração de Insights (CrewAI)**
   - **Agente Analista** usa tools para:
     - Consultar métricas atuais
     - Gerar insights textuais com LLM (Gemini/OpenAI)
   - Resultado cacheado em `insights:ticker:periodo`

#### 5. **Recomendação Final (CrewAI)**
   - **Agente Consultor** consolida análises
   - Gera recomendação (COMPRA/VENDA/MANUTENÇÃO)
   - Calcula score de atratividade
   - Resultado cacheado em `recommendation:ticker:periodo`

#### 6. **Geração de Relatório (Multi-Ticker)**
   - Consolida análises de todos os tickers
   - Cria ranking comparativo
   - Gera PDF profissional com ReportLab
   - Salva em `/dia2/reports/`

---

## 📂 Estrutura de Arquivos

```
dia2/
├── financeadvisor/               # Pacote principal
│   ├── __init__.py
│   ├── main.py                   # Script de análise em lote
│   ├── requirements.txt          # Dependências Python
│   │
│   ├── core/                     # Módulos de negócio
│   │   ├── __init__.py
│   │   ├── orchestrator.py       # 🎯 Orquestrador principal
│   │   ├── data_loader.py        # 📊 Carregamento de dados (brapi.dev)
│   │   └── metrics_calculator.py # 📈 Cálculo de métricas financeiras
│   │
│   ├── crew/                     # Sistema multi-agente CrewAI
│   │   ├── __init__.py
│   │   ├── crew.py               # 🤖 Definição de agentes e tasks
│   │   └── tools.py              # 🔧 Tools: cache, LLM
│   │
│   ├── utils/                    # Utilitários compartilhados
│   │   ├── __init__.py
│   │   ├── cache.py              # ⚡ Redis: cache e rate limiting
│   │   └── llm_client.py         # 💬 Cliente LLM (Gemini)
│   │
│   └── workers/                  # (DEPRECATED) Workers assíncronos
│
├── streamlit_app.py              # 🖥️ Interface web Streamlit
├── docker-compose.yaml           # 🐳 Configuração Docker (Redis)
├── .env                          # 🔐 Variáveis de ambiente (criar)
├── reports/                      # 📄 PDFs gerados
└── .streamlit/                   # ⚙️ Configurações Streamlit
    └── config.toml
```

### Módulos Principais

#### 🎯 `core/orchestrator.py`
Coordena todo o fluxo de trabalho:
- `analyze(ticker, periodo, ...)` – análise única
- `analyze_multi_tickers(tickers, ...)` – análise comparativa + PDF

#### 📊 `core/data_loader.py`
Gerencia dados da brapi.dev:
- Busca cotações históricas
- Informações fundamentalistas
- Dividendos distribuídos

#### 📈 `core/metrics_calculator.py`
Calcula métricas financeiras:
- Retorno acumulado e médio
- Volatilidade (desvio padrão)
- Dividend yield
- P/L, ROE, margem líquida
- Preço atual vs. mínimo/máximo

#### 🤖 `crew/crew.py`
Define agentes CrewAI:
- **Analyst Agent:** gera insights detalhados
- **Advisor Agent:** consolida recomendações
- **Tasks:** insight_task, recommendation_task

#### 🔧 `crew/tools.py`
Tools personalizadas:
- `CacheTool`: operações Redis
- `LLMTool`: chamadas ao LLM

#### ⚡ `utils/cache.py`
Interface Redis:
- `get_cached(key)` / `set_cached(key, value, ttl)`
- `check_rate_limit(user_id, max_requests, window)`
- Conexão com retry automático

---

## 🔄 Sobre Cache

### O que é cacheado no Redis?

| Chave | Conteúdo | TTL | Propósito |
|-------|----------|-----|-----------|
| `rawdata:TICKER:PERIODO` | JSON da brapi.dev | 24h | Evitar requisições redundantes |
| `metrics:TICKER:PERIODO` | Métricas calculadas | 24h | Economizar processamento |
| `insights:TICKER:PERIODO` | Texto gerado pelo LLM | 24h | Evitar chamadas LLM desnecessárias |
| `recommendation:TICKER:PERIODO` | Recomendação final | 24h | Cache de resultado completo |
| `rate:USER_ID:janela` | Contadores | 1min | Rate limiting por usuário |

**Benefícios:**
- ⚡ Respostas instantâneas para consultas repetidas
- 💰 Economia de custos de API (LLM)
- 🚀 Melhor experiência do usuário
- 🛡️ Proteção contra rate limits

 

---

## 🎨 Interface Streamlit

A interface web oferece:

**Barra Lateral:**
- ✅ Seleção de 2-6 ações (multiselect)
- ✅ Escolha do período (1y, 6mo, 3mo, 2y)
- ✅ Seleção do modelo (OpenAI/Gemini)
- ✅ Informações de ajuda expansíveis

**Área Principal:**
- ✅ Cards com ações selecionadas
- ✅ Botão de análise destacado
- ✅ Barra de progresso durante processamento
- ✅ Resultado com link do PDF
- ✅ Botão de download direto

**Feedback Visual:**
- 🔵 Info boxes para orientação
- 🟡 Warnings para validações
- 🟢 Success messages após conclusão
- 🔴 Error messages em falhas
- ⏳ Progress bars em tempo real

---

## 🛠️ Personalizações Comuns

### Trocar o modelo LLM

**No código Python:**
```python
resposta = analyze(
    ticker="PETR4",
    periodo="1y",
    user_question="Análise",
    llm_provider="openai"  # ou "gemini"
)
```

**Na interface Streamlit:** use o seletor de modelo na barra lateral.

### Ajustar critérios de recomendação

Edite `financeadvisor/crew/tools.py`:

```python
# Exemplo: mudar threshold de dividend yield
if dividend_yield > 0.08:  # 8% ao invés de 7%
    recomendacao = "COMPRA"
```

### Adicionar novos tickers

Em `streamlit_app.py`, adicione ao `ACOES_DISPONIVEIS`:

```python
ACOES_DISPONIVEIS = [
    "PETR4", "VALE3", "ITUB4", "BBDC4",
    "SEU_TICKER_AQUI",  # adicione aqui
    ...
]
```

### Modificar período de cache

Em `financeadvisor/utils/cache.py`:

```python
# Alterar TTL padrão de 24h para 12h
DEFAULT_TTL = 3600 * 12  # segundos
```

### Personalizar PDF gerado

Edite `financeadvisor/crew/tools.py` na função de geração de PDF:
- Altere cores, fontes, layout
- Adicione gráficos, tabelas
- Customize cabeçalho/rodapé

---

## 📊 Ações Disponíveis

O sistema suporta principais ações da B3:

**Petróleo & Mineração:** PETR4, VALE3  
**Bancos:** ITUB4, BBDC4, BBAS3, B3SA3  
**Utilities:** ELET3, ENBR3, CPLE6, TAEE11, CMIG4  
**Consumo:** ABEV3, JBSS3, EMBR3  
**Outros:** RENT3, WEGE3, SUZB3, RAIL3, CSAN3, VIVT3

---

## 🧪 Comandos Úteis

### Verificar status do Redis
```bash
docker ps
docker logs redis
```

### Reiniciar Redis
```bash
docker-compose restart
```

### Limpar cache Redis
```bash
docker exec -it redis redis-cli FLUSHALL
```

### Verificar instalação das dependências
```bash
pip list | grep -E "crewai|streamlit|redis"
```

### Gerar relatório de debug
```bash
python -c "from financeadvisor.utils.cache import get_redis; print(get_redis().ping())"
```

---

## 🐛 Troubleshooting

### Erro: "Connection refused" (Redis)
**Solução:** Certifique-se que o Docker está rodando:
```bash
docker-compose up -d
```

### Erro: API key inválida
**Solução:** Verifique o arquivo `.env`:
- Chave correta e sem espaços extras
- Arquivo `.env` está em `dia2/.env`

### PDF não é gerado
**Solução:** Verifique permissões da pasta `reports/`:
```bash
mkdir -p reports
chmod 755 reports
```

### LLM retorna respostas genéricas
**Solução:**
- Limpe o cache Redis e tente novamente
- Aumente a `temperature` do LLM
- Refine o prompt com mais contexto ou forneça métricas específicas

---

## 🤝 Tecnologias Utilizadas

| Tecnologia | Propósito |
|------------|-----------|
| **CrewAI** | Orquestração multi-agente |
| **OpenAI/Gemini** | Modelos de linguagem (LLMs) |
| **Redis** | Cache e rate limiting |
| **Streamlit** | Interface web interativa |
| **ReportLab** | Geração de PDFs |
| **Pandas/NumPy** | Manipulação de dados |
| **brapi.dev** | API de dados financeiros B3 |
| **Docker** | Containerização de serviços |

---

## 📚 Próximos Passos

Sugestões para expandir o projeto:

1. **Gráficos no PDF:** adicionar charts com Matplotlib/Plotly
2. **Alertas por email:** notificar quando uma ação atingir critérios
3. **Análise técnica:** integrar indicadores (RSI, MACD, Bollinger)
4. **Dashboard histórico:** armazenar rankings ao longo do tempo
5. **API REST:** expor endpoints com FastAPI
6. **Backtesting:** simular estratégias de investimento
7. **Integração com corretoras:** executar ordens automaticamente
8. **Chatbot conversacional:** perguntas interativas sobre análises

---

## ⚠️ Observações Importantes

- **Uso Educacional:** Este projeto é um protótipo para aprendizado e demonstração de conceitos de IA multi-agente.
- **Não é Consultoria Financeira:** As análises geradas são automatizadas e não substituem consultoria profissional.
- **Segurança:** Para produção, implemente autenticação, criptografia de chaves e auditoria de logs.
- **Rate Limits:** Respeite os limites das APIs (brapi.dev, OpenAI, Gemini).
- **Custos:** Chamadas para LLMs têm custo. Configure limites de gastos nas plataformas.

---

## 📄 Licença

Este projeto é de código aberto e destinado a fins educacionais. Use com responsabilidade.

---

**Desenvolvido para o Bootcamp AKCIT com ❤️ usando IA Multi-Agente**
