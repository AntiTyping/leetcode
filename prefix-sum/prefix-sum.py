a = [8, 3, -2, 4, 10,-1, 0, 5,3]

p = [0] * len(a)
p[0] = a[0]

for i in range(1, len(a)):
   p[i] = p[i-1] + a[i]

def rangeQuery(prefixSums, i, j):
   if i == 0:
      return prefixSums[j]
   else:
      return prefixSums[j] - prefixSums[i-1]

# print(list(range(1,10)))
print(a)
print(p)

print(rangeQuery(p, 0,1))
