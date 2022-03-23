from datetime import datetime
from enum import Enum
import logging
import logging.config
import os
import yaml


class LogHandlers:
    CONSOLE = 1
    LOGFILE = 2
    HEROKU = 3
    

class Logger:
    def __init__(self, handler: LogHandlers, mod_name: str) -> None:
        self.__handler = handler
        self_timestamp = datetime.now().strftime("%Y-%m-%d")
        self._current_dir = os.path.abspath(os.getcwd())
        self._log_dir = os.path.join(os.path.dirname(__file__))
        self._log_config = []
        self._logger = ""
        self._mod_name = mod_name
        self._init_config()
 
    def _init_config(self) -> None:
        with open(f"{self._log_dir}/log-config.yml", "r") as fh:
            self._log_config = yaml.safe_load(fh)
        
        logging.config.dictConfig(self._log_config)
        #self._logger = logging.getLogger("root")
        self._logger = logging.getLogger(self._mod_name)
        
    
    def _file_config(self) -> None:
        pass
    
    def info(self, msg, *args, **kwargs):
        self._logger.info(msg, *args, **kwargs)
        
    def critical(self, msg, *args, **kwargs):
        self._logger.critical(msg, *args, **kwargs)