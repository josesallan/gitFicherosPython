mates = int(input('Calificación Matemáticas:'))
lengua = int(input('Calificación Lengua:'))
historia = int(input('Calificación Historia:'))
tic = int(input('Calificación TIC II:'))
notas = [['Matemáticas', mates], ['Lengua', lengua], ['Historia', historia], ['TIC II', tic]]
media = (mates + lengua + historia + tic) / 4
print(notas)
print('Calificación media obtenida:', media)
