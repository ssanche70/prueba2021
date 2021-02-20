digitos = {'0':'S','1':'U','2':'T','3':'P','4':'A','5':'G','6':'M','7':'E','8':'L','9':'C'}

texto = str(input('Ingrese 10 numeros'))

if len(texto) == 10:
    for i in texto:
        print(digitos[i], end="")
else:
    print('Son solo 10 numeros')