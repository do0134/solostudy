# 백준 1239 차트

from itertools import accumulate, permutations

n = int(input())
arr = list(map(int,input().split()))


if max(arr) > 50:
    print(0)
elif max(arr) == 50:
    print(1)
else:
    max_v = 0
    perm = list(permutations(arr))
    for p in perm:
        temp = 0
        edge = list(accumulate(p))

        for e in edge:
            if e + 50 in edge:
                temp += 1
        max_v = max(max_v, temp)
    print(max_v)

