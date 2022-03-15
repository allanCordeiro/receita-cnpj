from .db import core

class Persister:
    def __init__(self):
        self.__conn = core.engine.connect()
        self.__ins = core.available_links.insert() 
    
    def insert(self, data: list) -> None:
        self.__conn.execute(
            self.__ins, data)
        