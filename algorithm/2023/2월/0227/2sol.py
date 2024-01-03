# 백준 A와 B
# https://www.acmicpc.net/problem/12904
origin = list(input())
target = list(input())

while len(origin) < len(target) :
    if target[-1] == "A" :
        target = target[:len(target)-1]
    elif target[-1] == "B" :
        target = target[:len(target)-1]
        target = target[::-1]

if origin == target :
    print(1)
else :
    print(0)