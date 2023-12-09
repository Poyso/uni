a = [3, [2, [3, 1]], 7, [2, 3]]


def deep_copy(a):
    b = []
    for e in a:
        if type(e) is list:
            b.append(deep_copy(e))
        else:
            b.append(e)
    return b


def rmax(b):
    if len(b) == 1:
        return b[0]
    else:
        m = rmax(b[1:])
        if m > b[0]:
            return m
        else:
            return b[0]


# Terribile: tempo e spazio quadratico
print(rmax([7, 2, 6, 5, 4, 1]))

# Scrivere una funzione che conti gli interi data una lista a
# anche gli interi appartenenti alle sottoliste


a = [3, 5, 7, 9, 10, 21]
b = [1, 2, 6, 14, 16, 23]
# scrivere una funzione che ordini gli elementi di a e b in una
# nuova lista
