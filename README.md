# Explicação do projeto.

Este repositório tem o propósito de armazenar o conhecimento adquirido durante o curso proposto pela DeerpLearning.AI.

[Acesse o curso neste link.](https://learn.deeplearning.ai/langchain/lesson/1/introduction)

## 1. Models,Prompts and Parsers

**Modelos** - Seleção do modelo de linguagem que iremos trabalhar.

**Prompts** - Sequência de inputs que será passado ao modelo que irá orienta-lo.

**Parsers** - Pegando a saída destes modelos e definindo uma formatação mais estruturada para que sejá possível utilizar este Output para outras atividades.

## 2. Memory

* Forma mais prática e útil para se trabalhar e acessar a memória do modelo através de toda a interação realizada.

Quando utilizamos a memória para um chat conversacional o LLM estamos utilizando uma chave API independente, o modelo não possui está configuração embutida "de fábrica". Esse histórico de conversa é utilizado como contexto e este armazenamento é utilizado como input para o LLM.

Um histórico muito grande pode resultar em grande gasto dos Tokens, por isso o LangChain providencia formas diferentes de armazenamento e acumulo de conversas.

**ConversationBufferMemory** - Usado na maioria dos desenvolvimentos de Chatbots, dependendo da interação pode exigir bastante uso de tokens. Podemos extrair as mensagens em uma variável.

**ConversationBufferWindowMemory** - Armazena um número limitado de interações.

**ConversationTokenBufferMemory** - Armazena um número limitado de tokens, ideal para não deixar subir o preço das chamadas de LLM.

**ConversationSummaryMemory** - Criar um resumo das interações e passar como contexto para o LLM.

## 3. Chains

**LLMChain** - Um chain combina o LLM e o prompt para gerar uma sequência de operações no seu texto ou próprio dado.

**SimpleSequentialChain** - Esta Chain combina o Output de uma chain para servir de input para a próxima chain.

**SequentialChain** - Esta Chain combina o Output de múltiplas chains para servir de input para a próxima chain.

**Router Chain** - Sequência de sub-Chains que podem ser aproveitadas para gerar input de uma nova Chain.

## 4. Question and Awnser(QandA)

* Realizar perguntas e obter respostas utilizando arquivos externos.

## 5. Avaliação(Dando problema)
 
* Avaliação manual do modelo(e debugar)
* Avaliação assistida do LLM

## 6. Agents

* Utilizando LagChains tools nativas: DuckDuckGo search e Wikipedia
* Definindo suas próprias tools
