def identificar_maior_palavra(texto):
    formatacao_simples_texto = texto.strip().lower()
    lista_de_palavras = formatacao_simples_texto.split(" ")
    maior_palavra = list()
    for palavras in lista_de_palavras:
        if len(palavras) > 10:
            maior_palavra.append(palavras)
    return maior_palavra