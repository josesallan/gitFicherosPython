import shelve

import os
# dirección absoluta completa del módulo en el que se está trabajando
ruta_modulo = os.path.abspath(__file__)
# nombre del directorio que contiene el archivo activo:
directorio_modulo = os.path.dirname(ruta_modulo)
nombrefichero = directorio_modulo + '/best_scores.dato'

mejores_marcas = shelve.open(nombrefichero)
mejores_marcas['1'] = ["no score", 0]
mejores_marcas['2'] = ["no score", 0]
mejores_marcas['3'] = ["no score", 0]
mejores_marcas.close()


