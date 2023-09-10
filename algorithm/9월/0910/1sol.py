# 백준 4779 칸토어 집합

def dfs(idx):
    if not idx:
        return "-"
    return dfs(idx-1) + " "*(3**(idx-1)) + dfs(idx-1)


while True:
    try:
        n = int(input())
    except:
        break
    s = dfs(n)
    print(s)