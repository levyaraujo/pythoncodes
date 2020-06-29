from datetime import datetime


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    # Funções dentro de classes são chamadas de métodos
    def __init__(self, name, idade, comendo=False, falando=False, premium=False):
        self.name = name
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.premium = premium

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.name} não pode falar porque está comendo.')
            return

        if self.falando:
            print(f'{self.name} já está falando.')
            return

        print(f'{self.name} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.name} não está falando')
            return

        print(f'{self.name} parou de falar.')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.name} já está comendo.')
            return

        if self.falando:
            print(f'{self.name} não pode comer pois está falando.')
            return

        print(f'{self.name} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.name} não está comendo.')
            return

        print(f'{self.name} parou de comer.')
        self.comendo = False

    def get_ano_nascimento(self):
        print(f'{self.name} nasceu em {self.ano_atual - self.idade}')

    def is_premium(self):
        if self.name == 'Levy':
            self.premium = True
            print(f'{self.name} é um usuário premium')
        else:
            print(f'{self.name} não é um usuário premium')

        self.premium = False

# Cada pessoa é uma instância da Classe Pessoa e tem suas próprias
# características (atributos)


pessoa1 = Pessoa('Levy', 19)
pessoa1.comer('abacate')
pessoa1.parar_comer()
pessoa1.falar('programação')
pessoa1.get_ano_nascimento()
pessoa1.is_premium()

print('-'*50)

pessoa2 = Pessoa('Geovana', 16)
pessoa2.comer('melancia')
pessoa2.parar_comer()
pessoa2.falar('séries')
pessoa2.get_ano_nascimento()
pessoa2.is_premium()
