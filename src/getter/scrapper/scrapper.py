from bs4 import BeautifulSoup
from datetime import datetime
from urllib.error import HTTPError
from utils import EnvData, Logger

import requests


class Scrapper:
    def __init__(self):
        self.__url = EnvData.get_env("RFB_URL")        
        self.__page_content = ""
        self.__links_list = list()
        self.__logger = Logger(__name__)
                
            
    def get_last_modification_date(self) -> datetime:
        self._get_parsed_content()
        content = self.__page_content.find_all(
            "span", class_="documentModified"
            )
        for span_data in content:
            date_string = span_data.find("span", class_="value")
            date_string = date_string.get_text().split(" ")[0]
            return datetime.strptime(date_string, "%d/%m/%Y")
        
    
    
    def get_links(self) -> list:
        self._get_parsed_content()
        content = self.__page_content.find_all("a", class_="external-link")
        for item in content:
            file_property = {}
            file_property['name'] = self._get_text_fixed(item.get_text())
            file_property['link'] = item.get('href')
            self.__links_list.append(file_property)
        
        return self.__links_list
   
    
    def _get_text_fixed(self, text) -> str:
        return text.replace(u'\xa0', ' ')
    
    def _get_parsed_content(self) -> None:
        page = self._get_page_content()        
        self.__page_content = BeautifulSoup(page.content, "html.parser")
        
    
    def _get_page_content(self) -> requests.models.Response:
        try:
            return requests.get(self.__url)
        except HTTPError as http_error:
            self.__logger.critical("Error during scrapping process.")
            
            