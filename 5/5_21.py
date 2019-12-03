cad = input('Digite uma cadeia: ')
sub_cad = input('Digite uma cadeia complememtar: ')
index = cad.find(sub_cad)

if (index != -1):
    print('a cadeia: {}, está contida em: {}'.format(sub_cad,cad))
    print('o seu index é: {}'.format(index))
else:
    print('A subcadeia não está contida na cadeia principal')
    print('Logo o Index é: {}'.format(index))