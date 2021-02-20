dias = ['L','M','X','J','V','S','D'] * 6

meses = ['1','3','5','7','9','10','12']

en1 = str(input('ingrese un numero del 1 al 12'))

en2 = str(input('Ingrese una letra L M X J V S D'))

pos = dias.index(en2)


arr = ""

if en1 in meses:
    if en2 in dias:
        for i in range(1,32):
            arr = arr + str(i) + str(dias[pos])
            i += 1
            pos = pos + 1
            if pos == 7:
                d = 0

    print(arr)
