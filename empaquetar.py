import pickle
file = open("hola.pkl","bw")
alumnos =["Luis", "Antonia", "Pep"]
pickle.dump(alumnos, file)