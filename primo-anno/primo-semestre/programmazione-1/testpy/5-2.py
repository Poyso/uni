x = [1, 2, 10, 4, 5, 6]
n = len(x)


# Selection sort
def selection_sort(x, n):
    for i in range(n):
        for k in range(n):
            if x[i] < x[k]:
                x[i], x[k] = x[k], x[i]
    return x


def bubble_sort(x, n):
    for c in range(n):
        sorted = True
        for i in range(n-1-c):
            if x[i] > x[i+1]:
                sorted = False
                x[i], x[i+1] = x[i+1], x[i]
        if sorted:
            print("Funzione gia ordinata")
            break
    return x


print(bubble_sort(x, n))
