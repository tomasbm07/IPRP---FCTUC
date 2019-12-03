def soma(list):
    new_list = [0]
    result = 0
    for i in range((len(list))):
        if i == 0:
            new_list[0] = list[0]
            result = list[0]
        else:
            new_list.append(list[i] + result)
            result += list[i]
    return(new_list)


print(soma([1, 2, 3]))
