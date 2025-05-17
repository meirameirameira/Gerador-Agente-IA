# -*- coding: utf-8 -*-
"""Gerador-Agente-IA.ipynb
"""

%pip -q install google-genai

!pip install -q google-adk

import os
from google.colab import userdata

os.environ["GOOGLE_API_KEY"] = userdata.get('GOOGLE_API_KEY')

from google import genai

client = genai.Client()

MODEL_ID = "gemini-2.0-flash"

from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.genai import types  # Para criar conteúdos (Content e Part)
from datetime import date
import textwrap # Para formatar melhor a saída de texto
from IPython.display import display, Markdown # Para exibir texto formatado no Colab
import requests # Para fazer requisições HTTP
import warnings

warnings.filterwarnings("ignore")

# Função auxiliar que envia uma mensagem para um agente via Runner e retorna a resposta final
def call_agent(agent: Agent, message_text: str) -> str:
    # Cria um serviço de sessão em memória
    session_service = InMemorySessionService()
    # Cria uma nova sessão (você pode personalizar os IDs conforme necessário)
    session = session_service.create_session(app_name=agent.name, user_id="user1", session_id="session1")
    # Cria um Runner para o agente
    runner = Runner(agent=agent, app_name=agent.name, session_service=session_service)
    # Cria o conteúdo da mensagem de entrada
    content = types.Content(role="user", parts=[types.Part(text=message_text)])

    final_response = ""
    # Itera assincronamente pelos eventos retornados durante a execução do agente
    for event in runner.run(user_id="user1", session_id="session1", new_message=content):
        if event.is_final_response():
          for part in event.content.parts:
            if part.text is not None:
              final_response += part.text
              final_response += "\n"
    return final_response

# Função auxiliar para exibir texto formatado em Markdown no Colab
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# --- Agente 1: Gerador de Agente --- #
def agente_gerador(topico):
    gerador = Agent(
        name="agente_gerador",
        model="gemini-2.0-flash",
        instruction="""
        Você é um assistente inteligente e especialista em IA que ao buscar com a ferramenta google_search auxilía o usuário a gerar agentes de ia assim como esse que você esta sendo feito sobre o tópico de interesse.
        Você é destinado a pessoas com pouco conhecimento em linguagens de programação, seu público tem uma faixa etária bem abrangente.
        Não seja tão técnico e apenas escreva códigos se extremamente necessário, este passo serve apenas para dar ideias ao usuário.
        """,
        description="Agente que busca",
        tools=[google_search]
    )

    entrada_do_agente_gerador = f"Vamos criar Agentes de Ia juntos sobre {topico}!"
    # Executa o agente
    geracao = call_agent(gerador, entrada_do_agente_gerador)
    return geracao

# --- Agente 2: Planejador de Agente --- #
def agente_planejador(topico, geracao_buscada):
    planejador = Agent(
        name="agente_planejador",
        model="gemini-2.0-flash",
        # Inserir as instruções do Agente Planejador
        instruction="""
        Você, por ser um especialista em ia, escolha um assunto dos tópicos buscados e o aprofunde. Mesmo com um público que pode não entender sobre linguagens de programação, em suas explicações você também deve usar python, explicando bem cada linha de código gerada para que a lógica seja facilmente entendida.
        Você deve especificar e ensinar caso seja necessária a utilização de SDKs ou APIs.
        Não seja tão técnico e apenas escreva códigos se extremamente necessário, este passo serve apenas para dar ideias ao usuário.
        """,
        description="Agente que planeja Agente",
        tools=[google_search]
    )

    entrada_do_agente_planejador = f"Tópico:{topico}"
    # Executa o agente
    plano_do_agente = call_agent(planejador, entrada_do_agente_planejador)
    return plano_do_agente

# --- Agente 3: Resumo --- #
def agente_resumo(topico, plano_do_agente):
    resumo = Agent(
        name="agente_resumo",
        model="gemini-2.0-flash",
        instruction="""
            De acordo com o que você fez planejou crie um resumo para o usuário com pontos relevantes.
            """,
        description="Agente resumo de plano de agentes"
    )
    entrada_do_agente_resumo = f"Tópico: {topico}\nPlano de Agente: {plano_do_agente}"
    # Executa o agente
    resumos = call_agent(resumo, entrada_do_agente_resumo)
    return resumos

# --- Agente 4: Tutorial --- #
def agente_tutorial(topico, resumo_gerado):
    tutorial = Agent(
        name="agente_tutorial",
        model="gemini-2.0-flash",
        instruction="""
            Agora faça um tutorial extremamente detalhado, técnico e com códigos em python para implementar os agentes gerados.
            """,
        description="Agente tutorial de post para redes sociais."
    )
    entrada_do_agente_tutorial = f"Tópico: {topico}\nRascunho: {resumos}"
    # Executa o agente
    texto_tutorial = call_agent(tutorial, entrada_do_agente_tutorial)
    return texto_tutorial

# --- Obter o Tópico do Usuário ---
topico = input("\n❓ Por favor, digite o TÓPICO sobre o qual você quer gerar seus agentes: ")

# Inserir lógica do sistema de agentes

if not topico:
    print("\nPor favor, insira um tópico válido.")

else:
    print(f"\nVamos criar Agentes de IA juntos sobre {topico}!")

    geracao_buscada = agente_gerador(topico)
    print("\n -- Resultados do Agente Gerador --")
    display(to_markdown(geracao_buscada))
    print("\n==================================================================================")

    plano_do_agente = agente_planejador(topico, geracao_buscada)
    print("\n -- Resultados do Agente Planejador --")
    display(to_markdown(plano_do_agente))
    print("\n==================================================================================")

    resumos = agente_resumo(topico, plano_do_agente)
    print("\n -- Resultados do Agente Resumo --")
    display(to_markdown(resumos))
    print("\n==================================================================================")

    texto_tutorial = agente_tutorial(topico, resumos)
    print("\n -- Resultados do Agente Tutorial --")
    display(to_markdown(texto_tutorial))
    print("\n=================================================================================="
    )