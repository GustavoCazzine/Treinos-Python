import random

jogadas = ["pedra", "papel", "tesoura"]

def jogar_maquina():
    jogada = random.choice(jogadas)
    return jogada

def definir_vencedor(jogada_1, jogada_2):
    if jogada_1 == jogada_2:
        return "Empate"
    
    condicoes_jogadas = [
        (jogada_1 == "pedra" and jogada_2 == "tesoura"),
        (jogada_1 == "tesoura" and jogada_2 == "papel"),
        (jogada_1 == "papel" and jogada_2 == "pedra")
    ]

    if any(condicoes_jogadas):
        return "Jogador 1"
    else:
        return "Jogador 2"
    
def validar_jogada(jogada_usuario):
    jogadas_validas = ["pedra", "papel", "tesoura"]
    return jogada_usuario in jogadas_validas
