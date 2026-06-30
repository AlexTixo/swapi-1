import requests
import os


class APIRequester:

    def __init__(self, base_url):
        self.base_url = base_url
        self.response = None

    def get(self, endpoint):
        full_url = self.base_url + endpoint
        try:
            response = requests.get(full_url, verify=False)
            response.raise_for_status()
            self.response = response.json()
        except requests.RequestException:
            print('Возникла ошибка при выполнении запроса')
            self.response = None
        print(full_url)
        return self.response


class SWRequester(APIRequester):

    def __init__(self, base_url='https://swapi.dev/api'):
        super().__init__(base_url)

    def get_sw_categories(self):
        return self.get('/')

    def get_sw_info(self, sw_type):
        return self.get('/'+sw_type+'/') 


def save_sw_data():
    item = SWRequester()
    os.makedirs("data", exist_ok=True)
    categories = item.get_sw_categories()
    cats = list(categories.keys())
    for i in cats:
        info = item.get_sw_info(i)
        file_name = 'data/' + i + '.txt'
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(str(info))
        print(f'Данные для {i} сохранены в {file_name}')


save_sw_data()
