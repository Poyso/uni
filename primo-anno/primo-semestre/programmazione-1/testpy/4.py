N = ['B', 'A', 'D', 'F', 'E', 'C']
P = [2, 0, 6, 9, 7, 3]
E = []


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


def disenga_linea(p, N, c):
    linea = ""
    for x in range(min(p), max(p)+1):
        if x in P:
            i = P.index(x)
            nome = N[i]
            if nome in c:
                linea += '*'
            else:
                linea += "+"
        else:
            linea += " "
    return linea


print(disenga_linea(P, N, c))


# Dimensione temporale e' Theta(n*n)
# Dimensione spazioale e' Theta(n) cioe la dimensione di E
