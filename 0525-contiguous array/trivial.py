a = [0, 1, 1, 0, 1, 1, 0, 0]

for i in range(len(a)):
    if a[i] == 0:
        a[i] = -1

print(a)
max = 0
for i in range(len(a)):
    sum = a[i];
    for j in range(1, len(a)):
        sum += a[j]
        if sum == 0:
            if j - i + 1 > max:
                max = j - i + 1

print(max)