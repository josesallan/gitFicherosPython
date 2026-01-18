import os
# dirección absoluta completa del módulo en el que se está trabajando
ruta_modulo = os.path.abspath(__file__)
# nombre del directorio que contiene el archivo activo:
directorio_modulo = os.path.dirname(ruta_modulo)
direccion_fichero = directorio_modulo + "/datos_experimento.csv"
fichero = open(direccion_fichero)
area = 0
for linea in fichero:
	datos_linea = linea.split(",")
	diferencial_area = float(datos_linea[1]) * 0.1
	area = area + diferencial_area
print("El espacio recorrido es:", area, "m2")
fichero.close()
fichero = open(direccion_fichero)
datos = fichero.readlines()
area2 = 0
for i in range (0, len(datos) - 1):
	datomin = datos[i].split(',')
	min = float(datomin[1])
	datomax = datos[i + 1].split(',')
	max = float(datomax[1])
	diferencial_area = (max + min) / 2 * 0.1
	area2 = area2 + diferencial_area
print("El espacio recorrido es:", area2, "m2")