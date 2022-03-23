from datetime import datetime 
from dbcore import core
from scrapper import Scrapper
from sqlalchemy.sql import text
from utils.logger import Logger, LogHandlers



class DateChecker:
    def __init__(self):        
        self.__scrapper = Scrapper()        
        self.__conn = core.engine.connect()        
        self._last_db_date = datetime(1901, 1, 1)
        self._logger = Logger(__name__)
    
    @property
    def last_db_date(self):
        return self._last_db_date
            
    def is_new_data_available(self) -> bool:
        last_site_update = self.__scrapper.get_last_modification_date()    
        self._last_db_date = self._get_last_db_date()        
        self._logger.info(f"last db date info: {self.last_db_date}")
        if self.last_db_date < last_site_update:            
            return True
        return False
    
    def _get_last_db_date(self) -> list:
        query = text(
            "SELECT created_at FROM available_links" \
            " ORDER BY created_at DESC LIMIT 1")        
        try:
            get_date = self.__conn.execute(query).fetchall()
            return self._get_transformed_date(get_date)
        except IndexError:
            self._logger.info("Fresh data. Start to get some info.")
            return self.last_db_date
        
    
    def _get_transformed_date(self, date: list) -> datetime:
        (date_value) = date[0]        
        last_date = self._reset_time(date_value.created_at)
        return last_date
    
    def _reset_time(self, date_info: datetime) -> datetime:
        return date_info.replace(hour=0, minute=0, second=0, microsecond=0)      
        
    