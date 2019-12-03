frase = input('Digite uma frase: ')
total = ''
frase = frase[::-1]
for i in range(len(frase)):
    print(frase[i] + total)
    total = frase[i] + total