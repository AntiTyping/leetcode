size = 3
a = [5, 2, 8, 14, 3]
#    0  1  2   3  4

i = 0
sum = 0
answer = []
while i < len(a):
    sum += a[i]
    if i >= size:
        sum -= a[i-size]
    if i >= size -1:
        answer.append(sum / float(size))
    i += 1

print(answer)