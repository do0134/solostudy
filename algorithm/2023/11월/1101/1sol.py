# 백준 19532 수학은 비대면강의입니다

a,b,c,d,e,f = map(int,input().split())

flag = False

for i in range(-999,1000):
    for j in range(-999,1000):
        if a*i+b*j == c and d*i+e*j == f:
            flag = True
            print(i,j)
            break
    if flag:
        break