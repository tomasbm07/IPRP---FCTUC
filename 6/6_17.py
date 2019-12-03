dicio = {'joao': 10, 'pedro': 18, 'tiago': 13, 'luis': 18}
novo_dicio = {}
'''''
for chave, valor in dicio.items():
    novo_dicio[valor] = novo_dicio.get(valor, []) + [chave]
print(novo_dicio)

print(list(dicio.items()))
'''''

keys = list(dicio.keys())
values = list(dicio.values())



print(novo_dicio)
# print(keys, values)

