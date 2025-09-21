from core.sistemas import sortear_numero, avaliar_palpite, retornar_inteiro, config_game
from utils.interface import limpar_tela, criar_titulo, delay

#jogo simples de adivinhação
def main():
    criar_titulo("Adivinhação de números")
    delay(.5)
    print("\nVamos configurar seu jogo antes de iniciar.\n")
    delay(.5)
    venceu = False
    while True:
        if venceu:
            break
        else:
            numero_maximo = config_game()
            if isinstance(numero_maximo, int):
                numero_sorteado = sortear_numero(numero_maximo)
                tentativas_usuario = 0
                
                while True:
                    tentativas_usuario += 1
                    numero_usuario = input("Seu palpite: ")
                    numero_usuario = retornar_inteiro(numero_usuario)
                    if isinstance(numero_usuario, int):
                        palpite_correto = avaliar_palpite(numero_usuario, numero_sorteado)
                        match palpite_correto:
                            case "certo":
                                print(f"Parabéns! Você acertou o número {numero_sorteado} em {tentativas_usuario} tentativas.")
                                venceu = True
                                break
                            case _:
                                if palpite_correto == "maior":
                                    print("Número sorteado é Menor do que seu ultimo palpite! Tente novamente")
                                    delay(2)
                                    limpar_tela()
                                else:
                                    print("Número sorteado é Maior do que seu ultimo palpite! Tente novamente")
                                    delay(2)
                                    limpar_tela()
                    else:
                        print(f"Escolhe um número válido! Tente novamente.")
            else:
                print("Escolhe um número válido! Tente novamente.")
                delay(1)
                limpar_tela

if __name__ == "__main__":
    main()