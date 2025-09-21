from core.controle import definir_vencedor, jogar_maquina, validar_jogada

def main():
    while True:
        jogada_jogador = input("Escolha: pedra, papel ou tesoura? ").strip().lower()
        jogada_maquina = jogar_maquina()

        if validar_jogada(jogada_jogador, jogada_maquina):
            vencedor = definir_vencedor(jogada_jogador, jogada_maquina)
            match vencedor:
                case "Empate":
                    print("Empate! ambos os jogadores jogaram iguais")
                case "Jogador 1":
                    print(f"Você venceu! Você jogou {jogada_jogador} e seu adversário {jogada_maquina}.")
                case "Jogador 2":
                    print(f"Você perdeu! Você jogou {jogada_jogador} e seu adversário {jogada_maquina}.")
                case _:
                    print("Erro inesperado, tente novamente.")
        else:
            print("Digite uma jogada válida.")

if __name__ == "__main__":
    main()