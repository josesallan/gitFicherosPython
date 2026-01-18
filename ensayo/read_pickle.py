import pickle
file = open("hola.pkl", "br")
alumnos_leidos = pickle.load(file)
print(alumnos_leidos)
