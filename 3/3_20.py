passe = input('Type a password: ')
spacing = input('Type the spacing between each letter: ')

def encode():
    global total
    total = ''
    #97-122 | a-z | ord(97) = a | chr('a') = 97
    for i in range(len(passe)):
        crypt = ((int(ord(passe[i])) - 97 + int(spacing)) % 26) + 97
        total += str(chr(crypt))
    print('Your encrypted password is:', total)
    return total

def decode():
    de_total = ''
    #97-122 | a-z | ord(97) = a | chr('a') = 97
    for i in range(len(total)):
        de_crypt = ((int(ord(total[i])) - 97 - int(spacing)) % 26) + 97
        de_total += str(chr(de_crypt))
    print('Your decripted password is:', de_total)


encode()
decode()
