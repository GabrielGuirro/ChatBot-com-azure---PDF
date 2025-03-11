# Chat Inteligente com Base em PDFs - Azure

## Visão Geral

Este projeto utiliza a **Azure Cognitive Search** para indexar e buscar informações de arquivos **PDF**, combinando com a **Azure OpenAI** (GPT-3) para gerar respostas contextuais baseadas no conteúdo dos documentos. O objetivo é criar um chat interativo onde o usuário pode perguntar sobre o conteúdo dos PDFs e receber respostas precisas.

## Funcionalidades

- Carregar e processar arquivos PDF.
- Indexar o conteúdo do PDF no **Azure Cognitive Search**.
- Realizar buscas eficientes utilizando o serviço de busca vetorial.
- Gerar respostas contextuais com **Azure OpenAI**.
- Chat interativo para perguntas e respostas baseadas no conteúdo dos PDFs.

## Tecnologias Usadas

- **Python**: Linguagem principal.
- **Azure Cognitive Search**: Para indexação e busca de conteúdo.
- **Azure OpenAI (GPT-3)**: Para gerar respostas naturais e contextuais.
- **FAISS**: Para busca vetorial (se necessário).

## Como Usar

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
Instale as dependências:

bash
Copiar
pip install -r requirements.txt
Adicione seus PDFs na pasta inputs/.

Configure as credenciais do Azure no arquivo src/azure_config.py.

Execute o chat interativo:

bash
Copiar
python src/chat_interativo.py
