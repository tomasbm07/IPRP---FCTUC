def copia(original, novo):
    original_file = open(original, 'r')
    original_lines = original_file.readlines()
    original_file.close()
    novo_file = open(novo, 'w')
    novo_file.writelines(original_lines)
    novo_file.close()


copia('primeiro.txt', 'copia_primeiro.txt')
