import os
# dirección absoluta completa del módulo en el que se está trabajando
ruta_modulo = os.path.abspath(__file__)
# nombre del directorio que contiene el archivo activo:
directorio_modulo = os.path.dirname(ruta_modulo)


titulo = input('Título de la canción: ')
autor = input('Nombre del autor: ')
nombreorigen = directorio_modulo + '/1.txt'
nombrefichero = directorio_modulo + '7' + titulo + '.txt'
origen = open(nombreorigen)
final = open(nombrefichero, 'w+')
final.write(titulo + ' - ')
final.write(autor + '\n')
for linea in origen:
    final.write(linea)
final = open(nombrefichero, 'r')
for lineara in final:
    print(lineara.rstrip())
