from google.cloud import bigquery
import os

# Caso não esteja configurado nas variáveis de ambiente, explicitar a chave de acesso:
# TODO: o programador deve alterar antes de executar esse código
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/caminho-para-o-arquivo.json"

# Inicializando o cliente BigQuery
client = bigquery.Client()

# Nome completo da tabela
# TODO: o programador deve alterar antes de executar esse código
table_ref = "projeto.dataset.tabela"

# PREÇO MÉDIO DO PRODUTO POR CIDADE
query1 = """
        SELECT city AS Cidade, ROUND(AVG(price), 2) AS Valor_Medio
        FROM `?`
        GROUP BY city
        ORDER BY city ASC
        """

# QUAL A CIDADE QUE POSSUI MAIS PRODUTOS OFERTADOS
query2 = """
        SELECT city AS Cidade, COUNT(1) AS NumReg
        FROM `?`
        GROUP BY city
        ORDER BY NumReg DESC, city ASC LIMIT 1
        """

# LISTAR OS 5 PRODUTOS MAIS BARATOS E O MAIS CARO
query3 = """
        WITH ofertas AS
        ((SELECT name AS Produto, city AS Cidade, price AS Preco
        FROM `?`
        ORDER BY price, city ASC LIMIT 5)
        UNION ALL
        (SELECT name AS Produto, city AS Cidade, price AS Preco
        FROM `?`
        ORDER BY price DESC, city ASC LIMIT 1))
        SELECT * FROM ofertas
        """

# Executando e exibindo os resultados das queries:

query_job = client.query(query1.replace('?',table_ref))
query_result = query_job.to_dataframe()

print(query_result)

query_job = client.query(query2.replace('?',table_ref))
query_result = query_job.to_dataframe()

print(query_result)

query_job = client.query(query3.replace('?',table_ref))
query_result = query_job.to_dataframe()

print(query_result)

