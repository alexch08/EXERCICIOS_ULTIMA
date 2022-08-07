peso=float(input('Digite seu peso: \n'))
print(peso)
altura = float(input('Digte sua altura:\n'))
while peso<=0:
    print('Peso inválido')
    peso=float(input('Digite seu peso\n'))
    continue
while altura <=0:
    print('Altura inválida')
    altura=float(input('Digite sua altura\n'))
    continue
imc=peso / (altura ** 2)
if imc > 30:
	print('Você está obeso')
else:
	if imc >25:
		print('Você está acima do peso')
	elif imc > 18.5:
		print('Você está com peso normal')
	elif imc <= 18.5:
		print('Você está abaixo do peso')