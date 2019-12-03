string = 'Just a random fucking phrase'
string = string.lower()
rep = {}
pos = {}
inv = {}

print('Repetições numa string')
for num, element in enumerate(string):
    rep[element] = rep.get(element, 0) + 1
print(rep)

print('\nPosições numa string')
for i, x in enumerate(string):
    pos[x] = pos.get(x, []) + [i]
print(pos)

print('\nInverter um dicionário')
items = rep.items()
for keys, values in items:
    inv[values] = inv.get(values, []) + [keys]
print(inv)

print('\nHistograma')
keys = list(rep.keys())
values = list(rep.values())

for i in range(len(keys)):
    print(keys[i], '*' * values[i])
