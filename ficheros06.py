fichero = open('coordenadas.txt').read()
a = 1
b = 5
c = 6
d = 10
for i in range(100):
    print('X =', fichero[a: b], '- Y =', fichero[c: d])
    a = a + 12
    b = b + 12
    c = c + 12
    d = d + 12
