ternas = []

for a in range(1,1000):
    for b in range(a+1,1000):
        z=a**2+b**2
        if z**(0.5)==int(z**(0.5)):
            ternas.append([a,b,int(z**(0.5))])

for i in range(len(ternas)):
    if ternas[i][0]+ternas[i][1]+ternas[i][2]==1000:
        print(ternas[i][0],ternas[i][1],ternas[i][2])