palavra = input('Digite uma palavra: ')
for i in range(len(palavra)):
    for a in range(len(palavra)):
        if palavra[i] == palavra[a]:
            palavra.replace(palavra[i], '')
print(palavra)
