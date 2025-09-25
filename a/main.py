
texto_1 = 'O sol brilha forte no céu azul'

texto_2 = 'O céu azul anuncia um dia de sol intenso '

palavras_comuns = list()

lista_texto_1 = texto_1.split()
lista_texto_2 = texto_2.split()


for palavras in lista_texto_1:
    if palavras in lista_texto_2:
        palavras_comuns.append(palavras)


print(f"Palavras em comum: {palavras_comuns}")