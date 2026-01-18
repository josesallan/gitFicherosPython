from directorio_actual import directorio
ruta_modulo = directorio() + '/1.txt'
fichero = open(ruta_modulo).read()
print(fichero[10: 17])
for car in range(10, 17, 1):
    print(fichero[car].upper())