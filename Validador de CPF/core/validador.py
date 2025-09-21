
def validar_cpf(cpf):
    cpf = cpf.strip().replace(".", "")
    if cpf.isdigit() and len(cpf) == 11:
        return True
    else:
        return False
