"""Crea un programa que utilizando el módulo shelve gestione una base de datos con los
alumnos de un centro. Se debe almacenar su código (código de matrícula), nombre,
dirección y curso. Como clave usarás el código del alumno. Almacena diez estudiantes en
el almacén"""

import shelve
archivo = shelve.open("fichero")
archivo["1"] = "hola"
print(archivo)
a, b, c = input("hik")