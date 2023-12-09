import math


def radice_quadrata(a):
    return math.sqrt(a)


def radice_quarta(a):
    y = radice_quadrata(radice_quadrata(a))
    return y


def conta_parole(a):
    n, in_parola = 0, False
    for c in a:
        if c in " ":
            if in_parola:
                in_parola = False
        else:
            if not in_parola:
                in_parola = True
                n += 1
    return n


x = input("Inserire una frase: ")
print(conta_parole(x))

# debugger online per python, cpp, c, javascript e java
# python tutor ^
