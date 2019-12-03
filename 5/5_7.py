p1 = input('Digite uma plavara: ')
p2 = input('Digite outra palavra do mesmo comprimento da 1ª: ')
diferente = 0

for i in range(len(p1)):
    if p1[i] != p2[i]:
        diferente += 1

percent = diferente / len(p1)

if ((diferente / len(p1)) >= 0.1):
    print('As palavras não são amigas')
else:
    print('As palavras são amigas')