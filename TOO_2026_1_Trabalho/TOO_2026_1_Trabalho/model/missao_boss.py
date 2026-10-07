from model.missao import Missao
from model.enums import StatusMissao

class MissaoBoss(Missao):
    XP_POR_FASE = 30  # XP extra para cada fase da batalha contra o chefe

    def __init__(self, nome, descricao, recompensa, fases):
        super().__init__(nome, descricao, recompensa)
        self.__fases = None
        self.fases = fases  # passa pelo setter (validação)

    @property
    def fases(self):
        return self.__fases

    @fases.setter
    def fases(self, valor):
        if not isinstance(valor, int):
            raise TypeError("O número de fases deve ser um número inteiro.")
        if valor < 1:
            raise ValueError("O chefe precisa ter pelo menos 1 fase.")
        self.__fases = valor

    def calcular_recompensa(self):
        base = super().calcular_recompensa()
        if self.status is not StatusMissao.CONCLUIDA:
            return 0
        return base + self.fases * self.XP_POR_FASE
        
    def exibir_dados(self):
        return f'''
Dados da missão de Boss:
{super().exibir_dados()}
Fases da batalha: {self.fases}
'''

    def __str__(self):
        return self.exibir_dados()