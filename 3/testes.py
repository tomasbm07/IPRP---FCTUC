letra = ord('b')
spacing = 26
letra_nova = ((letra - 97 + spacing) % 26) + 97
print(chr(letra_nova))
