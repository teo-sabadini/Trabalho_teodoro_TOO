from model.enums import StatusMissao

class Missao:
    def __init__(self, nome, descricao, recompensa):
        self.__nome = nome
        self.__descricao = descricao
        self.__recompensa = recompensa
        self.__status = StatusMissao.PENDENTE

    @property
    def nome(self): 
        return self.__nome
    
    @property
    def descricao(self): 
        return self.__descricao
    
    @property
    def recompensa(self): 
        return self.__recompensa

    @property
    def status(self): 
        return self.__status

    #Criei um setter aqui, para o atributo status, pois ele pode receber alterações ao decorrer da missão.
    @status.setter
    def status(self, stat):
        if stat == self.__status:
            raise ValueError(f"O status da missão já é '{self.__status.value}'.")

        elif not isinstance(stat, StatusMissao):
            raise TypeError("Você precisa selecionar o ENUM 'StatusMissao'. Outro tipo de dado é inválido.")
        
        elif self.__status == StatusMissao.PENDENTE:
            if stat != StatusMissao.EM_ANDAMENTO:
                raise ValueError(f"A missão está '{StatusMissao.PENDENTE.value}', seu status só pode ser alterado para '{StatusMissao.EM_ANDAMENTO.value}'.")
             
        elif self.__status == StatusMissao.EM_ANDAMENTO:
            if stat != StatusMissao.CONCLUIDA:
                raise ValueError(f"A missão está '{StatusMissao.EM_ANDAMENTO.value}', seu status só pode ser alterado para '{StatusMissao.CONCLUIDA.value}'.")
            
        elif self.__status == StatusMissao.CONCLUIDA:
            raise ValueError(f"A missão já está '{StatusMissao.CONCLUIDA.value}', não pode ter seu status alterado.")
        
        self.__status = stat

    def iniciar_missao(self):
        if self.status == StatusMissao.PENDENTE:
            self.status = StatusMissao.EM_ANDAMENTO
            return f"A missão {self.nome} começou! O objetivo é {self.descricao}."
        else:
            return f'A missão {self.nome} já foi iniciada!!!'

    def calcular_recompensa(self):
        if self.status is not StatusMissao.CONCLUIDA:
            return 0
        return self.recompensa

    def concluir_missao(self, heroi):
        if self.status == StatusMissao.CONCLUIDA:
            raise ValueError(f"A missão já está '{StatusMissao.CONCLUIDA.value}', não receberá a recompensa novamente.")
    
        self.status = StatusMissao.CONCLUIDA
        heroi.ganhar_experiencia(self.calcular_recompensa())
        print(f"Missão '{self.nome}' concluída. {heroi.nome} obteve a recompensa e ganhou o xp.")
    
    def exibir_dados(self):
        msg = f'''
[{self.__class__.__name__}]
Nome: {self.nome}
Descrição: {self.descricao}
Recompensa: {self.recompensa}
Status: {self.status.value}'''

        return msg

    def __str__(self):
        return f'missão [{self.__class__.__name__}]: {self.nome} | status: {self.status}'


    