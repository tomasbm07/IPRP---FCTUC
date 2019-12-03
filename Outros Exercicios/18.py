requirements = {0: 'At least 1 letter between [a-z]', 1: 'At least 1 number between [0-9]',
                2: 'At least 1 letter between [A-Z]',
                3: 'At least 1 character from [$#@]', 4: 'Minimum length of transaction password: 6',
                5: 'Maximum length of transaction password: 12'}

checked_requirements = {0: 'The password has at least 1 letter between [a-z]',
                        1: 'The password has at least 1 letter between [A-Z]',
                        2: 'The password has at least 1 letter between [0-9]',
                        3: 'The password has at least 1 character from [$#@]', 4: 'The password has the minimum length',
                        5: 'The password has the maximum length'}

not_checked_requirements = {0: 'The password does not have at least 1 letter between [a-z]',
                            1: 'The password does not have at least 1 letter between [A-Z]',
                            2: 'The password does not have at least 1 letter between [0-9]',
                            3: 'The password does not have at least 1 character from [$#@]',
                            4: 'The password does not have the minimum length',
                            5: 'The password does not have the maximum length'}

for i in range(len(requirements)):
    print('{}'.format(requirements[i]))

print('\n-------------------------\n')

password_input = input('Digite passwords para testar separadas por uma vírgula\n>').split(',')


def password_check(password):
    check = [int(0) for x in range(len(requirements))]
    count = 0
    print('\n\nTesting: {}.\n'.format(password))

    for x in range(len(password)):
        char = ord(password[x])
        if char >= 97 and char <= 122:
            check[0] = 1

        char = ord(password[x])
        if char >= 65 and char <= 90:
            check[1] = 1

    for x in range(len(password)):
        char = ord(password[x])
        if char >= 48 and char <= 57:
            check[2] = 1

    for x in range(len(password)):
        char = ord(password[x])
        if char == 35 or char == 36 or char == 64:
            check[3] = 1

    for x in range(len(password)):
        if len(password) >= 6:
            check[4] = 1

    for x in range(len(password)):
        if len(password) <= 12:
            check[5] = 1

    print(check)
    for b in range(len(requirements)):
        if check[b] == 1:
            count += 1
            print('{}'.format(checked_requirements[b]))
        else:
            print('{}'.format(not_checked_requirements[b]))
    return count


# password_check('ABd1234@1')
# ABd1234@1,a F1#,2w3E*,2We3345
# print(password_input)

for a in range(len(password_input)):
    # print(password_input[a])
    # password_check(password_input[a])
    if password_check(password_input[a]) == 6:
        print('{} meets all the requirements!'.format(password_input[a]))
