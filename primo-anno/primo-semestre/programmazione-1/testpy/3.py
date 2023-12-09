def conta_occorrenza(x, y):
    le, n, c = len(y), 0, 0
    while c < len(x)-le:
        if x[c:c+le] == y:
            n += 1
        c += 1
    return n


print(conta_occorrenza("ciaoxciao", "ciao"))
