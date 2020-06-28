import requests


class repositoriesList():

    def __init__(self, user):
        self.user = user

    def api_request(self):
        response = requests.get(
            f'https://api.github.com/users/{self.user}/repos')
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def print_repositories(self):
        dados_api = self.api_request()
        if type(dados_api) is not int:
            for i in range(len(dados_api)):
                print(dados_api[i]['name'])
        else:
            print(dados_api)


repositories = repositoriesList('levyaraujo')
repositories.print_repositories()
