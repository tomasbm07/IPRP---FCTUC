import faker
fake = faker.Faker()

path_file_numbers = 'C:\\Users\\tomas\Desktop\\UC\\2019-2020\\1º Semestre\\IPRP\\Exercicios\\7\\7_14\\telefone.txt'
path_file_morada = 'C:\\Users\\tomas\Desktop\\UC\\2019-2020\\1º Semestre\\IPRP\\Exercicios\\7\\7_14\\moradas.txt'
path_file_nomes = 'C:\\Users\\tomas\Desktop\\UC\\2019-2020\\1º Semestre\\IPRP\\Exercicios\\7\\7_14\\nomes.txt'


def generate(num):
    file_morada = open(path_file_morada, 'w')
    file_nomes = open(path_file_nomes, 'w')
    for i in range(num+1):
        file_nomes.write('{}\n'.format(fake.name()))
        file_morada.write('{}\n'.format(fake.address()))
    file_morada.close()
    file_nomes.close()


generate(1000)
file_numbers = open(path_file_numbers, 'r')
file_morada = open(path_file_morada, 'r')
file_nomes = open(path_file_nomes, 'r')
numbers = file_numbers.readlines()
morada = file_morada.readlines()
nomes = file_nomes.readlines()
file_numbers.close()
file_nomes.close()
file_morada.close()

for i in range(len(numbers)):
    numbers[i] = numbers[i].strip().strip('\n').split(',')
    nomes[i] = nomes[i].strip('\n')
    morada[i] = morada[i].strip('\n')

for i in range(0, len(morada), 2):
    morada[i] = morada[i].split('\n')

print(numbers)
print(nomes)
print(morada)



