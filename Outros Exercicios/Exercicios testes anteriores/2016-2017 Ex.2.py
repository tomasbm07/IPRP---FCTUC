
pos = {}
string = 'x22ddd cbba'
new_list = []

for num, element in enumerate(string):
    pos[element] = pos.get(element, []) + [num]
print(pos)


def processa(string):
    count = 0
    elements = list(pos.keys())
    positions = list(pos.values())
    reps = [0 for i in string]
    print(elements)
    print(positions)

    for i in range(1, len(string)):
        for j in range()


    for i in range(len(elements)):
        new_list.append((elements[i], positions[i][0], 0))
    print(new_list)


processa(string)
