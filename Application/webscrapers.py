from bs4 import BeautifulSoup
import requests
import time
import pandas as pd


# Classe para web scraping do site Mercado Livre
class MLWebScraper:
    def __init__(self):

        # O site Mercado Livre lista 48 itens por página
        self.__items_per_page__ = 48

    
    def remove_city_zone(self, city):

            zone_list = ['Zona Sul', 'Zona Leste', 'Zona Norte', 'Zona Oeste', 'Centro']

            for zone in zone_list:
                if zone in city: 
                    city = city.replace(zone, '').strip()

            return city

    
    def get_urls(self, base_url, search_filters):
        urls = []
        
        item_index = 1
        current_url = base_url + search_filters

        try:
            response = requests.get(current_url)

            while response.status_code == 200:
                
                urls.append(current_url)

                # Uma pausa se um segundo para evitar que sejamos taxados pelo site como spammer :)
                time.sleep(1)
                
                # Nas páginas seguintes da busca (diferentes da primeira), é feito um controle do índice do 
                # primeiro item a ser exibido:
                current_url = base_url+ '_Desde_' + str(self.__items_per_page__ + item_index) +  search_filters
                item_index += self.__items_per_page__

                response = requests.get(current_url)

        except:
             print('URL inválida.')

        return urls
    
    def get_data(self, url):
        data = pd.DataFrame(columns=['item_title', 'item_attrs', 'item_location', 'item_currency', 'item_price'])

        try:
            response = requests.get(url)

            # Analiza o HTML e o salva como um objeto BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")


            # Encontra os itens listados na página
            items = soup.findAll ("div", { "class" : "item__info" })


            # Para cada item, adiciona seus dados num dataframe, 
            # fazendo ainda um tratamento básico de strings.
            for i in range(len(items)) :
                
                data = data.append({'item_title' : items[i].find("span", { "class" : "main-title" }).get_text().strip(),
                    'item_attrs' : items[i].find("div", { "class" : "item__attrs" }).get_text().strip(),
                    'item_location' : self.remove_city_zone(items[i].find("div", { "class" : "item__location" }).get_text().strip()),
                    'item_currency' : items[i].find("span", { "class" : "price__symbol" }).get_text(),
                    'item_price': items[i].find("span", { "class" : "price__fraction" }).get_text().replace('.','')}, ignore_index=True)
         
        
        except Exception as e:
            print(str(e))

        return data
        


        
    