file = open('primeiro.txt', 'r')
file.seek(10, 0)        # Mover o cursor antes de ler a linha
line = file.readline()  # Le a linha ate um \n de onde estiver o cursor
print(line)             # por default é o inicio do documento
char = []
file.seek(10, 0)
for i in range(7):
    char.append(line[i])
    print(line[i])
print(char)
file.close()
