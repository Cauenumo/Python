# print({x:x**2 for x in range(10)})

d = {'k1':1, 'k2':2}

print(d)
#imprime as chaves
for k in d.keys():
    print(k)
#imprime os valores
for x in d.values():
    print(x)
#imprime as chaves e os valores
for i in d.items():
    print(i)