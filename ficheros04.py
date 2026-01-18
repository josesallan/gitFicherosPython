from directorio_actual import directorio
rutafichero = directorio() + '/1.txt'
rutafichero2 = directorio() + '/4.txt'
fichero = open(rutafichero, 'r')
fichero2 = open(rutafichero2, 'w+')
for linea in fichero:
    fichero2.write(linea)
fichero.close()
fichero2.seek(10)
fichero2.write('ser rey')
fichero2.seek(0)
for linea in fichero2:
    print(linea.rstrip())
