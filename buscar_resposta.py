from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure_config import AZURE_ENDPOINT, AZURE_API_KEY, INDEX_NAME

def buscar_informacao(pergunta):
    """
    Realiza uma busca no Azure Cognitive Search com base na pergunta fornecida.

    :param pergunta: A pergunta que o usuário deseja buscar no índice.
    :return: Lista de respostas relevantes encontradas.
    """
    search_client = SearchClient(endpoint=AZURE_ENDPOINT, index_name=INDEX_NAME, credential=AzureKeyCredential(AZURE_API_KEY))
    
    # Realiza a busca no índice
    resultados = search_client.search(query=pergunta)
    
    respostas = [doc['conteudo'] for doc in resultados]
    return respostas

if __name__ == "__main__":
    # Exemplo de uso
    pergunta = "Qual é o conceito de inteligência artificial?"
    respostas = buscar_informacao(pergunta)
    for resposta in respostas:
        print(resposta)
