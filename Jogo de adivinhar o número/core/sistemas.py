import random

#Sortear um número de 1 a 100 atravez da biblioteca random
def sortear_numero(numero_maximo):
    numero_sorteado = random.randint(0, numero_maximo)
    return numero_sorteado

#Avaliar se acerto é correto // Parametros palpite do usuario e numero sorteado
def avaliar_palpite(palpite_usuario, numero_sorteado):
    palpite = "certo" if numero_sorteado == palpite_usuario else "errado"
    if palpite == "errado":
        if palpite_usuario > numero_sorteado:
            return "maior"
        else:
            return "menor"
    else:
        return palpite

#tratamento de erro simples para receber apenas números inteiros
def retornar_inteiro(numero):
    try:
        return int(numero)
    except ValueError:
        return f"Insira um número inteiro! Tente novamente."
    
def config_game():
    numero_maximo = input("Até qual número posso escolher: ")
    numero_maximo = retornar_inteiro(numero_maximo)
    return numero_maximo