dia_semana = {1: 'Domingo', 2: 'Segunda-feira', 3: 'Terça-feira', 4: 'Quarta-feira', 5: 'Quinta-feira', 6: 'Sexta-feira', 7: 'Sábado'}
mes = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}

def convert(data):
    print('{}, {} de {} de {}'.format(dia_semana[data[0]], data[1], mes[data[2]], data[3]))


date = input('Digite uma data: ').split('/')

for i in range(len(date)):
    date[i] = int(date[i])

#print(date)
convert(date)
#convert([1,7,1,2001])
