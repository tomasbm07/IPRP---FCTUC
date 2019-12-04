pos = {}
string = 'x22ddd cbba'
new_list = []

for num, element in enumerate(string):
    pos[element] = pos.get(element, []) + [num]
# print(pos)


def processa(string):
    a = 0
    elements = list(pos.keys())
    positions = list(pos.values())
    reps = {}
    print(elements)
    # print(positions)

    for x in range(len(string) - 1):
        if string[x] == string[x+1]:
            reps[string[x]] = reps.get(string[x], 0) + 1
    print(reps)

    keys = list(reps.keys())
    print(keys)

    for i in range(len(elements)):
        for j in range(len(keys)):
            if elements[i] == keys[j]:
                a = reps.get(keys[j])
                break
            else:
                a = 0
        new_list.append((elements[i], positions[i][0], a))
    print(new_list)


processa(string)
