# Scryfall Cards Data Collector

Este projeto utiliza a API do [Scryfall](https://scryfall.com/docs/api) para fazer requisições e coletar dados de cartas do popular jogo de cartas Magic: The Gathering (MTG). Com ele, você pode facilmente pesquisar cartas com parâmetros personalizados e organizar os dados em um `DataFrame` do pandas, facilitando a análise de preços, raridade, cores e outros atributos das cartas.

## Funcionalidades

- **Busca de cartas personalizada**: Especifique parâmetros como tipo de carta, cor, raridade, e habilidades de jogo.
- **Criação de DataFrame**: Extrai dados das cartas e organiza em um `DataFrame` do pandas com atributos como nome, tipo, data de lançamento, preço em dólar, custo de mana convertido, cores e raridade.
- **Exploração e análise de dados**: O `DataFrame` permite realizar uma análise mais profunda dos dados das cartas para diferentes propósitos, como avaliação de mercado, coleções e estudos estatísticos.

## Como Usar

### 1. Pré-requisitos
Este projeto requer o Python e as bibliotecas `requests` e `pandas`. Instale as bibliotecas com:
```bash
pip install requests pandas
