import pickle
fichero = open('secreto.pkl', 'rb')
texto = pickle.load(fichero)
texto2 = ''
print('Texto a desencriptar')
print(texto)
clave = int(input('Introduce la clave de desencriptación: '))
for letra in texto:
    car = chr(ord(letra) - clave)
    texto2 = texto2 + car
print('Texto desencriptado:')
print(texto2)
