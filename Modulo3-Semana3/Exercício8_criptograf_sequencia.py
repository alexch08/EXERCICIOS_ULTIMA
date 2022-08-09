# palavra += chr(int(codigo_letra))
mensagem_criptografada = ['8', '5', '-1', '7', '6', '-1', '8', '4', '-1', '7', '3', '-1', '7', '7', '-1', '6', '5', '-1']
letra_atual = str()
palavra = str()
for i in mensagem_criptografada:
    if i != '-1':
        letra_atual += i
    else:
        palavra += chr(int(letra_atual))
        letra_atual = str()
print(palavra)
