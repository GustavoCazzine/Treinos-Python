import os
import time

#limpar o terminal para melhor organização
def limpar_tela():
    return os.system("cls")

#Cria titulos padronizados
def criar_titulo(titulo):
    print("-" * (len(titulo) + 5))
    print(f"{titulo.center(len(titulo) + 5)}")
    print("-" * (len(titulo) + 5))

#Adicionar um delay de segundos
def delay(segundos):
    time.sleep(segundos)