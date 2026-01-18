# Importo el módulo pickle de la biblioteca estándar
import pickle
# Abro el archivo donde voy a guardar los datos, modo wb OJOOO
fichero = open('notas,pkl', 'wb')
# Pregunto:
mates = int(input('Calificación Matemáticas:'))
lengua = int(input('Calificación Lengua:'))
historia = int(input('Calificación Historia:'))
tic = int(input('Calificación TIC II:'))
# Creo la lista con las notas
notas = [['Matemáticas', mates], ['Lengua     ', lengua], ['Historia   ', historia], ['TIC II     ', tic]]
# Guardo la información en el archivo notas.pkl
pickle.dump(notas, fichero)
