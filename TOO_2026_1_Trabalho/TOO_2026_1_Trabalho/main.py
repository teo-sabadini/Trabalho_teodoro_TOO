from model.heroi import Heroi
from model.missao import Missao
from model.inimigo import Inimigo
from model.enums import ClasseHeroi, TipoInimigo, StatusMissao
from model.missao_exploracao import MissaoExploracao
from model.missao_boss import MissaoBoss
from model.missao_defesa import MissaoDefesa

def main():
    heroi = Heroi("Armando", ClasseHeroi.MAGO, 100, 100, 15, 5)

    missoes = [
        MissaoExploracao("Ruínas Esquecidas", "explorar as ruínas e chegar ao fim da dungeon", 100, 3),
        MissaoDefesa("Defesa do Reino", "proteger o reino do ataque dos orcs", 80, "reino"),
        MissaoBoss("Smaug", "derrotar o dragão da montanha", 150, 3),
    ]

    print("=" * 50)
    print("MISSÕES DISPONÍVEIS")
    print("=" * 50)
    for missao in missoes:
        print(missao.exibir_dados())
        print(f"Recompensa agora: {missao.calcular_recompensa()} XP (ainda não concluída)")

    # 2) Ciclo completo de uma missão até o herói subir de nível
    print("\n" + "=" * 50)
    print("CICLO COMPLETO DA MISSÃO")
    print("=" * 50)
    missao = missoes[0]
    print("ANTES:")
    print(heroi.exibir_dados())

    print(missao.iniciar_missao())
    missao.concluir_missao(heroi)
    print(f"XP pago pela missão: {missao.calcular_recompensa()}")

    print("\nDEPOIS:")
    print(heroi.exibir_dados())

    # 3) Erros provocados de propósito, tratados com try/except
    print("=" * 50)
    print("TESTES DE ERRO")
    print("=" * 50)

    try:
        print("Tentando concluir a missão do dragão sem iniciá-la...")
        missoes[2].concluir_missao(heroi)
    except ValueError as erro:
        print(f"Erro: {erro}")

    try:
        print("\nTentando concluir a missão das ruínas de novo...")
        missoes[0].concluir_missao(heroi)
    except ValueError as erro:
        print(f"Erro: {erro}")

    try:
        print("\nTentando alterar o status com um texto em vez do enum...")
        missoes[1].status = "Concluida"
    except TypeError as erro:
        print(f"Erro: {erro}")

    try:
        print("\nTentando pular direto de Pendente para Concluída...")
        missoes[1].status = StatusMissao.CONCLUIDA
    except ValueError as erro:
        print(f"Erro: {erro}")

    try:
        print("\nTentando criar uma exploração com dificuldade 9...")
        MissaoExploracao("Dungeon Impossível", "sobreviver", 100, 9)
    except ValueError as erro:
        print(f"Erro: {erro}")

    # 4) Terminando as demais missões com o mesmo método
    print("\n" + "=" * 50)
    print("CONCLUINDO AS OUTRAS MISSÕES")
    print("=" * 50)
    for missao in missoes[1:]:
        print(missao.iniciar_missao())
        missao.concluir_missao(heroi)
        print(f"XP pago: {missao.calcular_recompensa()}\n")

    print(heroi.exibir_dados())


    
main()