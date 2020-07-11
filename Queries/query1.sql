/* PREÇO MÉDIO DO PRODUTO POR CIDADE */

SELECT city AS Cidade, ROUND(AVG(price), 2) AS Valor_Medio
FROM `data-challenge-zenklub.cds.products`
GROUP BY city
ORDER BY city ASC