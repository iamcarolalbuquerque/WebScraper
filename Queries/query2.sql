/* QUAL A CIDADE QUE POSSUI MAIS PRODUTOS OFERTADOS */

SELECT city AS Cidade, COUNT(1) AS NumReg
FROM `data-challenge-zenklub.cds.products`
GROUP BY city
ORDER BY NumReg DESC, city ASC LIMIT 1
