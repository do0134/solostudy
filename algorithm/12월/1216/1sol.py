# 백준 12018 Yonsei ToTo

n,m = map(int,input().split())
arr = list()
answer = 0

for _ in range(n):
    p,l = map(int,input().split())
    people = list(map(int,input().split()))
    if p < l:
        answer += 1
        m -= 1
        if not m:
            break
    elif p == l:
        arr.append(max(min(people),1))
    else:
        people.sort()
        arr.append(people[p-l])

arr.sort()
for i in arr:
    if i:
        m -= i
    else:
        m -= 1
    if m < 0:
        break
    else:
        answer += 1


print(answer)

"""
3 2
2 4
36 36
2 4
36 36
2 4
36 36
"""