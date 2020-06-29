from datetime import datetime


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    # Funções dentro de classes são chamadas de métodos
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar porque está comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        if self.falando:
            print(f'{self.nome} não pode comer pois está falando.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def get_ano_nascimento(self):
        print(f'{self.nome} nasceu em {self.ano_atual - self.idade}')


# Cada pessoa é uma instância da Classe Pessoa e tem suas próprias
# características (atributos)

pessoa1 = Pessoa('Levy', 19)
pessoa1.comer('abacate')
pessoa1.parar_comer()
pessoa1.falar('programação')
pessoa1.get_ano_nascimento()

print('-'*50)

pessoa2 = Pessoa('Geovana', 16)
pessoa2.comer('melancia')
pessoa2.parar_comer()
pessoa2.falar('séries')
pessoa2.get_ano_nascimento()
