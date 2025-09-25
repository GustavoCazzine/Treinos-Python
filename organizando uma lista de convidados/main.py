lista_convidados = set()

while True:
    convidado = str(input("Digite o nome do convidado: ").lower())
    if convidado == "sair":
        print(f"Sua lista de convidados: {", ".join(nome.capitalize() for nome in lista_convidados)}")
        break
    else:
        if convidado.isalpha():
            if not convidado in lista_convidados:
                lista_convidados.add(convidado)
            else:
                print(f"{convidado} já está na lista.")
        else:
            print("Digite o nome correto do convidado")
