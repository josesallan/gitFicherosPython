fichero = open('coordenadas.txt').read()

a = 1
b = 5
c = 6
d = 10
x = acx = float(fichero[a:b])
y = acy = float(fichero[c:d])
disparos = 1
xmed = acx / disparos
ymed = acy / disparos
print('Disparo', disparos, ':\t x=', '{0:.2f}'.format(x), 'y = ', '{0:.2f}'.format(y), '\t xmed=', '{0:.3f}'.format(xmed), 'ymed=', '{0:.3f}'.format(ymed))

for i in range(2, 501, 1):
    a = a + 12
    b = b + 12
    c = c + 12
    d = d + 12
    disparos = disparos + 1
    x = float(fichero[a:b])
    y = float(fichero[c:d])
    acx = acx + x
    acy = acy + y
    xmed = acx / disparos
    ymed = acy / disparos
    print('Disparo', disparos, ':\t x=', '{0:.2f}'.format(x), 'y = ', '{0:.2f}'.format(y), '\t xmed = ', '{0:.3f}'.format(xmed), 'ymed=', '{0:.3f}'.format(ymed))
