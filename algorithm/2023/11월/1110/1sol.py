# 백준 9252 LCS2

s1 = input()
s2 = input()

dp = [[""]*(len(s2)+1) for _ in range(len(s1)+1)]

for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1]+s1[i-1]
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

if dp[-1][-1]:
    print(len(dp[-1][-1]))
    print(dp[-1][-1])
else:
    print(0)
