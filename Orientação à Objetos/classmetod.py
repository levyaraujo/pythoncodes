class User:

    ano_atual = 2020

    def __init__(self, name, idade):
        self.name = name
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod  # Decorador
    def por_ano_nascimento(cls, nome, nascimento):
        idade = cls.ano_atual - nascimento
        return cls(nome, idade)
