from model.missao import Missao
from model.enums import StatusMissao

class MissaoDefesa(Missao):
    # XP extra de acordo com o que está sendo defendido
    BONUS_ALVO = {"reino": 50, "pessoa": 30}

    def __init__(self, nome, descricao, recompensa, reino_ou_pessoa):
        super().__init__(nome, descricao, recompensa)
        self.__reino_ou_pessoa = None
        self.reino_ou_pessoa = reino_ou_pessoa  # passa pelo setter (validação)

    @property
    def reino_ou_pessoa(self):
        return self.__reino_ou_pessoa

    @reino_ou_pessoa.setter
    def reino_ou_pessoa(self, valor):
        valor = str(valor).lower()
        if valor not in self.BONUS_ALVO:
            raise ValueError("O alvo da defesa deve ser 'reino' ou 'pessoa'.")
        self.__reino_ou_pessoa = valor

    def calcular_recompensa(self):
        base = super().calcular_recompensa()
        if self.status is not StatusMissao.CONCLUIDA:
            return 0
        return base + self.BONUS_ALVO[self.reino_ou_pessoa]

    
    def exibir_dados(self):
        return f'''
Dados da missão de defesa:
{super().exibir_dados()}
Alvo da defesa: {self.__reino_ou_pessoa}
'''

    def __str__(self):
        return self.exibir_dados()