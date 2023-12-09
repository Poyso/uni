a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 11


def ricerca(a, k):
    rx = len(a)
    sx = 0
    if k > a[sx] or k < a[rx]:
        return "l' elemento non esiste nella lista"
    while rx > sx:
        ck = (rx+sx)//2
        if k == a[ck]:
            return ck
        else:
            if a[ck] > k:
                rx = ck
            else:
                sx = ck


print(ricerca(a, k))


# Dictionary
# e una sequenza di coppie in cui in una coppia
# appartiene una chiave e un valore
# il valore e' un valore qualsiasi
# la chiave e' un qualcosa unica che identifica quel valore
# python e' la chiave e 5 e' il valore
c = {"python": 5, 3: 3}
print(c)
