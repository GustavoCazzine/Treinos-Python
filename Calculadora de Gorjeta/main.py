from core.calculos import calcular_gorjeta

#Calculadora  simples de gorjeta

def main():
    while True:
        try:
            valor_total_conta = float(input("Digite o valor da conta: "))
            if valor_total_conta and valor_total_conta > 0:
                while True:
                    try:
                        porcentagem_gorjeta = int(input("Digite a porcentagem de gorjeta: "))
                        if porcentagem_gorjeta and porcentagem_gorjeta > 0:
                            valor_gorjeta, total_a_pagar = calcular_gorjeta(valor_total_conta, porcentagem_gorjeta)
                            print(f"Valor da gorjeta: R${valor_gorjeta:.2f}\n Total a pagar: R${total_a_pagar:.2f}")
                            break
                        else:
                            print("Valor incorreto, digite um valor maior que 0")
                    except ValueError:
                        print("Tipo inválido, digite um número")
            else:
                print("Valor incorreto, digite um valor maior que 0")
        except ValueError:
            print("Tipo inválido, digite um número")

if __name__ == "__main__":
    main()