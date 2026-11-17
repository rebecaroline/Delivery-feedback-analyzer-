# 🍔 Delivery Feedback Analyzer

Pipeline em Python que utiliza Engenharia de Prompts e LLMs (Large Language Models) para classificar avaliações de clientes de delivery, extrair sentimentos e identificar gargalos operacionais automaticamente.

## 🚀 Objetivo
Demonstrar a aplicação prática de Inteligência Artificial Generativa na resolução de problemas reais de produto e análise de dados, transformando textos não estruturados em métricas acionáveis.

## 🛠️ Tecnologias Utilizadas
* **Python 3**
* **Pandas** (manipulação e estruturação dos dados)
* **JSON** (saída estruturada para integração com pipelines e dashboards)
* **Prompt Engineering** (classificação zero-shot e extração de entidades)

## ⚙️ Como funciona
1. Lê uma base de avaliações de clientes.
2. Aplica um prompt estruturado exigindo retorno em formato **JSON** contendo: `sentimento`, `categoria` (Entrega, Pedido/Qualidade, Aplicativo, Atendimento) e `prioridade_acao`.
3. Consolida os resultados para visualização rápida e tomada de decisão pela equipe de produto.
