import datetime

vendas = 'C:\\Users\\tomas\\Desktop\\UC\\2019-2020\\1º Semestre\\IPRP\\Exercicios\\7\\7_11\\vendas.txt'
numero = 'C:\\Users\\tomas\\Desktop\\UC\\2019-2020\\1º Semestre\\IPRP\\Exercicios\\7\\7_11\\nº vendas.txt'

day = datetime.datetime.now().day
month = datetime.datetime.now().month
year = datetime.datetime.now().year

data = ('{}/{}/{}'.format(day, month, year))

def recibo(file, number, empresa, nc, data, valor, vendedor):
    file.write('Venda a Dinheiro No {}\n'.format(number))
    file.write('--------------------------\n')
    file.write('Empresa: {}\n'.format(empresa))
    file.write('N.C: {}\n'.format(nc))
    file.write('Data: {}\n'.format(data))
    file.write('Valor: {}\n'.format(valor))
    file.write('Vendedor: {}\n'.format(vendedor))
    file.write('\n')


file_vendas = open(vendas, 'a')
file_number = open(numero, 'r')
sale_number = file_number.read()
file_number.close()
file_number = open(numero, 'w')
sale_number = int(sale_number) + 1
file_number.write(str(sale_number))
file_number.close()

nc = input('Digite o NIF: ')
valor = input('Digite o valor: ')
vendedor = input('Vendedor: ')

recibo(file_vendas, sale_number, 'Vendas & Vendas', nc, data, valor, vendedor)
file_vendas.close()

