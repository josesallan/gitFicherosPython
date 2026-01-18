import pickle
fichero = open('secreto.pkl', 'wb')
texto = input('Introduce el texto a encriptar:')
clave = int(input('Introduce la clave de encriptación'))
texto2 = ''
for i in texto:
    cod = ord(i) + clave
    let = chr(cod)
    texto2 = texto2 + let
print(texto2)
pickle.dump(texto2, fichero)
