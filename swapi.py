import requests
import os


class APIRequester:

    def __init__(self, base_url):
        self.base_url = base_url
        self.response = None

    def get(self):
        try:
            response = requests.get(self.base_url, verify=False)
            response.raise_for_status()
            self.response = response.json()
        except requests.RequestException as e:
            print(f'Ошибка при выполнении запроса: {e}')
            self.response = None


class SWRequester(APIRequester):
    url = 'https://swapi.dev/api/'
    base_url = url

    def __init__(self):
        super().__init__(self.base_url)

    def get_sw_categories(self):
        self.get()
        return self.response

    def get_sw_info(self, sw_type):
        self.base_url = self.url + sw_type
        self.get()
        return self.response


def save_sw_data():
    item = SWRequester()
    os.makedirs("data", exist_ok=True)
    categories = item.get_sw_categories()
    cats = list(categories.keys())
    print(cats)
    for i in cats:
        info = item.get_sw_info(i)
        file_name = 'data/' + i + '.txt'
        with open(file_name, 'w') as f:
            f.write(str(info))


save_sw_data()
