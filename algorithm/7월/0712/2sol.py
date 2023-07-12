# 백준 2258 정육점
# https://www.acmicpc.net/problem/2258

from collections import defaultdict

n, m = map(int,input().split())
meats = [list(map(int,input().split())) for _ in range(n)]
meats_dict = defaultdict(list)

for w,c in meats:
    meats_dict[c].append(w)

answer = 2147483648
temp = 0
for i in sorted(meats_dict.keys()):
    temp_sum = sum(meats_dict[i])
    temp += temp_sum
    if temp >= m:
        meats_dict[i].sort(reverse=True)
        temp_cost = temp - temp_sum
        cnt = 0
        if answer == 2147483648:
            for j in meats_dict[i]:
                temp_cost += j
                cnt += 1
                if temp_cost >= m:
                    answer = min(answer, i*cnt)
                    break
        else:
            answer = min(answer, i)

if answer == 2147483648:
    print(-1)
else:
    print(answer)
"""
10 14
2 3
2 4
2 5
3 1
1 3
7 9
7 3
8 4
10 3
3 10

4 3
1 2
3 2
2 2
5 7

10 10
2 3
2 4
2 5
3 1
1 3
7 9
7 3
8 4
10 3
3 10
"""
