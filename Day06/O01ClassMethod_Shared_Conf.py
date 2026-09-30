
class AppSettings:
    # shared by all instances
    config = {}

    @classmethod
    def set_config(cls, api_key, base_url):
        cls.config["api_key"] = api_key
        cls.config["base_url"] = base_url

    def show_config(self):
        print(f"Using API :{self.config['api_key']} at {self.config['base_url']}" )

AppSettings.set_config("XYS123", "https//api.example.com")

s1 = AppSettings()
s2 = AppSettings()

s1.show_config()
s2.show_config()

AppSettings.set_config("MYKEY@123", "https//api.products.com")

s3 = AppSettings()
s3.show_config()

s1.show_config()
s2.show_config()