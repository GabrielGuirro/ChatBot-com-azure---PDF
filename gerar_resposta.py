import openai
from azure_config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def gerar_resposta(pergunta, contexto):
    """
    Gera uma resposta com base no contexto fornecido utilizando o GPT-3 da Azure OpenAI.

    :param pergunta: A pergunta que o usuário deseja fazer.
    :param contexto: O contexto relevante extraído dos documentos.
    :return: Resposta gerada pelo GPT-3.
    """
    resposta = openai.Completion.create(
        engine="text-davinci-003",  # ou outro modelo OpenAI
        prompt=f"Com base no seguinte contexto, responda à pergunta:\n\n{contexto}\n\nPergunta: {pergunta}\nResposta:",
        max_tokens=150
    )
    
    return resposta.choices[0].text.strip()

if __name__ == "__main__":
    # Exemplo de uso
    contexto = "O conceito de inteligência artificial refere-se ao estudo de sistemas computacionais..."
    pergunta = "O que é inteligência artificial?"
    resposta = gerar_resposta(pergunta, contexto)
    print(resposta)
