import fitz  # PyMuPDF

def carregar_pdf(caminho_pdf):
    """
    Carrega um arquivo PDF e extrai o texto de todas as suas páginas.

    :param caminho_pdf: Caminho do arquivo PDF.
    :return: Texto extraído do PDF.
    """
    documento = fitz.open(caminho_pdf)
    texto = ""
    for pagina in documento:
        texto += pagina.get_text()
    return texto

if __name__ == "__main__":
    # Exemplo de uso
    caminho_pdf = "inputs/seu_arquivo.pdf"  # Altere conforme necessário
    texto = carregar_pdf(caminho_pdf)
    print(texto)
