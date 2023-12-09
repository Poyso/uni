x = input("Inserire stringa: ")
vocali = ""


def ez(x):
    r = ""
    i = 0
    while i < len(x):
        if x[i] in vocali:
            r += x[i]
        i += 1
    return r


def vocalif(x):
    v = ""
    g = ""
    for c in x:
        if c in "aeiou":
            v += c
        else:
            g += c
    tupla = (v, g)
    return tupla


print(vocalif(x))
