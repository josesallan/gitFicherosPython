ingles = open('1.txt', 'r')
espanol = open('traduc.txt', 'w+')
for line in ingles:
    print(line)
    trad = input('Traducción línea:')
    espanol.write(trad + '\n')
espanol = open('traduc.txt', 'r')
for linea in espanol:
    print(linea.rstrip())
