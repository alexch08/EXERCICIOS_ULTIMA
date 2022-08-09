import string

lista_alfabeto = string.ascii_uppercase
frase_cript = 'HVWRX HPSROJDGR FRP R FXUVR GH SBWKRQ'
frase_descript = str()
for letra in frase_cript:
    print(frase_descript)
    if letra != ' ':
        frase_descript += lista_alfabeto[lista_alfabeto.index(letra)-3]
    else:
        frase_descript += letra

print(frase_descript) 
