ficheiro_original = '2014-2015 ex.4.txt'
ficheiro_novo = '2014-2015 ex.4_novo.txt'


def contagem(original, novo):
    soma = 0
    new_lines = []
    nums = []

    file = open(original, 'r')
    lines = file.readlines()
    file.close()

    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n').split()

    for i in range(len(lines)):
        for j in range(1, len(lines[i])):
            lines[i][j] = int(lines[i][j])
            soma += lines[i][j]
            if j == len(lines[i])-1:
                lines[i].append(soma)
                soma = 0

    for i in range(len(lines)):
        nums.append(lines[i][-1])
    nums.sort()

    for i in range(len(lines)):
        for j in range(len(nums)):
            if lines[i][-1] == nums[j]:
                new_lines.append(lines[j])
    print(new_lines)

    file = open(novo, 'w')
    for i in range(len(new_lines)):
        new_lines[i] = ''.join(str(new_lines[i])) + '\n'
        # new_lines[i].strip(',')
    print(new_lines)
    file.close()


contagem(ficheiro_original, ficheiro_novo)
