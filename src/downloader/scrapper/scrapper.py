from bs4 import BeautifulSoup
from datetime import datetime
from urllib.error import HTTPError
import requests


class Scrapper:
    def __init__(self, url):
        self.__url = url
        self.__page_content = ""
                
            
    def get_last_modification_date(self) -> datetime:
        self._get_parsed_content()
        content = self.__page_content.find_all(
            "span", class_="documentModified"
            )
        for span_data in content:
            date_string = span_data.find("span", class_="value")
            date_string = date_string.get_text().split(" ")[0]
            return datetime.strptime(date_string, "%d/%m/%Y")
    
    
    def _get_parsed_content(self) -> None:
        page = self._get_page_content()        
        self.__page_content = BeautifulSoup(page.content, "html.parser")
        
    
    def _get_page_content(self) -> requests.models.Response:
        try:
            return requests.get(self.__url)
        except HTTPError as http_error:
            #TODO
            print("TODO")
            