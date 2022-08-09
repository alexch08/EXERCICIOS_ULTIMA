valor_da_etiqueta = float(input('Digite o valor da etiqueta do produto:\n'))
print(valor_da_etiqueta)
forma_de_pagamento=int(input('Digite a forma de pagamento: \n 1 - À vista Dinheiro com 15 por cento de desconto \n 2 - À vista Cartáo Credito - 10 por cento desconto \n 3 - Parcelado \n\n'))
while valor_da_etiqueta <=0:
    print('Valor inválido')
    valor_da_etiqueta = float(input('Digite o valor da etiqueta do produto:'))
    continue
while forma_de_pagamento <= 0 or forma_de_pagamento > 3:
    print('Forma de pagamento inválida \n ')
    forma_de_pagamento=int(input('Digite a forma de pagamento: \n 1 - À vista Dinheiro com 15 por cento de desconto \n 2 - À vista Cartáo Credito - 10 por cento desconto \n 3 - Parcelado \n\n'))
    continue
if forma_de_pagamento == 3:
    numero_parcelas = int(input('Digite o número de parcelas\n'))
    while numero_parcelas < 2:
        print('Número de parcelas tem que ser maior ou igual a 2: \n')
        continue
    if numero_parcelas == 2:
        preco_final = valor_da_etiqueta
    else:
        preco_final = valor_da_etiqueta + (valor_da_etiqueta*numero_parcelas*0.10)
elif forma_de_pagamento == 2:
    preco_final = valor_da_etiqueta - (valor_da_etiqueta*0.10)
else: 
    preco_final= valor_da_etiqueta - (valor_da_etiqueta * 0.15)
print(f'Preço final é de R$: {preco_final:.2f}')
