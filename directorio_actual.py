def directorio():
	import os
	# dirección absoluta completa del módulo en el que se está trabajando
	ruta_modulo = os.path.abspath(__file__)
	# nombre del directorio que contiene el archivo activo:
	directorio_modulo = os.path.dirname(ruta_modulo)
	return directorio_modulo

print(__file__)