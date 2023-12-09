N = ['A', 'B', 'C', 'D', 'E']
P = [3, 7, 9, 10, 13]
E = []
linea = []
n = len(P)


for x in P:
    ecc_x = 0
    for y in P:
        if abs(x-y) > ecc_x:
            ecc_x = abs(x-y)
    E.append(ecc_x)


m = None
c = []
i = 0
while i < len(E):
    e = E[i]
    if e == m:
        c.append(N[i])
    elif m == None or e < m:
        m = e
        c = [N[i]]
    i += 1


for i in range(n):
    p = N[i]
    if p in c:
        linea.append('*')
    else:
        linea.append('+')
    if i < n-1:
        spazi = P[i+1]-P[i]-1
        linea.extend([' ']*spazi)
print(c)

linea_str = ' '.join(linea)
print(linea_str)
# Dimensione temporale e' Theta(n*n)
# Dimensione spazioale e' Theta(n) cioe la dimensione di E
