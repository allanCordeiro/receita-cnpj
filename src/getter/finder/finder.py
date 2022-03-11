from scrapper import Scrapper

class Finder:
    def __init__(self):
        self.__scrapper = Scrapper()        
    
    def get_links_list(self) -> list:
        return self.__scrapper.get_links()