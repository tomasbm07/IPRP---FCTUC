num = int(input('Digite um numero: '))
print('Tabuada do numero ', num )
print('--------------------')
for i in range(10):
    valor = num * (i+1)
    print('{} x {} = {}'.format(num,i+1,valor))