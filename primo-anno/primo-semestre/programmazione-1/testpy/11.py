d = {'python': 5, 3: 3.14, 2: 'programmazione', 'pi': 3.14, 3.2: 'ciao'}
d['PI'] = d['pi']
d[7] = 34
a = 24
b = a
c = a
if id(b) == id(c):
    print(True)
print(d)
