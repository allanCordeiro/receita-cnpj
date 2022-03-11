from datetime import datetime 

from bs4 import BeautifulSoup
from scrapper import Scrapper


class DateChecker:
    def __init__(self):
        
        self.__scrapper = Scrapper()        
        #TODO:: esta data vai ficar persistida em algum lugar
        self._last_database_date = datetime(2022, 2, 10)            
    
    def is_new_data_available(self) -> bool:
        last_site_update = self.__scrapper.get_last_modification_date()        
        if self._last_database_date < last_site_update:
            return True
        return False
    
    
    
            
        
    