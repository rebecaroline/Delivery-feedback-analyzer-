import json
import pandas as pd

# Simulação de base de dados de avaliações de clientes
dados_feedbacks = [
    {"id": 1, "comentario": "A comida chegou quentinha e muito antes do prazo! Adorei."},
    {"id": 2, "comentario": "O entregador demorou 40 minutos a mais e o refrigerante veio errado."},
    {"id": 3, "comentario": "O aplicativo travou na hora de aplicar o cupom de desconto."},
    {"id": 4, "comentario": "Excelente atendimento do restaurante, mandaram até bilhete."}
]

def gerar_prompt_analise(comentario: str) -> str:
    """Cria um prompt estruturado para extração de insights via LLM."""
    return f"""
    Analise o seguinte feedback de cliente de delivery e retorne APENAS um JSON válido com as chaves:
    - "sentimento": ("Positivo", "Neutro" ou "Negativo")
    - "categoria": ("Entrega", "Pedido/Qualidade", "Aplicativo" ou "Atendimento")
    - "prioridade_acao": ("Alta", "Média" ou "Baixa")

    Feedback: "{comentario}"
    """

def processar_feedbacks(lista_dados: list) -> pd.DataFrame:
    resultados = []
    for item in lista_dados:
        prompt = gerar_prompt_analise(item["comentario"])
        # Estrutura pronta para integração com API de LLM (ex: Gemini / OpenAI)
        resposta_estruturada = {
            "id": item["id"],
            "comentario": item["comentario"],
            "prompt_gerado": prompt.strip()
        }
        resultados.append(resposta_estruturada)
    
    return pd.DataFrame(resultados)

if __name__ == "__main__":
    df_resultado = processar_feedbacks(dados_feedbacks)
    print("Pipeline de análise de feedbacks concluído com sucesso!")
    print(df_resultado[["id", "comentario"]].to_string(index=False))
