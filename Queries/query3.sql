/* LISTAR OS 5 PRODUTOS MAIS BARATOS E O MAIS CARO */

WITH ofertas AS
((SELECT name AS Produto, city AS Cidade, price AS Preco
FROM `data-challenge-zenklub.cds.products`
ORDER BY price, city ASC LIMIT 5)
UNION ALL
(SELECT name AS Produto, city AS Cidade, price AS Preco
FROM `data-challenge-zenklub.cds.products`
ORDER BY price DESC, city ASC LIMIT 1))
SELECT * FROM ofertas