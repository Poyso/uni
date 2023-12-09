a = [3.14, "python", 2, "programma", 0, "corso", 12]


def fun(e):
    z = (1, e) if type(e) is str else (0, e)
    return z
    #  if type(e) is str:
    #    return (1, e)
    #  else:
    #    return (0, e)


def bubble_sort(a, key):
    n = len(a)
    ordinata = False
    c = 0
    while not ordinata:
        ordinata = True
        for i in range(n-1-c):
            if key(a[i]) > key(a[i+1]):
                ordinata = False
                a[i], a[i+1] = a[i+1], a[i]
        c += 1


def f(e):
    if type(e) is str:
        return len(e)
    else:
        return e


def sortlen(a, key):
    n = len(a)
    ordinata = False
    c = 0
    while not ordinata:
        ordinata = True
        for i in range(n-1-c):
            if key(a[i]) > key(a[i+1]):
                ordinata = False
                a[i], a[i+1] = a[i+1], a[i]
        c += 1


# bubble_sort(a=a, key=fun)
sortlen(a=a, key=lambda e: len(e) if type(e) is str else e)
print(a)

b = a  # b alias di a`
c = a[:]  # c clone di a

# se modifico 'b' modifico anche 'a' perche 'b' e un alias di 'a'
# se modifico 'c' non modifico 'a' perche 'c' e un clone di 'a'
