# WebScraper

Essa aplicação em Python realiza o webscraping a partir de um link de uma busca de produto no site Mercado Livre. Os dados coletados são armazenados num arquivo .csv para, em seguida, serem carregados em uma base de dados BigQuery (o carregamento destes foi feito via console do Google Cloud). Também são realizadas consultas nesses dados para obter-se informações relevantes sobre a busca realizada.

## Pré-requisitos
Considerando que o Python e o pip estão devidamente instalados e em suas versões atualizadas, é necessário instalar as seguintes bibliotecas:
```
pip install requests

pip install beautifulsoup4

pip install pandas
```
e para quem vai realizar as consultas via Python:
```
pip install google-cloud-storage

pip install google-cloud-bigquery
```

## Execução
Para o webscraping, basta executar **Application/main.py**.

Para as consultas, podem ser feitas de duas formas:
- executando o arquivo **Queries/queries.py** _ou_
- executando as consultas salvas nos arquivos .sql diretamente no console do BigQuery no Google Cloud.
