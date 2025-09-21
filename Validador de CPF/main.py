from core.validador import validar_cpf

#Validador de CPF simples
def main():
    """
    Pede um CPF ao usuário e usa a função de validação para verificar o formato
    """

    while True:
        print("\nValidador de Formato de CPF\n")
        entrada_usuario_cpf = input("Digite seu CPF: ")
        if validar_cpf(entrada_usuario_cpf):
            print("CPF válido")
        else:
            print("CPF inválido, preencha apenas números com exatos 11 digítos.")



if __name__ == "__main__":
    main()