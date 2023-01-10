from collections import deque

target = list(input())
target2 = ''
for i in range(len(target)):
    target2 += target[i]
    target[i] = int(target[i])

answer = abs(100-int(target2))
arr2 = []
n = int(input())
if n > 0 :
    arr = list(map(int,input().split()))
    for i in range(10):
        if i not in arr:
            arr2.append(str(i))

if target2 == '100':
    print(0)
elif n == 0:
    print(min(len(target),answer))
elif n == 10:
    print(abs(100-int(target2)))
else:
    stack = list()
    for i in arr2:
        stack.append(i)
    l = len(target2)
    while stack:
        cn = stack.pop()
        answer = min(answer,len(cn)+abs(int(cn)-int(target2)))
        for i in arr2:
            nn = cn + str(i)
            if len(nn) < l+2:
                stack.append(nn)

    print(answer)





    pass
