lista_voluntarios = list()

while True:
    nome_voluntario = input("Digite o nome do voluntário (ou 'sair' para encerrar): ").lower().strip()

    if not nome_voluntario:
        print("Campo em branco, tente novamente.")
        continue

    if nome_voluntario == "sair":
        break

    if nome_voluntario.isalpha():
        lista_voluntarios.append(nome_voluntario)
        print(f"Voluntário '{nome_voluntario.capitalize()}' adicionado com sucesso!")

    else:
        print("Erro: O nome deve conter apenas letras.")

print("\n--- Lista Final de Voluntários ---")
# Imprime a lista de forma mais legível
for nome in lista_voluntarios:
    print(nome.capitalize())