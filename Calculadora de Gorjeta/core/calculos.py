def calcular_gorjeta(valor_compra, porcentagem_gorjeta):
    valor_gorjeta = valor_compra * (porcentagem_gorjeta / 100)
    total_pagar = valor_compra + valor_gorjeta
    return valor_gorjeta, total_pagar