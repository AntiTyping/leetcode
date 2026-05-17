a = [8, 3, -2, 4, 10,-1, 0, 5,3]

# Using extra [0] at the beginning so -1 indexing works
p = [0] * (len(a) + 1)
p[1] = a[0]

for i in range(1, len(a)):
   p[i+1] = p[i-1] + a[i]

print(p)

print(p[5] - p[4])
