from core.contador import contador_vogais

"""
Recebe uma frase do usuario, chama a função de contagem de vogais e imprime o resultado
"""

def main():
    frase = str(input("Digite um texto:"))
    qtd_vogais = contador_vogais(frase)
    print(f"O texto contém {qtd_vogais} vogais.")


if __name__ == "__main__":
    main()