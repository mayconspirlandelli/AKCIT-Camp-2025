
import os
import re
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langgraph.graph import StateGraph, START, END


# Carregas chaves
load_dotenv()
os.environ.get("GOOGLE_API_KEY")

#Carrega modelo
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

template_text = (
    "Você é o garço de um delivery online, responsavel por anotar, registrar, finalizar e cancelar pedidos \n"
    "Converse de forma objetiva, em português, com o cliente {nome}.\n"
    "Pergunta do cliente: {pergunta}\n\n"
    "Responda de forma curta e útil."    
)
prompt = PromptTemplate(
    input_variables=["nome", "pergunta"],
    template=template_text
)

# Criar uma pipeline LCEL 
qa_chain = prompt | llm | StrOutputParser()


def extrair_nome(texto: str) -> str:
    """Heurística simples: usa a frase inteira como nome, limpando espaços e pontuação leve."""
    if not texto:
        return ""
    candidato = texto.strip()
    # Remove aspas e pontuação nas pontas
    candidato = re.sub(r'^["\'\s]+|["\'\s]+$', "", candidato)
    # Capitaliza primeiro nome/partes
    partes = [p.capitalize() for p in re.split(r"\s+", candidato) if p]
    return " ".join(partes)


def boas_vindas_node(state: dict) -> dict:
    state["resposta"] = "Olá! Eu sou o Ana Bot sua assistente de pedidos. Como posso te chamar?"
    state["etapa"] = "aguardar_nome"
    return state


# Registro a nome do cliente
def identificar_cliente_node(state: dict) -> dict:
    mensagem = (state.get("mensagem_usuario") or "").strip()
    if not mensagem:
        state["resposta"] = "Não entendi. Qual é o seu nome?"
        state["etapa"] = "aguardar_nome"
        return state

    nome = extrair_nome(mensagem)
    if not nome:
        state["resposta"] = "Poderia repetir seu nome, por favor?"
        state["etapa"] = "aguardar_nome"
        return state

    state["nome"] = nome
    state.setdefault("historico", [])
    state["resposta"] = f"Prazer, {nome}! Como posso ajudar em tecnologia hoje?"
    state["etapa"] = "responder_perguntas"
    return state



def escolher_produtos_node(state: dict) -> dict:
    mensagem = (state.get("mensagem_usuario") or "").strip()
    nome = state.get("nome", "usuário")

    if mensagem.lower() == "tchau" or "tchau" in mensagem.lower():
        state["resposta"] = f"Até logo, {nome}! 👋"
        state["etapa"] = "fim"
        state["encerrar"] = True
        return state

    # Gera resposta via LLM
    resposta = qa_chain.invoke({
        "nome": nome,
        "pergunta": mensagem or "Informe ao clientes os produtos disponíveis "
    })

    # Atualiza histórico simples
    historico = state.setdefault("historico", [])
    if mensagem:
        historico.append({"role": "user", "content": mensagem})
    historico.append({"role": "assistant", "content": resposta})

    state["resposta"] = resposta
    state["etapa"] = "responder_perguntas"
    state["encerrar"] = False
    return state


def roteador_node(state: dict) -> dict:
    # Nó "inócuo" apenas para permitir arestas condicionais
    return state


def proxima_parada(state: dict) -> str:
    # Verifica a etapa atual do estado
    etapa = state.get("etapa")
    if etapa == "aguardar_nome":
        return "aguardar_nome"
    if etapa == "responder_perguntas":
        return "responder_perguntas"
    if etapa == "fim":
        return "fim"
    # Padrão: início do fluxo
    return "boas_vindas"


# Criar o grafo do agente com múltiplos nós
graph = StateGraph(dict)

# Criar os Nodes
graph.add_node("boas_vindas", boas_vindas_node)
graph.add_node("identifica_cliente", identifica_cliente_node)
graph.add_node("escolher_produtos", escolher_produtos_node)
graph.add_node("adicionar_itens_carrinho", adicionar_itens_carrinho_node)
graph.add_node("finalizar_pedido", finalizar_pedido_node)
graph.add_node("cancelar_pedido", cancelar_pedido_node)

#Defini as aretas 
graph.add_edge(START, "boas_vindas")
graph.add_edge("boas_vindas", "identifica_cliente")
graph.add_edge("identifica_cliente", "escolher_produtos")
graph.add_edge("escolher_produtos", "adicionar_itens_carrinho")
graph.add_edge("adicionar_itens_carrinho", "finalizar_pedido")
graph.add_edge("finalizar_pedido", END)
graph.add_edge("cancelar_pedido", END)

# Node de partida
graph.set_entry_point("boas_vindas")

# Compila o grafo em um executor (cria um app pronto para .invoke)
app = graph.compile()




# ============================================================
# 6. Execução interativa (simulação de uso)
# ============================================================
# Loop de CLI simples para interagir com o agente.
# A cada entrada do usuário, invocamos o grafo passando um estado inicial
# com a chave "interesse" e depois exibimos a chave "resposta".
if __name__ == "__main__":
    print("🤖 Ana Bolt - Agente conversacional sobre delivery da confeiria\n")

    # Estado de conversa persistente entre rodadas
    state: dict = {}

    # Primeira saudação
    result = app.invoke(state)
    state.update(result)
    print(state.get("resposta", "Olá!"))

    while True:
        try:
            mensagem = input("\nVocê: ")
        except (KeyboardInterrupt, EOFError):
            print("\nEncerrando o agente. Até logo!")
            break

        if mensagem.lower() in ["sair", "exit", "quit"]:
            print("Encerrando o agente. Até logo!")
            break

        # Preenche a última mensagem e invoca 1 passo do grafo
        state["mensagem_usuario"] = mensagem
        result = app.invoke(state)
        state.update(result)

        print(f"\n🔎 Agente: {state.get('resposta', '')}")

        if state.get("etapa") == "fim" or state.get("encerrar"):
            print("\nConversa encerrada.")
            break
