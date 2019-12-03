profissao = {102: 'Professor', 411: 'Advogado', 203: 'Estudante'}
estado_civil = {1: 'Casado', 2: 'Solteiro'}

file = open('nomes.txt', 'r')
lines = file.readlines()
new_lines = []

for i in range(len(lines)):
    lines[i] = lines[i].strip('\n').split('/')

print(lines)
print(new_lines)
