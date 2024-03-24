# 백준 1419 등차수열의 합

l = int(input())
r = int(input())
k = int(input())

if k == 2:
    answer = r-max(l,3)+1
elif k == 3:
    answer = r//3-(max(l,6)-1)//3
elif k == 4:
    answer = r//2 - (max(l,14)-1) // 2
    if l <= 10 <= r:
        answer += 1
else:
    answer = r//5 - (max(l,15)-1)//5

if answer < 0:
    answer = 0
print(answer)

