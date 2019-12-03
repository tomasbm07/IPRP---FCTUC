x = (input('Digite as cordenadas de x = ')).split()
y = (input('Digite as cordenadas de y = ')).split()

def produto():
    result = []
    idk = 0
    for i in range(len(x)):
        result.append(int(x[i]) * int(y[i]))
        idk += int(result[i])
    print('{} x {} = {}'.format(x, y, idk))

if len(x) == len(y):
    produto()
else:
    print('-----Erro-----')
