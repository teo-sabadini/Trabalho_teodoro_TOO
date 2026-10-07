from model.missao import Missao
from model.enums import StatusMissao

class MissaoExploracao(Missao):
    NIVEL_MINIMO = 1
    NIVEL_MAXIMO = 5
    XP_POR_NIVEL = 20

    def __init__(self, nome, descricao, recompensa, dificuldade_dungeon):
        super().__init__(nome, descricao, recompensa)
        self.__dificuldade_dungeon = None
        self.dificuldade_dungeon = dificuldade_dungeon

    @property
    def dificuldade_dungeon(self):
        return self.__dificuldade_dungeon

    @dificuldade_dungeon.setter
    def dificuldade_dungeon(self, valor):
        if not isinstance(valor, int):
            raise TypeError("A dificuldade deve ser um número inteiro.")
        if valor < self.NIVEL_MINIMO or valor > self.NIVEL_MAXIMO:
            raise ValueError(
                f"A dificuldade deve estar entre {self.NIVEL_MINIMO} e {self.NIVEL_MAXIMO}."
            )
        self.__dificuldade_dungeon = valor

    def calcular_recompensa(self):
        base = super().calcular_recompensa()
        if self.status is not StatusMissao.CONCLUIDA:
            return 0
        return base + self.dificuldade_dungeon * self.XP_POR_NIVEL

    def exibir_dados(self):
        return f'''
Dados da missão de exploração:
{super().exibir_dados()}
Dificuldade da dungeon: {self.__dificuldade_dungeon}/{self.NIVEL_MAXIMO}
'''

    def __str__(self):
        return self.exibir_dados()