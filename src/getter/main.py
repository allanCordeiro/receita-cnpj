from datechecker import DateChecker
from finder import Finder
from persister import Persister
from utils.logger import Logger, LogHandlers
import wget


def downloader_poc():
    log = Logger(__name__)   
    url = "http://200.152.38.155/CNPJ/K3241.K03200Y0.D20212.ESTABELE.zip"          
    log.info("testando o download")
    try:
        wget.download(url, '/home/allan/Documentos/Dev/Estudos/data-eng/receita-cnpj/datalake/bronze')
    except Exception as e:
        log.critical(f"Deu erro grande aqui {e}")    
    
    
if __name__ == "__main__":
    #log = Logger(LogHandlers.CONSOLE, __name__)    
    datechecker = DateChecker()
    links = Finder()
    save = Persister()
    if (datechecker.is_new_data_available()):        
        lista_links = links.get_links_list()
        save.insert(lista_links)
    #log.info("não há dados para persistir")
    downloader_poc()
        