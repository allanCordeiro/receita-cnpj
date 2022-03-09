from bs4 import BeautifulSoup
from datechecker import DateChecker
import requests
import wget


def downloader_poc():
    url = "http://200.152.38.155/CNPJ/K3241.K03200Y9.D20212.ESTABELE.zip"
    wget.download(url, '/home/allan/Documentos/Dev/Estudos/data-eng/receita-cnpj/datalake/bronze')
    
def scrapping_poc():
    url = "https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj"
    page = requests.get(url)    
    soup = BeautifulSoup(page.content, "html.parser")
    print(type(soup))
    #print(soup.prettify())
    result = soup.find_all("a", class_="external-link")
    link_list = []
    for item in result:
        link = {}
        link['item_name'] = item.get_text().replace(u'\xa0', ' ')
        link['item_link'] = item.get('href')
        link_list.append(link)
    


if __name__ == "__main__":
    #scrapping_poc()
    datechecker = DateChecker()
    print(datechecker.is_new_data_available())
    