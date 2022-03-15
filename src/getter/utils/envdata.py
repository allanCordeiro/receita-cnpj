from decouple import config

class EnvData:
    @staticmethod
    def get_env(env_name: str) -> str:
        try:
            return config(env_name)
        except:
            #TODO
            print("config not found")
            
