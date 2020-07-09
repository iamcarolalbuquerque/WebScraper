from webscrapers import MLWebScraper


# URL que queremos fazer o web scrape
base_url = 'https://lista.mercadolivre.com.br/veiculos/carros-caminhonetes/chevrolet/celta/celta-2012-completo'
search_filter = '_PriceRange_10001-0'

mlws = MLWebScraper()

# Obtém as urls da paginação do site
urls = mlws.get_urls(base_url,search_filter)
data = []

# Obtém os dados relevantes itens ofertados
for url in urls:
    data.extend (mlws.get_data(url))


print(len(data))
print(data[1])
#print(*data, sep = ", ")
    