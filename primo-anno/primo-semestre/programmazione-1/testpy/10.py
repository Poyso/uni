f = open("test.txt")
d = {}
for line in f:
    for x in line:
        if x >= 'a' or x <= 'z' or x >= 'A' or x <= 'Z':
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
print(d)
