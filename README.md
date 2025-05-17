# Gerador-Agente-IA
Este projeto inovador oferece uma solução para a criação e compreensão de Agentes de Inteligência Artificial de forma acessível e didática. Com uma arquitetura baseada em múltiplos agentes encadeados, o `Gerador-Agente-IA` guia o usuário desde a concepção inicial de um agente até a sua implementação prática, mesmo para aqueles com pouca ou nenhuma experiência em programação.

## 🚀 Como Funciona?

O sistema opera através de uma sequência de quatro agentes de IA, cada um com uma função específica, trabalhando em conjunto para transformar um tópico de interesse em um guia completo para o desenvolvimento de novos agentes:

1.  **Agente Gerador:** Este agente atua como um brainstormer, buscando e apresentando ideias gerais sobre o tópico fornecido pelo usuário. Ele é projetado para ser amigável e inspirador, focando em conceitos e possibilidades sem se aprofundar em detalhes técnicos complexos.
2.  **Agente Planejador:** Uma vez que as ideias são geradas, o Agente Planejador seleciona um dos tópicos e o aprofunda. Ele detalha como um agente de IA poderia ser construído em torno desse tópico, explicando a lógica e, quando necessário, fornecendo exemplos de código Python com explicações linha a linha. Ele também especifica a necessidade de SDKs ou APIs relevantes.
3.  **Agente Resumo:** Com base no plano detalhado, o Agente Resumo condensa as informações mais relevantes em um sumário conciso. Este resumo destaca os pontos essenciais e facilita a compreensão rápida do projeto do agente.
4.  **Agente Tutorial:** Por fim, o Agente Tutorial transforma o resumo em um guia passo a passo, extremamente detalhado e técnico. Este agente fornece o código Python necessário para implementar os agentes gerados, garantindo que o usuário tenha todas as ferramentas para colocar a mão na massa.

## ✨ Recursos

* **Geração de Agentes Personalizada:** Crie agentes de IA sobre qualquer tópico de seu interesse.
* **Aprendizado Simplificado:** Explicações claras e concisas, projetadas para um público amplo e iniciantes em IA.
* **Exemplos de Código Práticos:** Tutoriais detalhados com código Python e explicações para fácil entendimento.
* **Uso de Ferramentas Reais:** Orientações sobre o uso de SDKs e APIs quando aplicável.
* **Fluxo de Trabalho Guiado:** Uma cadeia de agentes que te acompanha em cada etapa do processo.

## 🛠️ Tecnologias Utilizadas

* **Google Gemini API:** Para as capacidades de geração de texto e compreensão da linguagem natural.
* **Google ADK (Agent Development Kit):** Para a orquestração e gerenciamento dos agentes.
* **Python:** Linguagem de programação principal utilizada nos exemplos de código.
* **Google Search Tool:** Para pesquisa e coleta de informações.

## 🚀 Começando

Para começar a gerar seus próprios agentes de IA, siga os passos abaixo:


1.  **Instale as Dependências:**
    ```bash
    %pip -q install google-genai
    !pip install -q google-adk
    ```

2.  **Configure sua Chave de API do Google:**
    Você precisará de uma chave de API do Google Gemini. Armazene-a de forma segura (por exemplo, usando `userdata.get('GOOGLE_API_KEY')` no Google Colab, como no código fonte).

    ```python
    import os
    from google.colab import userdata

    os.environ["GOOGLE_API_KEY"] = userdata.get('GOOGLE_API_KEY')
    ```

3.  **Execute o Notebook:**
    Abra e execute o notebook `Projeto Imersão Alura.ipynb` em um ambiente como o Google Colab. Você será solicitado a inserir um tópico de interesse.

    ```python
    # Exemplo de uso no notebook
    topico = input("\n❓ Por favor, digite o TÓPICO sobre o qual você quer gerar seus agentes: ")

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
        print("\n==================================================================================")
    ```

## 👀 Observações:
Este projeto foi feito de acordo com a Imersão IA 3ª Edição da Alura para concorrer aos melhores projetos.
