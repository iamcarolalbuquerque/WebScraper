from webscrapers import MLWebScraper
import pandas as pd


# URL que queremos fazer o web scrape
base_url = 'https://lista.mercadolivre.com.br/veiculos/carros-caminhonetes/chevrolet/celta-em-sao-paulo/celta-2012-completo'
search_filter = '_PriceRange_10001-0'

mlws = MLWebScraper()
data = pd.DataFrame()

# Obtém as urls da paginação do site
# Esse método é propositalmente lento para evitar que o site nos marque como spammers :)
urls = mlws.get_urls(base_url,search_filter)

# Obtém os dados relevantes itens ofertados
for url in urls:
    data = data.append(mlws.get_data(url))


# print(data[['name', 'city', 'price']])
# print(data['city'].drop_duplicates().sort_values())

data[['name', 'city', 'price']].to_csv('../products.csv', index=False)


    