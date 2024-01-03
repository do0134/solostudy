def decode(p):
    x = 1000000
    if p[0] == "0":
        return 0
    dp = [0] * len(password)
    dp[0] = dp[1] = 1
    return dp[-1]%x


password = input()
print(decode(password))