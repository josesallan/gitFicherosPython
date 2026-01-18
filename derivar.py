def fun(xx):
	yy = 3 * xx * xx + 1
	return yy

import os
# dirección absoluta completa del módulo en el que se está trabajando
ruta_modulo = os.path.abspath(__file__)
# nombre del directorio que contiene el archivo activo:
directorio_modulo = os.path.dirname(ruta_modulo)
ruta_archivos = directorio_modulo + "/coordenadas.csv"
fichero = open(ruta_archivos,"w")
for xx in range(-30,31):
	x = xx / 100 
	y = fun(x)
	y2 = fun(x + 0.01)
	derivada = (y2 - y)/0.01
	print(derivada)
	print(x, y)
	fichero.write(str(x))
	fichero.write(",")
	fichero.write(str(y))
	fichero.write(",")
	fichero.write(str(derivada))
	fichero.write("\n")