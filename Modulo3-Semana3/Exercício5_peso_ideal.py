variavel=input('Escolha H, se você for homem e M, se você for mulher\n')
print(variavel)
altura = float(input('Escolha sua altura\n'))
print(altura)

if variavel == 'H'or variavel =='h':
    print(f'Você digitou {variavel}')
    print('Você é homem')
    peso_ideal=(72.7*altura)-58
    print(f'Seu peso ideal é: {peso_ideal:.2f}')
elif variavel == 'M' or variavel == 'm':
    print('Você é mulher')
    peso_ideal=(61.1*altura)-44.7
    print(f'Seu peso ideal é: {peso_ideal:.2f}')
else:
    print('Você digitou opção inválida')