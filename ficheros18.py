import random
import shelve
import os

print("VANILLA UNICORN")
print("---------------")
nombre = input("nombre:")
while True:
	try:
		dinero = input("Cuanto dinero quieres apostar?:")
		dinero = float(dinero)
		if dinero < 0:
			raise EOFError
		if dinero == float(dinero):
			break
	except ValueError:
		print("Eso no es un numero")
	except EOFError:
		print("Tiene que ser un numero positivo")
total = 0
respuesta = "s"
while True:
	nr1 = random.randint(1, 5)
	nr2 = random.randint(1, 5)
	nr3 = random.randint(1, 5)
	if respuesta == "n":
		print("Programa terminado:")
		break
	if respuesta == "s":
		print("-----------------------------")
		print("Tirada:		/", nr1, "/", nr2, "/", nr3, "/")
	if nr1 == 5 and nr2 == 5 and nr3 == 5:
		print("Todos los numeros son 5!")
		total = dinero * 10
		ganancias = total - dinero
		dinero = total
		print("!Has ganado " + str(ganancias) + "€. Ahora tienes " + str(total) + "€")
	elif nr1 == 5 and nr2 == 5 or nr2 == 5 and nr3 == 5 or nr1 == 5 and nr3 == 5:
		print("Has sacado dos 5!")
		total = dinero * 4
		ganancias = total - dinero
		dinero = total
		print("!Has ganado " + str(ganancias) + "€. Ahora tienes " + str(total) + "€")
	elif nr1 == 5 and nr2 == nr3 or nr2 == 5 and nr1 == nr3 or nr3 == 5 and nr1 == nr2:
		print("Ha sacado un 5 y dos numeros iguales!")
		total = dinero * 3
		ganancias = total - dinero
		dinero = total
		print("!Has ganado " + str(ganancias) + "€. Ahora tienes " + str(total) + "€")
	elif nr1 == nr2 == nr3:
		print("Los tres numeros son iguales")
		total = dinero * 5
		ganancias = total - dinero
		dinero = total
		print("!Has ganado " + str(ganancias) + "€. Ahora tienes " + str(total) + "€")
	elif nr1 == nr2 or nr1 == nr3 or nr2 == nr3:
		print("Dos de los numeros son iguales")
		total = dinero * 2
		ganancias = total - dinero
		dinero = total
		print("!Has ganado " + str(ganancias) + "€. Ahora tienes " + str(total) + "€")
	elif nr1 == 5 or nr2 == 5 or nr3 == 5:
		print("Recuperas tu dinero!")
	elif nr1 != nr2 and nr2 != nr3 and nr1 != nr3 and nr1 != 5 and nr2 != 5 and nr3 != 5:
		print("Ningun numero es igual, has perdido todo tu dinero!")
		break
	respuesta = input("Pulsa n para terminar, o, s para seguir jugando:")

""" Sección para determinar si hay que guardar la última puntuación
puntuacion"""
# nombre es la variable que almacena el nombre
# dinero es la variable que hay que estudiar


# dirección absoluta completa del módulo en el que se está trabajando
ruta_modulo = os.path.abspath(__file__)
# nombre del directorio que contiene el archivo activo:
directorio_modulo = os.path.dirname(ruta_modulo)
nombrefichero = directorio_modulo + '/best_scores.dato'

best_scores = shelve.open(nombrefichero)

if dinero > best_scores['1'][1]:
	best_scores['3'] = best_scores['2']
	best_scores['2'] = best_scores['1']
	best_scores['1'] = [nombre, dinero]
elif dinero > best_scores['2'][1]:
	best_scores['3'] = best_scores['2']
	best_scores['2'] = [nombre, dinero]
elif dinero > best_scores['3'][1]:
	best_scores['3'] = [nombre, dinero]


print("1º", best_scores['1'][0], best_scores['1'][1])
print("2º", best_scores['2'][0], best_scores['2'][1])
print("3º", best_scores['3'][0], best_scores['3'][1])
