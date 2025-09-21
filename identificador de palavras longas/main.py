from core.identificador import identificar_maior_palavra

#Verificador simples da palavra mais longa

def main():
    entrada_texto_usuario = str(input("Digite um texto: "))
    maior_palavra = identificar_maior_palavra(entrada_texto_usuario)
    if len(maior_palavra) == 0:
        print("Nenhuma palavra longa foi encontrada no texto.")
    else:
        print(f"Palavras longas encontradas: {maior_palavra}")

    
if __name__ == "__main__":
    main()