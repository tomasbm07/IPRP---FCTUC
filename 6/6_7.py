def inverter(list):
    for i in range(len(list)):
        for a in range(len(list[i])):
            if (list[i][a] == 0):
                list[i][a] = 1
            else:
                list[i][a] = 0
    return list


print(inverter([[0, 1, 0], [1, 1, 1], [0, 1, 0]]))

