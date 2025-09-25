def verificar_item(item, lista):
    return item in lista

lista_items = list()

def main():
    while True:
        item_desejado = str(input("Digite o item que você quer verificar: ").strip().lower())
        if item_desejado:
            if verificar_item(item_desejado, lista_items):
                print(f"O item {item_desejado} já está na lista")
            else:
                lista_items.append(item_desejado)
                print(f"O Item {item_desejado} precisa ser comprado.")
        else:
            print("Campo em branco! Digite o nome do item.")

if __name__ == "__main__":
    main()