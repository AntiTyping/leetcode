sack = 6
items = [[2, 6], [5, 9], [4,5]]

dp = [0] * (sack + 1)
0, 1, 2, 3, 4, 5, 6
0, 0, 6, 6, 6, 6, 6
0, 0, 6, 6, 6, 9, 9
0, 0, 6, 6, 6, 9,11


for i in items:
    for j in reversed(range(sack+1)):
        if i[0] <= j:
            dp[j] = max(dp[j], dp[j-i[0]] + i[1])
    print(dp)
