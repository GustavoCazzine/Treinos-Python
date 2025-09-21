from unidecode import unidecode

def contador_vogais(frase):
    qtd_vogais = 0
    frase_formatada = unidecode(frase.lower())
    for letras in frase_formatada:
        if letras in "aeiou":
            qtd_vogais += 1

    return qtd_vogais