def d(n, initial, k):
    c = []
    for i in range(len(initial)):
        c.append([i, initial[i]])
    print(c)

    c.sort(reverse=True, key=lambda x: x[1])

    print(c)

    for i in range(k):
        c[i][1] += k

    print(c)

    return c[:3]



print(d(4, [3,8,10,9], 2))
