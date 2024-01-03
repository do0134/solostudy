# 백준 1750 암호 만들기

def dfs(crypto, odd_cnt, idx):
    if len(crypto) == l:
        if l - odd_cnt >= 2 and odd_cnt >= 1:
            print(crypto)
        return
    elif l - len(crypto) > c-idx-1:
        return
    for i in range(idx+1,c):
        temp = 0
        if arr[i] in ("a","e","o","u","i"):
            temp = 1
        dfs(crypto+arr[i],odd_cnt+temp, i)


l,c = map(int,input().split())
arr = list(input().split())
arr.sort()
dfs("", 0, -1)