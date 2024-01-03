# 백준 제곱수 찾기
# https://www.acmicpc.net/problem/1025
def check_sqrt(num : int) :
    global answer
    if (num**(1/2)) % 1 == 0:
        answer = max(num, answer)

def check_range(r,c) :
    if 0 <= r < n and 0 <= c < m :
        return True
    else :
        return False


n,m = map(int,input().split())
arr = [list(input()) for _ in range(n)]

answer = -1
for i in range(n) :
    for j in range(m) :
        for dr in range(-n,n) :
            for dc in range(-m,m) :
                if dr == dc == 0 :
                    continue
                temp = ""
                cr = i
                cc = j
                while check_range(cr,cc) :
                    temp += arr[cr][cc]
                    check_sqrt(int(temp))
                    cr += dr
                    cc += dc

print(answer)