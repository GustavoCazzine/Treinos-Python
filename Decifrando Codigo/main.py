alfabeto = "abcdefghijklmnopqrstuvwxyz"

menssagem = "zifryx o nelfobdyu!"

def descodificar(menssagem):
    tradução_mensagem = ""
    for letras in menssagem:
        if letras in alfabeto:
            index_letra = alfabeto.find(letras)
            tradução_mensagem += alfabeto[(index_letra - 10) % 26]
        else:
            tradução_mensagem += letras

    print(tradução_mensagem)


def codificar(menssagem):
    mensagem_codificada = ""

    for letra in menssagem:
        if letra in alfabeto:
            index = alfabeto.find(letra)
            mensagem_codificada += alfabeto[(index + 10) % 26]
        else:
            mensagem_codificada += letra

    print(mensagem_codificada)


codificar("python e divertido!")

descodificar("zidryx o nsfobdsny!")