n=eval(input('introduceti numarul:'))
suma=0
for t in range  (1, n+1):
    if ((t%3==0) and (t%5==0)):
        suma=suma+t
print('Suma numerilor care se impart la 3 si 5 este ' , suma)