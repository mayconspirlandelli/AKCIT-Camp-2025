#Fluxo do Agente de Pedidos 
#START → boas_vindas → identifica_cliente → escolher_produtos 
#   → adicionar_itens_carrinho → finalizar_pedido → END
#                              └── cancelar_pedido → END

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
    "Você é o garçom de um delivery online, responsavel por anotar, registrar, finalizar e cancelar pedidos \n"
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
    """
    Permite que o cliente escolha produtos do cardápio.
    Caso o cliente ainda não tenha mencionado nenhum produto, 
    o sistema apresenta sugestões.
    """

    nome = state.get("nome", "cliente")
    mensagem = (state.get("mensagem_usuario") or "").strip().lower()

    # Simula um cardápio (poderia vir de um banco de dados)
    cardapio = ["pizza", "hambúrguer", "pastel", "refrigerante", "suco"]

    # Se não há mensagem do cliente, mostra o cardápio
    if not mensagem:
        state["resposta"] = (
            f"Olá, {nome}! Aqui está nosso cardápio de hoje:\n"
            f"🍕 {', '.join(cardapio)}.\n\n"
            "Qual desses produtos você gostaria de pedir?"
        )
        state["etapa"] = "escolher_produtos"
        return state

    # Se o cliente quiser cancelar o pedido
    if "cancelar" in mensagem:
        state["resposta"] = "Entendido! Cancelando o pedido conforme solicitado."
        state["etapa"] = "cancelar_pedido"
        return state

    # Se o cliente quiser finalizar sem escolher nada
    if "finalizar" in mensagem:
        state["resposta"] = "Você ainda não adicionou itens. Deseja escolher algo antes de finalizar?"
        state["etapa"] = "escolher_produtos"
        return state

    # Verifica se o produto faz parte do cardápio
    produto_encontrado = None
    for item in cardapio:
        if item in mensagem:
            produto_encontrado = item
            break

    if produto_encontrado:
        resposta = qa_chain.invoke({
            "nome": nome,
            "pergunta": f"O cliente deseja adicionar {produto_encontrado} ao pedido. Confirme e agradeça."
        })
        state["resposta"] = (
            f"{resposta}\nDeseja adicionar mais itens ao carrinho ou finalizar o pedido?"
        )
        state["produto_escolhido"] = produto_encontrado
        state["etapa"] = "adicionar_itens_carrinho"
        return state

    # Se o produto não está no cardápio
    state["resposta"] = (
        f"Desculpe, {nome}, não encontrei esse item no nosso cardápio. "
        "Temos 🍕 pizza, 🍔 hambúrguer, 🥟 pastel, 🥤 refrigerante e 🍹 suco. "
        "O que você gostaria?"
    )
    state["etapa"] = "escolher_produtos"
    return state



def adicionar_itens_carrinho_node(state: dict) -> dict:
    """
    Adiciona os itens escolhidos pelo cliente ao carrinho.
    Usa a LLM para responder confirmações e solicitações.
    """
    mensagem = (state.get("mensagem_usuario") or "").strip()
    nome = state.get("nome", "cliente")

    if not mensagem:
        state["resposta"] = "Quais produtos você gostaria de adicionar ao seu carrinho?"
        state["etapa"] = "adicionar_itens_carrinho"
        state["encerrar"] = False
        return state

    # Verifica se o cliente quer finalizar ou cancelar
    if "finalizar" in mensagem.lower():
        state["resposta"] = "Certo! Vamos para a finalização do pedido."
        state["etapa"] = "finalizar_pedido"
        return state

    if "cancelar" in mensagem.lower():
        state["resposta"] = "Tudo bem! Cancelando o pedido conforme solicitado."
        state["etapa"] = "cancelar_pedido"
        return state

    # Adiciona itens ao carrinho
    carrinho = state.setdefault("carrinho", [])
    carrinho.append(mensagem)

    resposta = qa_chain.invoke({
        "nome": nome,
        "pergunta": f"O cliente deseja adicionar {mensagem}. Confirme o registro."
    })

    state["resposta"] = resposta + "\nDeseja adicionar mais itens ou finalizar o pedido?"
    state["etapa"] = "adicionar_itens_carrinho"
    return state



def finalizar_pedido_node(state: dict) -> dict:
    """
    Finaliza o pedido, exibe um resumo e confirma a conclusão.
    """
    nome = state.get("nome", "cliente")
    carrinho = state.get("carrinho", [])

    if not carrinho:
        state["resposta"] = f"{nome}, você ainda não adicionou itens ao carrinho! Quer voltar e escolher algo?"
        state["etapa"] = "escolher_produtos"
        state["encerrar"] = False
        return state

    resumo = ", ".join(carrinho)
    resposta = (
        f"Perfeito, {nome}! Seu pedido com os seguintes itens foi finalizado:\n"
        f"🧁 {resumo}\n\n"
        "Agradecemos sua preferência! Deseja fazer outro pedido ou encerrar?"
    )

    state["resposta"] = resposta
    state["etapa"] = "fim"
    state["encerrar"] = True
    return state


def cancelar_pedido_node(state: dict) -> dict:
    """
    Cancela o pedido atual e encerra a conversa.
    """
    nome = state.get("nome", "cliente")

    resposta = (
        f"Tudo bem, {nome}. O seu pedido foi cancelado com sucesso. ❌\n"
        "Se desejar, posso iniciar um novo pedido a qualquer momento!"
    )

    state["resposta"] = resposta
    state["etapa"] = "fim"
    state["encerrar"] = True
    return state

def proxima_parada(state: dict) -> str:
    """
    Define a próxima etapa do fluxo de acordo com o estado atual do pedido.
    O roteador centraliza a lógica de transição entre os nós do grafo.
    """

    etapa = state.get("etapa")

    if etapa == "identificar_cliente":
        return "identificar_cliente"

    if etapa == "escolher_produtos":
        return "escolher_produtos"

    if etapa == "adicionar_itens_carrinho":
        return "adicionar_itens_carrinho"

    if etapa == "finalizar_pedido":
        return "finalizar_pedido"

    if etapa == "cancelar_pedido":
        return "cancelar_pedido"

    if etapa == "fim":
        return "fim"

    # Padrão: início do fluxo (caso seja a primeira interação)
    return "boas_vindas"

# Criar o grafo do agente com múltiplos nós
graph = StateGraph(dict)

# Criar os Nodes
graph.add_node("boas_vindas", boas_vindas_node)
graph.add_node("identificar_cliente", identificar_cliente_node)
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
#graph.set_entry_point("boas_vindas")

# Compila o grafo em um executor (cria um app pronto para .invoke)
app = graph.compile()


# Imprimir o Grafo
# from IPython.display import Image, display
# try:
#     display(Image(graph.get_graph().draw_mermaid_png()))
#     print(graph.get_graph().draw_mermaid())
# except Exception:
#     # This requires some extra dependencies and is optional
#     pass



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
