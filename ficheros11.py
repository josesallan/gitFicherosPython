# Importo el módulo pickle de la biblioteca estándar
import pickle
# Abro el archivo donde voy a guardar los datos, modo rb OJOOO
fichero = open('notas.pkl', 'rb')
notas = pickle.load(fichero)
suma = 0
i = 0
for dato in notas:
    print(dato[0], '->\t', dato[1])
    suma = suma + dato[1]
    i = i + 1
media = suma / i
print('Calificación media obtenida:', media)
