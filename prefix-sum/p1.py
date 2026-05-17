a = [8, 3, -2, 4, 10,-1, 0, 5,3]

p = [0] * len(a)
p[0] = a[0]

for i in range(1,len(a)):
  p[i] = p[i-1] + a[i]


def f(p, i, j):
  if i == 0:
    return p[j]
  else:
    return p[j] - p[i-1]

def f1(a, i, j):
  sum = 0
  for k in range(i, j):
    sum += a[k]
  return sum

print(f(p,1,4))
print(f(p,1,4))

