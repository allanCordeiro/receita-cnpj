from datechecker import DateChecker
from finder import Finder
from persister import Persister
import wget



def downloader_poc():
    url = "http://200.152.38.155/CNPJ/K3241.K03200Y9.D20212.ESTABELE.zip"
    wget.download(url, '/home/allan/Documentos/Dev/Estudos/data-eng/receita-cnpj/datalake/bronze')
    

    


if __name__ == "__main__":    
    datechecker = DateChecker()
    links = Finder()
    save = Persister()
    if (datechecker.is_new_data_available()):
        lista_links = links.get_links_list()
        save.insert(lista_links)
        for link in lista_links:
            print(link)    