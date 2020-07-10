from webscrapers import MLWebScraper
import pandas as pd


# URL que queremos fazer o web scrape
base_url = 'https://lista.mercadolivre.com.br/veiculos/carros-caminhonetes/chevrolet/celta-em-sao-paulo/celta-2012-completo'
search_filter = '_PriceRange_10001-0'

mlws = MLWebScraper()
data = pd.DataFrame()

# Obtém as urls da paginação do site
urls = mlws.get_urls(base_url,search_filter)

# Obtém os dados relevantes itens ofertados
for url in urls:
    data = data.append(mlws.get_data(url))


print(data[['item_title', 'item_location', 'item_price']])

# print(data['item_location'].drop_duplicates().sort_values())
    