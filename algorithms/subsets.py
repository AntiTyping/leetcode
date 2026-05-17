def search(s, k, n):
    if k == n:
        print(s)
    else:
        search(s, k+1, n)
        s.add(k)
        search(s, k+1, n)
        s.remove(k)

search(set(), 0, 3)