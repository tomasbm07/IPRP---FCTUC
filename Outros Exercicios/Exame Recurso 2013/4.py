dic = {'esta': ['es', 'ta'], 'linha': ['li', 'nha'], 'parece': ['pa', 're', 'ce'],
       'demasiado': ['de', 'ma', 'si', 'a', 'do'],
       'longa': ['lon', 'ga'], 'e': ['e'], 'vai': ['vai'], 'bocados': ['bo', 'ca', 'dos'],
       'de': ['de'], 'ser': ['ser'], 'dividida': ['di', 'vi', 'di', 'da'], 'aos': ['aos']}


def hifenar(string, size, dicio):
    tamanho = 0
    sub_string = ''
    word = ''

    for i in range(len(string)):
        tamanho += 1
        word += string[i]
        if string[i] == ' ':
            word = ''
        if tamanho == size:
            for j in dic.keys():
                if word in j and len(j) > 2:

                    if tamanho + len((dicio.get(j))[0]) > size:
                        sub_string += '\n'
                        sub_string += (dicio.get(j))[0]

                    sub_string = sub_string[:i - len((dicio.get(j))[0])]
                    sub_string += (dicio.get(j))[0]

            sub_string += '-\n'
            sub_string += string[i]
            tamanho = 0
        else:
            sub_string += string[i]
    return sub_string


a = 'esta linha parece demasiado longa e vai ser dividida aos bocados'
print(hifenar(a, 21, dic))

