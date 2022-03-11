from decouple import config

class EnvData:
    @staticmethod
    def get_url():
        try:
            return config("RFB_URL")
        except:
            #TODO
            print("url not found")