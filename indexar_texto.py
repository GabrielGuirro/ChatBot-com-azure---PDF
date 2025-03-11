from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure_config import AZURE_ENDPOINT, AZURE_API_KEY, INDEX_NAME

def indexar_pdf(texto, id_documento):
    """
    Indexa o texto extraído do PDF no serviço de Azure Cognitive Search.

    :param texto: Texto extraído do PDF.
    :param id_documento: ID único para o documento a ser indexado.
    """
    # Configura o cliente do Azure Cognitive Search
    search_client = SearchClient(endpoint=AZURE_ENDPOINT, index_name=INDEX_NAME, credential=AzureKeyCredential(AZURE_API_KEY))
    
    documento = {
        "id": id_documento,
        "conteudo": texto
    }
    
    search_client.upload_documents(documents=[documento])
    print(f"Documento {id_documento} indexado com sucesso.")

if __name__ == "__main__":
    # Exemplo de uso
    texto_pdf = "Conteúdo do PDF extraído"
    indexar_pdf(texto_pdf, id_documento="1")  # Ajuste o ID conforme necessário
