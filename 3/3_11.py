def e3_11():
    adn = input("type uma cadeia de ADN (A, C, T, G): ")
    # A-C \ C-A \ T - G \ G - T
    final = ''
    for i in range(len(adn)):
        if adn[i] == 'A':
            final += 'T'

        if adn[i] == 'C':
            final += 'A'

        if adn[i] == 'T':
            final += 'G'

        if adn[i] == 'G':
            final += 'T'
    print(final)