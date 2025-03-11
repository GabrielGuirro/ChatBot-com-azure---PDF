from processar_pdf import carregar_pdf
from indexar_texto import indexar_pdf
from buscar_resposta import buscar_informacao
from gerar_resposta import gerar_resposta

def iniciar_chat(caminho_pdf):
    """
    Inicia o chat interativo com base no conteúdo do PDF.
    
    :param caminho_pdf: Caminho do arquivo PDF a ser processado.
    """
    # Carregar e processar o conteúdo do PDF
    texto_pdf = carregar_pdf(caminho_pdf)
    indexar_pdf(texto_pdf, id_documento="1")
    
    print("Bem-vindo ao chat! Digite 'sair' para encerrar.")
    
    while True:
        pergunta = input("Pergunta: ")
        
        if pergunta.lower() == 'sair':
            print("Sessão de chat encerrada.")
            break
        
        # Buscar conteúdo relevante no Azure Cognitive Search
        respostas_relevantes = buscar_informacao(pergunta)
        contexto = "\n".join(respostas_relevantes)
        
        # Gerar uma resposta com o GPT-3
        resposta_final = gerar_resposta(pergunta, contexto)
        
        print(f"Resposta: {resposta_final}")

if __name__ == "__main__":
    # Exemplo de uso
    iniciar_chat("inputs/seu_arquivo.pdf")
