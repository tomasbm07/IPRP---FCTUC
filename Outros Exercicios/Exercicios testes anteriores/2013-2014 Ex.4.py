file = open('Horário.txt', 'r')
lines = file.readlines()
file.close()
salas = []
time = []

for i in range(len(lines)):
    lines[i] = lines[i].strip('\n').split()
    salas.append(lines[i][-1])


def escrever():
    for i in range(len(salas)):
        file = open('Ocupação da Sala {}'.format(salas[i]), 'r')
        test = file.readlines()
        file.close()
        if test != []:
            file = open('Ocupação da Sala {}'.format(salas[i]), 'a')
            file.write('{} {} {} {} {}\n'.format(lines[i][0], lines[i][1], lines[i][2], lines[i][3], lines[i][4]))
            file.close()
        else:
            file = open('Ocupação da Sala {}'.format(salas[i]), 'w')
            file.write('{} {} {} {} {}\n'.format(lines[i][0], lines[i][1], lines[i][2], lines[i][3], lines[i][4]))
            file.close()


# print(lines)
# print(salas)

for i in range(len(lines)):
    time.append(lines[i][1])

for i in range(len(time)):
    for j in range(len(time[i])):
        if time[i][j] != ':':
            int(time[i][j])

print(time)

# escrever()
