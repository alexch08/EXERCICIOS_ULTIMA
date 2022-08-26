def decorator_imprimir(funcao):
    def wrapper():
        print('Antes da Execução')
        funcao(15000, 25, 240)
    return wrapper

@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    resultado = capital * (taxa / 100) * tempo
    print(resultado)

juros_simples()