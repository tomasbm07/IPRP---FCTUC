frase = input('Digite uma frase: ')
total = ''
for i in range(len(frase)):
    print(total + frase[i])
    total += frase[i]